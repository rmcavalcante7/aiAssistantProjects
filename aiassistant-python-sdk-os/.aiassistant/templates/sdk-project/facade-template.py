"""Public SDK facade.

This file is a starter template. Rename classes and methods to match the real
SDK domain before publishing.
"""

from __future__ import annotations


class Client:
    """Main public SDK client.

    :param api_key: API credential used by the SDK.
    :param base_url: Optional API base URL.

    :example:
        >>> client = Client(api_key="token")
        >>> isinstance(client, Client)
        True
    """

    def __init__(self, api_key: str, base_url: str | None = None) -> None:
        self.api_key = api_key
        self.base_url = base_url

