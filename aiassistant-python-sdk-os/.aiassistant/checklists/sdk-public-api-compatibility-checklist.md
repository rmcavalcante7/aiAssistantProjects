# SDK Public API Compatibility Checklist

## Objective

Validate that public API changes are intentional, tested, documented, and
versioned appropriately.

## Public Surface Inventory

- [ ] Top-level package exports were reviewed.
- [ ] Public facade/client classes were reviewed.
- [ ] Public domain namespaces were reviewed.
- [ ] Public method/function names and signatures were reviewed.
- [ ] Public configuration objects were reviewed.
- [ ] Public models and result objects were reviewed.
- [ ] Public exception types and error semantics were reviewed.
- [ ] README examples were reviewed.
- [ ] Sphinx/docs examples were reviewed.

## Compatibility

- [ ] Change is classified as additive, behavior-preserving, deprecation, or
      breaking.
- [ ] Existing public imports still work unless breaking change is approved.
- [ ] Existing method signatures still work unless breaking change is approved.
- [ ] Existing documented behavior still works unless breaking change is
      approved.
- [ ] Deprecations include migration guidance.
- [ ] Breaking changes include versioning impact and explicit approval.

## Tests

- [ ] Functional tests cover the public path.
- [ ] Tests cover backward-compatible behavior.
- [ ] Tests cover new public behavior.
- [ ] Exception behavior is tested when public.
- [ ] Integration tests cover provider behavior when needed.

## Documentation

- [ ] README was updated.
- [ ] API docs were updated.
- [ ] Examples were updated.
- [ ] Changelog/release notes mention public impact.
- [ ] Migration guidance exists when users must change code.

## Related Files

- [[0003-sdk-public-api-compatibility-policy]]
- [[python-sdk-implementation-prompt]]

