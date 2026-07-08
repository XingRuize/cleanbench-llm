"""Tests for formatting-related corruptors."""

import pytest
import random

from cleanbench.corruption.formatting import (
    CaseCorruptor,
    DateFormatCorruptor,
    WhitespaceCorruptor,
)


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("Alice", True),
        ("  Alice  ", True),
        ("", False),
        ("   ", False),
        (None, False),
        (123, False),
    ],
)
def test_whitespace_can_apply(value, expected):
    """Verify which values support whitespace corruption."""
    corruptor = WhitespaceCorruptor()
    actual = corruptor.can_apply(value)
    assert actual is expected


def test_whitespace_corrupt_adds_only_surrounding_whitespace():
    """Verify that corruption adds whitespace without changing the content."""
    # Arrange: prepare the object, input, and random generator.
    corruptor = WhitespaceCorruptor()
    original = "Alice"
    rng = random.Random(42)

    # Act: run the method being tested.
    result = corruptor.corrupt(original, rng)

    # Assert: verify the observable behavior.
    assert result != original
    assert result.strip() == original


def test_whitespace_corrupt_is_reproducible():
    """Verify that the same seed produces the same corruption."""
    whitespace_corruptor = WhitespaceCorruptor()

    first_rng = random.Random(42)
    second_rng = random.Random(42)

    first_result = whitespace_corruptor.corrupt("Alice", first_rng)
    second_result = whitespace_corruptor.corrupt("Alice", second_rng)

    assert first_result == second_result


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("Alice", True),
        ("A123", True),
        ("123", False),
        ("---", False),
        ("", False),
        (None, False),
        (123, False),
    ],
)
def test_case_can_apply(value, expected):
    """Verify which values support case corruption."""
    case_corruptor = CaseCorruptor()

    actual = case_corruptor.can_apply(value)

    assert actual is expected


def test_case_corrupt_changes_only_character_case():
    """Verify that corruption changes case without changing the text."""
    case_corruptor = CaseCorruptor()
    original = "Alice"
    rng = random.Random(42)

    result = case_corruptor.corrupt(original, rng)

    assert result != original
    assert result.lower() == original.lower()


def test_case_corrupt_is_reproducible():
    """Verify that the same seed produces the same case corruption."""
    case_corruptor = CaseCorruptor()

    first_result = case_corruptor.corrupt("Alice", random.Random(42))
    second_result = case_corruptor.corrupt("Alice", random.Random(42))

    assert first_result == second_result


def test_case_corrupt_rejects_invalid_value():
    """Verify that unsupported values raise a clear error."""
    case_corruptor = CaseCorruptor()
    rng = random.Random(42)

    with pytest.raises(ValueError):
        case_corruptor.corrupt(123, rng)


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("2026-07-02", True),
        ("2024-02-29", True),
        ("2026-02-29", False),
        ("07/02/2026", False),
        ("hello", False),
        ("", False),
        (None, False),
        (20260702, False),
    ],
)
def test_date_format_can_apply(value, expected):
    """Verify which values support date-format corruption."""
    date_corruptor = DateFormatCorruptor()

    actual = date_corruptor.can_apply(value)

    assert actual is expected


def test_date_format_corrupt_uses_supported_format():
    """Verify that a date is rendered in one supported alternative format."""
    date_corruptor = DateFormatCorruptor()
    rng = random.Random(42)

    result = date_corruptor.corrupt("2026-07-02", rng)

    expected_results = {
        "07/02/2026",
        "02/07/2026",
        "2026.07.02",
    }

    assert result in expected_results
    assert result != "2026-07-02"


def test_date_format_corrupt_is_reproducible():
    """Verify that the same seed produces the same date format."""
    date_corruptor = DateFormatCorruptor()

    first_result = date_corruptor.corrupt("2026-07-02", random.Random(42))
    second_result = date_corruptor.corrupt("2026-07-02", random.Random(42))

    assert first_result == second_result


def test_date_format_corrupt_rejects_invalid_value():
    """Verify that invalid dates raise a clear error."""
    date_corruptor = DateFormatCorruptor()

    with pytest.raises(ValueError):
        date_corruptor.corrupt("not-a-date", random.Random(42))
