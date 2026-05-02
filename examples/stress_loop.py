"""Stress the BLE link with a long blob of text and report the health afterwards.

Useful when bringing up a new target host: any chunking / pacing / MTU issues
show up as missing or duplicated characters once you compare the output on
the target against the input below.
"""

from __future__ import annotations

import string
import time

from clawtap_mcp import ble, text_to_scancodes


def main() -> None:
    payload = (string.ascii_letters + string.digits) * 20  # ~1240 chars
    payload += "\n"

    started = time.perf_counter()
    ok = ble.send(text_to_scancodes(payload))
    elapsed = time.perf_counter() - started

    if not ok:
        raise SystemExit("Send failed.")

    cps = len(payload) / elapsed
    print(f"Sent {len(payload)} chars in {elapsed:.2f}s ({cps:.0f} chars/s)")

    # Re-check the link.
    print(f"is_connected={ble.is_connected}")


if __name__ == "__main__":
    main()
