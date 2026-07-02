"""Interface that every data corruptor must follow."""

from abc import ABC, abstractmethod
import random
from typing import Any

from cleanbench.domain.models import CorruptionRecord, CorruptionType


class Corruptor(ABC):
    """Abstract base class for cell-level data corruptors."""

    corruption_type: CorruptionType

    @abstractmethod
    def can_apply(self, value: Any) -> bool:
        """Return whether this corruption can be applied to the value."""
        pass

    @abstractmethod
    def corrupt(self, value: Any, rng: random.Random) -> Any:
        """Corrupt a value using the provided random-number generator."""
        pass

    def build_record(self, *args: Any, **kwargs: Any) -> CorruptionRecord:
        """Build a ground-truth record from the clean and corrupted values."""
        pass
