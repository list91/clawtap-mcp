"""Type whatever is currently in the OS clipboard on the target computer.

Requires `pyperclip` on the *host* side (the machine running the MCP server),
not on the target. Run as a stand-alone script — it imports the public
helpers from clawtap_mcp directly.
"""

from __future__ import annotations

import sys

import pyperclip

from clawtap_mcp import ble, text_to_scancodes


def main() -> int:
    text = pyperclip.paste()
    if not text:
        print("Clipboard is empty.", file=sys.stderr)
        return 1

    data = text_to_scancodes(text)
    if not data:
        print("Clipboard text has no supported characters.", file=sys.stderr)
        return 1

    if not ble.send(data):
        print("Failed to send — is the device powered and in range?", file=sys.stderr)
        return 2

    print(f"Typed {len(data)} characters from clipboard.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
