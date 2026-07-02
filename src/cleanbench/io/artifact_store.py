"""Persist experiment configuration, model responses, metrics, and logs."""

from pathlib import Path
from typing import Any


class ArtifactStore:
    """Ensure every experiment has complete, traceable artifacts."""

    def initialize_run(self, output_dir: Path) -> None:
        """Create the directory structure for an experiment run."""
        pass

    def save_json(self, name: str, payload: Any) -> None:
        """Save a JSON artifact."""
        pass

    def save_text(self, name: str, content: str) -> None:
        """Save text content such as prompts or logs."""
        pass
