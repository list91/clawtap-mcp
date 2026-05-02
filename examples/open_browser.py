"""Open a URL in the target's default browser by emulating Win+R.

Sequence:
  1. Win+R                            → Run dialog appears.
  2. Type the URL.
  3. Enter                            → browser launches.

Works on Windows targets. macOS / Linux equivalents are left as an exercise.
"""

from __future__ import annotations

import time

from clawtap_mcp import ALL_KEYS, SPECIAL_KEYS, ble, text_to_scancodes


URL = "https://example.com"


def combo(keys: list[str]) -> None:
    key_bytes = [ALL_KEYS[k] for k in keys]
    ble.send(bytes([0x01, len(key_bytes)] + key_bytes))


def press(key: str) -> None:
    ble.send(bytes([SPECIAL_KEYS[key]]))


def main() -> None:
    combo(["win", "r"])
    time.sleep(0.4)
    ble.send(text_to_scancodes(URL))
    time.sleep(0.1)
    press("enter")
    print(f"Asked target to open {URL}")


if __name__ == "__main__":
    main()
