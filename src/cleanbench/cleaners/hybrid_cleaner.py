"""Hybrid cleaner that applies rules before using an LLM."""

import pandas as pd

from cleanbench.cleaners.base import Cleaner
from cleanbench.domain.models import CleaningProposal


class HybridCleaner(Cleaner):
    """Combine two cleaners and resolve conflicting proposals."""

    name = "hybrid"

    def __init__(self, rule_cleaner: Cleaner, llm_cleaner: Cleaner) -> None:
        """Store the rule-based and LLM-based cleaners."""
        pass

    def propose(self, frame: pd.DataFrame, id_column: str) -> list[CleaningProposal]:
        """Run rules first and send unresolved candidates to the LLM."""
        pass

    def resolve_conflicts(self, *args: object, **kwargs: object) -> list[CleaningProposal]:
        """Choose a proposal when both cleaners target the same cell."""
        pass
