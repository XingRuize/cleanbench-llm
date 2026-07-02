"""Repository for CSV-based benchmark datasets."""

from pathlib import Path
import pandas as pd

from cleanbench.domain.models import CorruptionRecord


class DatasetRepository:
    """Manage clean data, dirty data, and corruption ground truth."""

    def load_clean(self, path: Path) -> pd.DataFrame:
        """Load a clean CSV dataset."""
        pass

    def save_generated(
        self,
        dirty_frame: pd.DataFrame,
        records: list[CorruptionRecord],
        output_dir: Path,
    ) -> None:
        """Save a dirty dataset and its corruption ground truth."""
        pass

    def load_ground_truth(self, path: Path) -> list[CorruptionRecord]:
        """Load corruption ground-truth records."""
        pass
