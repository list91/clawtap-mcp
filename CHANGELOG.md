# Changelog

All notable changes to `clawtap-mcp` are listed here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this
project adheres to [Semantic Versioning](https://semver.org/).

## [1.1.0] — 2026-05-11

### Added
- pytest suite covering the Cyrillic ↔ US-QWERTY scancode map and the
  modifier-alias tables.
- GitHub Actions workflow `tests.yml` running on Python 3.10, 3.11, 3.12.
- `CONTRIBUTING.md` plus issue forms for bug reports and feature requests.
- `examples/` folder with five standalone scripts demonstrating clipboard
  send, Cyrillic input, `Win+R` browser launch, a vim session, and a
  throughput stress test.
- FAQ section in the README answering the top recurring questions.

### Changed
- Tightened `pyproject.toml` description and dropped trailing whitespace.

## [1.0.0] — 2026-04-08

### Added
- Logo + README redesign.

### Changed
- Polished the BLE device identifier and discovery flow.

## [0.2.0] — 2026-04-06

### Added
- Cyrillic input via ЙЦУКЕН → US-QWERTY scancode mapping. The target
  computer must have a Russian keyboard layout active for the characters
  to land correctly.

## [0.1.1] — 2026-04-06

### Changed
- Internal tool docstrings compacted by ~40%; added an explicit warning
  about non-ASCII inputs to prevent LLM hallucination of Cyrillic/emoji.

## [0.1.0] — 2026-04-06

### Added
- Initial public release.
- MCP server exposing `type_text`, `press_key`, `combo_keys`, and
  `health_check`.
- BLE-to-USB HID bridge using `bleak` in a dedicated thread to avoid
  asyncio conflicts with MCP / anyio.
- Packaging via `pyproject.toml` + `hatchling`, installable through
  `uvx clawtap-mcp`.

[1.1.0]: https://github.com/list91/clawtap-mcp/releases/tag/v1.1.0
[1.0.0]: https://github.com/list91/clawtap-mcp/releases/tag/v1.0.0
[0.2.0]: https://github.com/list91/clawtap-mcp/releases/tag/v0.2.0
[0.1.1]: https://github.com/list91/clawtap-mcp/releases/tag/v0.1.1
[0.1.0]: https://github.com/list91/clawtap-mcp/releases/tag/v0.1.0
