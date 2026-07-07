"""Schedule controlled corruptions across a complete DataFrame."""

from collections.abc import Sequence
from dataclasses import dataclass

import pandas as pd

from cleanbench.corruption.base import Corruptor
from cleanbench.domain.models import CorruptionRecord


@dataclass(frozen=True)
class CorruptionCandidate:
    """Represent one applicable corruptor for one table cell."""

    row_position: int
    column: str
    corruptor: Corruptor


class CorruptionPipeline:
    """Select cells, apply corruptions, and produce ground truth."""

    def __init__(self, corruptors: Sequence[Corruptor]) -> None:
        """Store the available corruptors."""
        self.corruptors = tuple(corruptors)

    def run(
        self,
        clean_frame: pd.DataFrame,
        id_column: str,
        protected_columns: set[str],
        corruption_rate: float,
        seed: int,
    ) -> tuple[pd.DataFrame, list[CorruptionRecord]]:
        """Return a dirty DataFrame copy and its ground-truth records."""
        pass

    def select_candidates(
        self,
        clean_frame: pd.DataFrame,
        id_column: str,
        protected_columns: set[str],
    ) -> list[CorruptionCandidate]:
        """Select candidate cells that are eligible for corruption."""
        pass