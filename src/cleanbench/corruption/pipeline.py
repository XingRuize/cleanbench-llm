"""Schedule controlled corruptions across a complete DataFrame."""

from collections.abc import Sequence
from dataclasses import dataclass
import math

import pandas as pd
import random

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
        if not 0 <= corruption_rate <= 1:
            raise ValueError("corruption_rate must be between 0 and 1.")

        dirty_frame = clean_frame.copy(deep=True)
        records: list[CorruptionRecord] = []

        if corruption_rate == 0:
            return dirty_frame, records

        candidates = self.select_candidates(
            clean_frame=clean_frame,
            id_column=id_column,
            protected_columns=protected_columns,
        )

        candidate_groups: dict[
            tuple[int, str],
            list[CorruptionCandidate],
        ] = {}

        for candidate in candidates:
            cell_key = (
                candidate.row_position,
                candidate.column,
            )

            candidate_groups.setdefault(cell_key, []).append(candidate)

        if not candidate_groups:
            return dirty_frame, records

        raw_target_count = len(candidate_groups) * corruption_rate

        target_count = math.ceil(raw_target_count)

        rng = random.Random(seed)

        cell_keys = list(candidate_groups.keys())

        selected_cell_keys = rng.sample(
            cell_keys,
            k=target_count,
        )

        raise NotImplementedError("Random candidate selection is not implemented yet.")

    def select_candidates(
        self,
        clean_frame: pd.DataFrame,
        id_column: str,
        protected_columns: set[str],
    ) -> list[CorruptionCandidate]:
        """Select candidate cells that are eligible for corruption."""
        excluded_columns = protected_columns | {id_column}
        candidates: list[CorruptionCandidate] = []
        for row_position, (_, row) in enumerate(clean_frame.iterrows()):
            for column in clean_frame.columns:
                if column in excluded_columns:
                    continue

                value = row[column]

                for corruptor in self.corruptors:
                    if corruptor.can_apply(value):
                        candidate = CorruptionCandidate(
                            row_position=row_position,
                            column=column,
                            corruptor=corruptor,
                        )
                        candidates.append(candidate)

        return candidates
