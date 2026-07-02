"""Validator for cleaning proposals."""

from cleanbench.domain.models import CleaningProposal, ValidationResult


class ProposalValidator:
    """Reject unsafe, unauthorized, or structurally invalid modifications."""

    def validate(
        self,
        proposal: CleaningProposal,
        protected_columns: set[str],
        allowed_columns: set[str],
    ) -> ValidationResult:
        """Apply all constraints and return the resulting validation errors."""
        pass

    def validate_confidence(self, confidence: float) -> ValidationResult:
        """Validate that confidence lies within the inclusive range zero to one."""
        pass

    def validate_protected_field(
        self, proposal: CleaningProposal, protected_columns: set[str]
    ) -> ValidationResult:
        """Reject modifications to identifiers and other protected columns."""
        pass
