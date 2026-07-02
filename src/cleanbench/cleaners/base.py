"""Common interface for all data cleaners."""

from abc import ABC, abstractmethod
import pandas as pd

from cleanbench.domain.models import CleaningProposal


class Cleaner(ABC):
    """Accept a dirty table and return cleaning proposals."""

    name: str

    @abstractmethod
    def propose(self, frame: pd.DataFrame, id_column: str) -> list[CleaningProposal]:
        """Generate modify, keep, or abstain proposals."""
        pass
