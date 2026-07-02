"""End-to-end experiment runner."""

from cleanbench.config import ExperimentConfig
from cleanbench.domain.models import EvaluationResult


class ExperimentRunner:
    """Connect data, corruption, cleaning, validation, evaluation, and reporting."""

    def run(self, config: ExperimentConfig) -> list[EvaluationResult]:
        """Execute one complete experiment."""
        pass

    def build_corruption_pipeline(self, config: ExperimentConfig) -> object:
        """Create a corruption pipeline from experiment configuration."""
        pass

    def build_cleaners(self, config: ExperimentConfig) -> list[object]:
        """Create experimental cleaning baselines from configuration."""
        pass

    def apply_validated_proposals(self, *args: object, **kwargs: object) -> object:
        """Apply only cleaning proposals that pass validation."""
        pass
