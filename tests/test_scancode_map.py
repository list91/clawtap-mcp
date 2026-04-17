"""Tests for the Cyrillic→US-QWERTY scancode mapping."""

import string

import pytest

from clawtap_mcp import (
    ALL_KEYS,
    CYRILLIC_TO_SCANCODE,
    MODIFIER_KEYS,
    SPECIAL_KEYS,
    text_to_scancodes,
)


def test_ascii_round_trip():
    """All printable ASCII should map to itself."""
    sample = string.ascii_letters + string.digits + " !@#$%^&*()"
    out = text_to_scancodes(sample)
    assert out == sample.encode("ascii")


def test_empty_input():
    assert text_to_scancodes("") == b""


def test_unsupported_chars_dropped():
    """Non-mapped characters should be silently skipped."""
    out = text_to_scancodes("hello☃world")
    assert out == b"helloworld"


def test_cyrillic_lowercase_full_alphabet():
    """Every lowercase letter of the Russian alphabet must have a mapping."""
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    for ch in alphabet:
        assert ch in CYRILLIC_TO_SCANCODE, f"missing mapping for {ch!r}"


def test_cyrillic_uppercase_full_alphabet():
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    for ch in alphabet:
        assert ch in CYRILLIC_TO_SCANCODE, f"missing mapping for {ch!r}"


@pytest.mark.parametrize(
    ("cyr", "expected"),
    [
        ("й", "q"),
        ("ц", "w"),
        ("у", "e"),
        ("ф", "a"),
        ("я", "z"),
        ("Й", "Q"),
        ("Ф", "A"),
        ("Я", "Z"),
    ],
)
def test_cyrillic_known_mappings(cyr: str, expected: str):
    out = text_to_scancodes(cyr)
    assert out == expected.encode("ascii")


def test_mixed_ascii_cyrillic():
    out = text_to_scancodes("hi привет")
    assert out == b"hi ghbdtn"


def test_special_keys_unique_codes():
    """No two distinct special keys should share a scancode (aliases excluded)."""
    canonical = {
        "enter", "escape", "backspace", "tab", "space",
        "insert", "delete", "home", "end",
        "pageup", "pagedown", "up", "down", "left", "right",
        "f1", "f2", "f3", "f4", "f5", "f6",
        "f7", "f8", "f9", "f10", "f11", "f12",
    }
    seen = {}
    for name in canonical:
        code = SPECIAL_KEYS[name]
        assert code not in seen, f"duplicate code 0x{code:02X}: {name} vs {seen[code]}"
        seen[code] = name


def test_modifier_aliases_consistent():
    """`win`, `gui`, `cmd`, `super`, `meta` must all alias to the same code."""
    aliases = ("win", "gui", "cmd", "super", "meta", "lgui")
    code = MODIFIER_KEYS["win"]
    for alias in aliases:
        assert MODIFIER_KEYS[alias] == code


def test_all_keys_merge():
    assert set(ALL_KEYS) == set(SPECIAL_KEYS) | set(MODIFIER_KEYS)
