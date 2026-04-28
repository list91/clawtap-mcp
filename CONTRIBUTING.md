# Contributing to ClawTap

Thanks for taking the time! This project is small, so the rules are simple.

## Bugs

Open an issue with:

- What you did (exact `type_text` / `press_key` / `combo_keys` call or MCP invocation).
- What happened (error message, wrong output, timeout).
- What you expected.
- OS + Python version + how you installed the package (`uvx`, `pip`, source).

Stack traces are worth a thousand words. Logs from `logger = logging.getLogger("clawtap")` are very welcome.

## Pull requests

1. Open an issue first for anything bigger than a typo.
2. Fork, branch off `main`, keep the diff focused on one thing.
3. Add or update tests under `tests/` — CI runs `pytest -q` on Python 3.10, 3.11, 3.12.
4. Run the test suite locally before pushing:

   ```bash
   pip install -e .
   pip install pytest
   pytest -q
   ```

5. Squash trivial fixup commits before review.

## Coding style

- Type hints encouraged on new public functions.
- Keep tool docstrings short — they ship into MCP clients verbatim.
- No new top-level dependencies without a reason.

## Adding scancode mappings

If you extend `CYRILLIC_TO_SCANCODE` or add a new layout, add a parametrised
case to `tests/test_scancode_map.py` for at least two characters per row.

## Releases

Releases follow [semver](https://semver.org/). Bump the version in
`pyproject.toml`, update `CHANGELOG.md`, tag `vX.Y.Z`.
