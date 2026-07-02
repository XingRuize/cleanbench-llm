"""Corruptors for deterministic formatting errors."""

import random
from datetime import date
from typing import Any

from cleanbench.corruption.base import Corruptor
from cleanbench.domain.models import CorruptionType


class WhitespaceCorruptor(Corruptor):
    """Add unwanted leading, trailing, or repeated whitespace."""

    corruption_type = CorruptionType.WHITESPACE

    def can_apply(self, value: Any) -> bool:
        """Return whether the value is a non-empty string after trimming."""
        if not isinstance(value, str):
            return False

        value = value.strip()
        return bool(value)

    def corrupt(self, value: Any, rng: random.Random) -> Any:
        """Apply one reproducible whitespace corruption strategy."""
        strategy = rng.choice([1, 2, 3])
        if strategy == 1:
            return " " + value
        if strategy == 2:
            return value + " "
        return " " + value + " "


class CaseCorruptor(Corruptor):
    """Change the capitalization of alphabetic text."""

    corruption_type = CorruptionType.CASE

    def can_apply(self, value: Any) -> bool:
        """Return whether the value contains alphabetic characters."""

        if not isinstance(value, str):
            return False

        for character in value:
            if character.isalpha():
                return True

        return False

    def corrupt(self, value: Any, rng: random.Random) -> Any:
        """Convert the value to a reproducible alternative case form."""

        if not self.can_apply(value):
            raise ValueError("Case corruption requires a string containing letters.")

        valid_candidates = []
        candidates = [
            value.upper(),
            value.lower(),
            value.swapcase(),
        ]

        for candidate in candidates:
            if candidate != value:
                valid_candidates.append(candidate)

        return rng.choice(valid_candidates)


class DateFormatCorruptor(Corruptor):
    """Convert a normalized date into another valid but inconsistent format."""

    corruption_type = CorruptionType.DATE_FORMAT

    def can_apply(self, value: Any) -> bool:
        """Return whether the value can be interpreted as a date."""
        if not isinstance(value, str):
            return False

        try:
            date.fromisoformat(value)
        except ValueError:
            return False

        return True

    def corrupt(self, value: Any, rng: random.Random) -> Any:
        """Render the date using a reproducibly selected alternative format."""
        if not self.can_apply(value):
            raise ValueError("Date-format corruption requires a valid ISO date.")

        parsed_date = date.fromisoformat(value)
        formats = [
            "%m/%d/%Y",
            "%d/%m/%Y",
            "%Y.%m.%d",
        ]

        selected_format = rng.choice(formats)
        return parsed_date.strftime(selected_format)
