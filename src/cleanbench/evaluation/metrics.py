"""Metrics for measuring data-cleaning quality."""

from cleanbench.domain.models import CleaningProposal, CorruptionRecord, EvaluationResult


class CleaningEvaluator:
    """Compare cleaning proposals with corruption ground truth."""

    def evaluate(
        self,
        cleaner_name: str,
        proposals: list[CleaningProposal],
        ground_truth: list[CorruptionRecord],
    ) -> EvaluationResult:
        """Compute all configured evaluation metrics."""
        pass

    def repair_precision(self, *args: object, **kwargs: object) -> float:
        """Return the proportion of proposed modifications that are correct."""
        pass

    def repair_recall(self, *args: object, **kwargs: object) -> float:
        """Return the proportion of true corruptions that were repaired."""
        pass

    def overcorrection_rate(self, *args: object, **kwargs: object) -> float:
        """Return the rate at which clean cells were incorrectly modified."""
        pass

    def abstention_accuracy(self, *args: object, **kwargs: object) -> float:
        """Return the accuracy of abstentions on uncertain cases."""
        pass
