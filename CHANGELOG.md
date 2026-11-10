# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed
- Blank cells are treated as blank: blank required cells are errors, blank optional cells raise nothing.
- Non-numeric cells such as `n/a` are reported instead of being dropped silently.
- Quick-start installs the package.

### Removed
- Unused `IntegrityRecord` schema and the `pydantic` dependency.

## [0.1.0] - 2026-02-05

### Added
- Add files via upload

### Other
- Create pyproject.toml
- Update ci.yml
- Create ci.yml
- Update README.md
- Update README.md
- Initial commit

[0.1.0]: https://github.com/felipearocha/integrity-data-foundation/releases/tag/v0.1.0
