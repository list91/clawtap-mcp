# ClawTap MCP

BLE-to-USB HID keyboard bridge exposed as an [MCP](https://modelcontextprotocol.io/) server.

**Send keystrokes to any computer via Bluetooth** — let AI assistants type on your machine through a hardware bridge.

## Architecture

```
Phone / AI  →  BLE  →  ClawTap  →  USB HID  →  💻
```

## Prerequisites

- **Bluetooth adapter** on the host machine (built-in or USB dongle)
- **Python 3.10+**
- **Hardware** (see below)

## Install MCP Server

```bash
# Claude Code / Claude Desktop
claude mcp add clawtap -- uvx clawtap-mcp

# Or manually
pip install clawtap-mcp
```

## MCP Tools

| Tool | Description |
|------|-------------|
| `type_text` | Type ASCII text as HID keystrokes |
| `press_key` | Press a special key (enter, escape, f1-f12, arrows, etc.) |
| `combo_keys` | Press a key combination up to 5 keys (ctrl+c, alt+tab, win+r) |
| `health_check` | Check BLE connection status and device availability |

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ClawTap not found` | Ensure device is powered and not connected to another BLE client. Press RESET on device. |
| Text appears as wrong characters | Switch keyboard layout on target computer (e.g. EN for English text) |
| BLE disconnects frequently | Keep device within 10m range. Check power supply stability. |

## License

MIT
