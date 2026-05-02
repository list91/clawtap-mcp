"""Demonstrate a non-trivial flow: open Vim, write text, save, quit.

Assumes the target already has a terminal in focus with `vim demo.txt`
ready to be invoked. The script just drives the keystrokes.
"""

from __future__ import annotations

import time

from clawtap_mcp import SPECIAL_KEYS, ble, text_to_scancodes


def type_text(text: str) -> None:
    ble.send(text_to_scancodes(text))


def press(key: str, count: int = 1) -> None:
    ble.send(bytes([SPECIAL_KEYS[key]] * count))


def main() -> None:
    # Launch vim on the target.
    type_text("vim demo.txt\n")
    time.sleep(0.6)

    # Enter insert mode, write a few lines, return to normal mode.
    type_text("ihello from ClawTap\nthis was typed over BLE\n")
    press("escape")
    time.sleep(0.2)

    # Save and quit.
    type_text(":wq\n")
    print("Wrote demo.txt on the target.")


if __name__ == "__main__":
    main()
