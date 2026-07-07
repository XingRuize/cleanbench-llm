"""Interface that every data corruptor must follow."""

from abc import ABC, abstractmethod
import random
from typing import Any

from cleanbench.domain.models import (
    CellAddress,
    CorruptionRecord,
    CorruptionType,
)

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

    def build_record(self, address: CellAddress, clean_value: Any, corrupted_value: Any, seed: int, metadata: dict[str, Any] | None = None) -> CorruptionRecord:
        """Build a ground-truth record from the clean and corrupted values."""

        if metadata is None:
                metadata = {}

        return CorruptionRecord(
            address=address,
            clean_value=clean_value,
            corrupted_value=corrupted_value,
            corruption_type=self.corruption_type,
            seed=seed,
            metadata=metadata,)
