"""Break aggregate metrics into interpretable failure categories."""

from typing import Any

from cleanbench.domain.models import CleaningProposal, CorruptionRecord


class ErrorAnalyzer:
    """Analyze failures by corruption type, column, and severity."""

    def analyze(
        self,
        proposals: list[CleaningProposal],
        ground_truth: list[CorruptionRecord],
    ) -> dict[str, Any]:
        """Generate a structured failure analysis."""
        pass

    def collect_examples(self, *args: object, **kwargs: object) -> list[dict[str, Any]]:
        """Select representative success and failure examples."""
        pass
