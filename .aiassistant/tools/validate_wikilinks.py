# Dependencies: Python standard library only.

from __future__ import annotations

import argparse
import inspect
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


WIKILINK_PATTERN: re.Pattern[str] = re.compile(r"\[\[([^\[\]\n]+)\]\]")
FENCE_PATTERN: re.Pattern[str] = re.compile(
    r"(?ms)^[ \t]*(```|~~~).*?^[ \t]*\1[ \t]*$"
)
INLINE_CODE_PATTERN: re.Pattern[str] = re.compile(r"`[^`\n]*`")


class WikilinkValidationError(Exception):
    """Raised when wikilink validation cannot be completed."""


@dataclass(frozen=True)
class MarkdownFile:
    """
    Store metadata for a Markdown file in the vault.

    :param path: Path = absolute file path.
    :param relative_path: str = POSIX-style path relative to the vault.
    :param stem: str = Markdown file stem without suffix.
    """

    path: Path
    relative_path: str
    stem: str


@dataclass(frozen=True)
class Wikilink:
    """
    Store one wikilink found in a Markdown file.

    :param source: str = source file path relative to the vault.
    :param raw: str = raw wikilink body without brackets.
    :param target: str = normalized target before alias and heading parts.
    :param alias: str | None = optional alias text.
    :param line: int = one-based line number.
    """

    source: str
    raw: str
    target: str
    alias: str | None
    line: int


@dataclass(frozen=True)
class GraphReport:
    """
    Store the complete wikilink validation report.

    :param nodes: list[dict[str, str]] = graph nodes.
    :param edges: list[dict[str, str]] = resolved graph edges.
    :param broken_links: list[dict[str, Any]] = links without a target.
    :param ambiguous_links: list[dict[str, Any]] = links with multiple targets.
    :param malformed_links: list[dict[str, Any]] = links using unsupported syntax.
    """

    nodes: list[dict[str, str]]
    edges: list[dict[str, str]]
    broken_links: list[dict[str, Any]]
    ambiguous_links: list[dict[str, Any]]
    malformed_links: list[dict[str, Any]]

    def hasErrors(self) -> bool:
        """
        Return whether the report contains validation errors.

        :return: bool = `True` when broken, ambiguous, or malformed links exist.

        :example:
            >>> report = GraphReport([], [], [], [], [])
            >>> report.hasErrors()
            False
        """

        return bool(
            self.broken_links
            or self.ambiguous_links
            or self.malformed_links
        )

    def toDict(self) -> dict[str, Any]:
        """
        Convert the report to a JSON-serializable dictionary.

        :return: dict[str, Any] = report data.

        :example:
            >>> report = GraphReport([], [], [], [], [])
            >>> report.toDict()["nodes"]
            []
        """

        return {
            "nodes": self.nodes,
            "edges": self.edges,
            "broken_links": self.broken_links,
            "ambiguous_links": self.ambiguous_links,
            "malformed_links": self.malformed_links,
        }


class WikilinkGraphValidator:
    """
    Validate wikilinks and derive graph data from a Markdown vault.

    The validator scans Markdown files, ignores fenced and inline code,
    resolves Obsidian-style wikilinks, and reports broken, ambiguous, or
    malformed targets.

    :param vault_path: Path = path to the Markdown vault.

    :raises WikilinkValidationError:
        When the vault path does not exist or is not a directory.

    :example:
        >>> validator = WikilinkGraphValidator(Path(".aiassistant"))
        >>> isinstance(validator.validate(), GraphReport)
        True
    """

    def __init__(self, vault_path: Path) -> None:
        self.vault_path: Path = vault_path.resolve()
        if not self.vault_path.exists() or not self.vault_path.is_dir():
            raise WikilinkValidationError(
                self._formatError(
                    f"Vault path does not exist or is not a directory: "
                    f"{self.vault_path}"
                )
            )

    def validate(self) -> GraphReport:
        """
        Validate all Markdown wikilinks in the vault.

        :return: GraphReport = graph data and validation findings.
        """

        markdown_files: list[MarkdownFile] = self._collectMarkdownFiles()
        by_stem: dict[str, list[MarkdownFile]] = self._indexByStem(
            markdown_files
        )
        by_relative_path: dict[str, MarkdownFile] = self._indexByRelativePath(
            markdown_files
        )

        nodes: list[dict[str, str]] = [
            {
                "id": markdown_file.relative_path,
                "label": markdown_file.stem,
                "path": markdown_file.relative_path,
            }
            for markdown_file in markdown_files
        ]

        edges: list[dict[str, str]] = []
        broken_links: list[dict[str, Any]] = []
        ambiguous_links: list[dict[str, Any]] = []
        malformed_links: list[dict[str, Any]] = []

        for markdown_file in markdown_files:
            for wikilink in self._extractWikilinks(markdown_file):
                if self._isMalformedTarget(wikilink.target):
                    malformed_links.append(self._toFinding(wikilink))
                    continue

                matches: list[MarkdownFile] = self._resolveTarget(
                    target=wikilink.target,
                    by_stem=by_stem,
                    by_relative_path=by_relative_path,
                )

                if not matches:
                    broken_links.append(self._toFinding(wikilink))
                    continue

                if len(matches) > 1:
                    finding: dict[str, Any] = self._toFinding(wikilink)
                    finding["matches"] = [
                        match.relative_path for match in matches
                    ]
                    ambiguous_links.append(finding)
                    continue

                edges.append(
                    {
                        "source": wikilink.source,
                        "target": matches[0].relative_path,
                        "label": wikilink.alias or wikilink.target,
                    }
                )

        return GraphReport(
            nodes=nodes,
            edges=edges,
            broken_links=broken_links,
            ambiguous_links=ambiguous_links,
            malformed_links=malformed_links,
        )

    # ============================================================
    # Collection and Indexing
    # ============================================================

    def _collectMarkdownFiles(self) -> list[MarkdownFile]:
        markdown_files: list[MarkdownFile] = []
        for path in sorted(self.vault_path.rglob("*.md")):
            if ".obsidian" in path.parts:
                continue
            relative_path: str = path.relative_to(self.vault_path).as_posix()
            markdown_files.append(
                MarkdownFile(
                    path=path,
                    relative_path=relative_path,
                    stem=path.stem,
                )
            )
        return markdown_files

    def _indexByStem(
        self,
        markdown_files: list[MarkdownFile],
    ) -> dict[str, list[MarkdownFile]]:
        by_stem: dict[str, list[MarkdownFile]] = {}
        for markdown_file in markdown_files:
            by_stem.setdefault(markdown_file.stem, []).append(markdown_file)
        return by_stem

    def _indexByRelativePath(
        self,
        markdown_files: list[MarkdownFile],
    ) -> dict[str, MarkdownFile]:
        by_relative_path: dict[str, MarkdownFile] = {}
        for markdown_file in markdown_files:
            relative_without_suffix: str = markdown_file.relative_path[:-3]
            by_relative_path[relative_without_suffix] = markdown_file
        return by_relative_path

    # ============================================================
    # Parsing
    # ============================================================

    def _extractWikilinks(self, markdown_file: MarkdownFile) -> list[Wikilink]:
        try:
            raw_text: str = markdown_file.path.read_text(encoding="utf-8")
        except OSError as exc:
            raise WikilinkValidationError(
                self._formatError(
                    f"Unable to read Markdown file: {markdown_file.path}"
                )
            ) from exc

        text: str = self._removeCode(raw_text)
        wikilinks: list[Wikilink] = []
        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in WIKILINK_PATTERN.finditer(line):
                raw_target: str = match.group(1).strip()
                target, alias = self._splitAlias(raw_target)
                target = self._stripHeading(target)
                wikilinks.append(
                    Wikilink(
                        source=markdown_file.relative_path,
                        raw=raw_target,
                        target=target,
                        alias=alias,
                        line=line_number,
                    )
                )
        return wikilinks

    def _removeCode(self, text: str) -> str:
        without_fences: str = FENCE_PATTERN.sub("", text)
        return INLINE_CODE_PATTERN.sub("", without_fences)

    def _splitAlias(self, raw_target: str) -> tuple[str, str | None]:
        if "|" not in raw_target:
            return raw_target.strip(), None
        target, alias = raw_target.split("|", 1)
        return target.strip(), alias.strip() or None

    def _stripHeading(self, target: str) -> str:
        return target.split("#", 1)[0].strip()

    # ============================================================
    # Resolution
    # ============================================================

    def _resolveTarget(
        self,
        target: str,
        by_stem: dict[str, list[MarkdownFile]],
        by_relative_path: dict[str, MarkdownFile],
    ) -> list[MarkdownFile]:
        normalized_target: str = target.replace("\\", "/").strip()
        normalized_target = self._stripMarkdownSuffix(normalized_target)

        if "/" in normalized_target:
            match: MarkdownFile | None = by_relative_path.get(
                normalized_target
            )
            return [match] if match else []

        return by_stem.get(normalized_target, [])

    def _stripMarkdownSuffix(self, target: str) -> str:
        if target.endswith(".md"):
            return target[:-3]
        return target

    def _isMalformedTarget(self, target: str) -> bool:
        if not target:
            return True
        if target.startswith("#"):
            return True
        if target.startswith(("http://", "https://")):
            return True
        if target.endswith(".md"):
            return True
        return False

    # ============================================================
    # Output Helpers
    # ============================================================

    def _toFinding(self, wikilink: Wikilink) -> dict[str, Any]:
        return {
            "source": wikilink.source,
            "line": wikilink.line,
            "raw": wikilink.raw,
            "target": wikilink.target,
        }

    def _formatError(self, message: str) -> str:
        caller = inspect.stack()[1]
        method_name = caller.function
        return (
            f"Class: {self.__class__.__name__}\n"
            f"Method: {method_name}\n"
            f"Error: {message}"
        )


def parseArguments(argv: list[str]) -> argparse.Namespace:
    """
    Parse command-line arguments.

    :param argv: list[str] = command-line arguments without executable name.

    :return: argparse.Namespace = parsed arguments.

    :example:
        >>> args = parseArguments(["--vault", ".aiassistant"])
        >>> args.vault
        '.aiassistant'
    """

    parser = argparse.ArgumentParser(
        description="Validate .aiassistant Obsidian wikilinks."
    )
    parser.add_argument(
        "--vault",
        default=".aiassistant",
        help="Path to the Markdown vault. Defaults to .aiassistant.",
    )
    parser.add_argument(
        "--json-output",
        default=None,
        help="Optional path where graph JSON should be written.",
    )
    return parser.parse_args(argv)


def writeJsonReport(report: GraphReport, output_path: Path) -> None:
    """
    Write a graph report as JSON.

    :param report: GraphReport = report to serialize.
    :param output_path: Path = output file path.

    :return: None.

    :raises WikilinkValidationError:
        When the JSON file cannot be written.
    """

    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(
            json.dumps(report.toDict(), indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
    except OSError as exc:
        raise WikilinkValidationError(
            "Class: module\n"
            "Method: writeJsonReport\n"
            f"Error: Unable to write JSON report: {output_path}"
        ) from exc


def printReport(report: GraphReport) -> None:
    """
    Print a concise validation report.

    :param report: GraphReport = report to print.

    :return: None.
    """

    print("Wikilink validation report")
    print(f"Nodes: {len(report.nodes)}")
    print(f"Edges: {len(report.edges)}")
    print(f"Broken links: {len(report.broken_links)}")
    print(f"Ambiguous links: {len(report.ambiguous_links)}")
    print(f"Malformed links: {len(report.malformed_links)}")

    for section_name, findings in (
        ("Broken links", report.broken_links),
        ("Ambiguous links", report.ambiguous_links),
        ("Malformed links", report.malformed_links),
    ):
        if not findings:
            continue
        print(f"\n{section_name}:")
        for finding in findings:
            print(
                f"- {finding['source']}:{finding['line']} -> "
                f"{finding['raw']}"
            )


def main(argv: list[str] | None = None) -> int:
    """
    Execute wikilink validation from the command line.

    :param argv: list[str] | None = optional command-line arguments.

    :return: int = process exit code.
    """

    args = parseArguments(argv or sys.argv[1:])
    try:
        validator = WikilinkGraphValidator(Path(args.vault))
        report = validator.validate()
        printReport(report)
        if args.json_output:
            writeJsonReport(report, Path(args.json_output))
        return 1 if report.hasErrors() else 0
    except WikilinkValidationError as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
