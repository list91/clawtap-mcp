"""Type a Cyrillic sentence on the target.

The target computer MUST have a Russian keyboard layout active — ClawTap
sends US-QWERTY scancodes that the OS then re-interprets as the Cyrillic
letters under the active layout. Switch layouts with `Win+Space` (Windows)
or your equivalent before running.
"""

from clawtap_mcp import ble, text_to_scancodes


PHRASE = "Привет, мир! Это ClawTap, печатает по Bluetooth.\n"


def main() -> None:
    data = text_to_scancodes(PHRASE)
    if not ble.send(data):
        raise SystemExit("BLE send failed.")
    print(f"Sent {len(data)} bytes ({len(PHRASE)} characters).")


if __name__ == "__main__":
    main()
