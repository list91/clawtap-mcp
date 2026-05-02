# Examples

These are minimal, copy-paste-friendly demos of what ClawTap is good at when
driven from a Python script (instead of through an MCP client). Each script
talks to the running MCP server over its standard transport — drop them into
any Claude/MCP host that already loads `clawtap-mcp`.

| File | What it shows |
|------|---------------|
| [`type_clipboard.py`](type_clipboard.py) | Pull text from the OS clipboard and type it on the target. |
| [`cyrillic_demo.py`](cyrillic_demo.py) | Send a Russian phrase; expects RU layout active on the target. |
| [`open_browser.py`](open_browser.py) | `Win+R` → type a URL → `Enter`. Useful for kiosk-style automation. |
| [`vim_session.py`](vim_session.py) | Drop into a Vim file, write a few lines, save, quit — all over BLE. |
| [`stress_loop.py`](stress_loop.py) | Hammer the link with 1000 characters and report `health_check()` afterwards. |
