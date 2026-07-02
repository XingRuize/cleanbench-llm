"""Structured LLM-based data cleaner."""

from typing import Any
import pandas as pd

from cleanbench.cleaners.base import Cleaner
from cleanbench.domain.models import CleaningProposal


class LLMClient:
    """Isolate cleaner logic from a specific model provider."""

    def complete_json(self, messages: list[dict[str, str]]) -> dict[str, Any]:
        """Send a request and return a JSON object."""
        pass


class LLMCleaner(Cleaner):
    """Send candidate cells to an LLM and parse structured proposals."""

    name = "llm"

    def __init__(self, client: LLMClient) -> None:
        """Inject an LLM client so tests can substitute a fake client."""
        pass

    def propose(self, frame: pd.DataFrame, id_column: str) -> list[CleaningProposal]:
        """Build requests, call the model, and return cleaning proposals."""
        pass

    def build_prompt(self, *args: object, **kwargs: object) -> list[dict[str, str]]:
        """Build a constrained prompt for structured cleaning."""
        pass

    def parse_response(self, response: dict[str, Any]) -> list[CleaningProposal]:
        """Convert model JSON into domain objects."""
        pass
