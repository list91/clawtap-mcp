<div align="center">

<img src="logo.png" alt="ClawTap" width="180">

# ClawTap

**Wireless keyboard bridge — type on any computer from your phone or AI assistant**

[![PyPI](https://img.shields.io/pypi/v/clawtap-mcp?color=orange&label=PyPI)](https://pypi.org/project/clawtap-mcp/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

</div>

---

A tiny USB stick that receives text over Bluetooth and types it as a real USB keyboard. Works with Claude, any MCP-compatible AI, or any BLE app on your phone.

```
Phone / AI  →  BLE  →  ClawTap  →  USB HID  →  💻
```

## Quick Start

```bash
claude mcp add clawtap -- uvx clawtap-mcp
```

Or install manually:

```bash
pip install clawtap-mcp
```

## MCP Tools

| Tool | What it does |
|------|-------------|
| `type_text(text)` | Type text as keystrokes. Supports ASCII + Cyrillic |
| `press_key(key, count)` | Press a special key: `enter`, `escape`, `backspace`, `f1`–`f12`, arrows |
| `combo_keys(keys)` | Key combo up to 5 keys: `["ctrl","c"]`, `["alt","tab"]`, `["win","r"]` |
| `health_check()` | Check wireless connection and device status |

### Examples

```python
# Type text
type_text("Hello World!\n")

# Cyrillic (target must have RU layout active)
type_text("Привет мир")

# Key combos
combo_keys(["ctrl", "c"])      # Copy
combo_keys(["alt", "tab"])     # Switch window
combo_keys(["win", "r"])       # Run dialog

# Special keys
press_key("backspace", 5)      # Delete 5 chars
press_key("enter")
```

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Device not found | Power cycle device. Make sure no other app is connected to it |
| Wrong characters | Check keyboard layout on target computer (EN for English, RU for Cyrillic) |
| Disconnects | Stay within 10m. Check USB power stability |

## License

MIT

---

