"""Convert experiment results into charts and a Markdown report."""

from pathlib import Path

from cleanbench.domain.models import EvaluationResult


class ReportGenerator:
    """Report method comparisons, costs, and representative failures."""

    def generate(self, results: list[EvaluationResult], output_dir: Path) -> None:
        """Generate all configured report artifacts."""
        pass

    def plot_method_comparison(self, *args: object, **kwargs: object) -> None:
        """Plot core metrics for each cleaning method."""
        pass

    def write_markdown_report(self, *args: object, **kwargs: object) -> None:
        """Write a research report containing conclusions and limitations."""
        pass
