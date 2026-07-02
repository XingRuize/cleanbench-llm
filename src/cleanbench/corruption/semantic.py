"""Corruptors for errors that require semantic interpretation."""

import random
from typing import Any

from cleanbench.corruption.base import Corruptor
from cleanbench.domain.models import CorruptionType


class TypoCorruptor(Corruptor):
    """Create typos by deleting, swapping, or replacing characters."""

    corruption_type = CorruptionType.TYPO

    def can_apply(self, value: Any) -> bool:
        """Return whether the text is long enough for a meaningful typo."""
        pass

    def corrupt(self, value: Any, rng: random.Random) -> Any:
        """Generate a reproducible character-level error."""
        pass


class CategoryCorruptor(Corruptor):
    """Replace a canonical category with an alias or inconsistent form."""

    corruption_type = CorruptionType.CATEGORY

    def can_apply(self, value: Any) -> bool:
        """Return whether the value exists in the configured category map."""
        pass

    def corrupt(self, value: Any, rng: random.Random) -> Any:
        """Select a reproducible non-canonical category form."""
        pass
