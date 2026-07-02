"""Data objects shared across CleanBench modules."""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class CorruptionType(str, Enum):
    """Corruption types planned for the first project phase."""

    WHITESPACE = "whitespace"
    CASE = "case"
    DATE_FORMAT = "date_format"
    NUMBER_FORMAT = "number_format"
    TYPO = "typo"
    CATEGORY = "category"
    MISSING = "missing"
    CROSS_FIELD = "cross_field"


class CleaningAction(str, Enum):
    """Actions that a cleaner may propose."""

    MODIFY = "modify"
    ABSTAIN = "abstain"
    KEEP = "keep"


@dataclass(frozen=True)
class CellAddress:
    """Uniquely identify one cell in a table."""

    row_id: str
    column: str


@dataclass(frozen=True)
class CorruptionRecord:
    """Ground-truth record for one synthetic corruption."""

    address: CellAddress
    clean_value: Any
    corrupted_value: Any
    corruption_type: CorruptionType
    seed: int
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class CleaningProposal:
    """A cleaner's modification, keep, or abstention proposal for one cell."""

    address: CellAddress
    original_value: Any
    proposed_value: Any
    action: CleaningAction
    confidence: float
    reason: str
    cleaner_name: str


@dataclass(frozen=True)
class ValidationResult:
    """Constraint-validation result for one cleaning proposal."""

    accepted: bool
    errors: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class EvaluationResult:
    """Metric collection produced by one experimental run."""

    cleaner_name: str
    metrics: dict[str, float]
    counts: dict[str, int]
