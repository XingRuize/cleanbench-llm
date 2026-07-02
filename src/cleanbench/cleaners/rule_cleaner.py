"""Rule-based cleaning baseline."""

import pandas as pd

from cleanbench.cleaners.base import Cleaner
from cleanbench.domain.models import CleaningProposal


class RuleCleaner(Cleaner):
    """Use deterministic rules for formatting and known categories."""

    name = "rules"

    def propose(self, frame: pd.DataFrame, id_column: str) -> list[CleaningProposal]:
        """Inspect allowed columns and generate rule-based proposals."""
        pass

    def normalize_whitespace(self, value: object) -> object:
        """Normalize whitespace in a value."""
        pass

    def normalize_case(self, value: object) -> object:
        """Normalize capitalization according to a column policy."""
        pass

    def normalize_date(self, value: object) -> object:
        """Convert a date value into the canonical format."""
        pass
