"""Experiment configuration loading and validation."""

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class ExperimentConfig:
    """Store all configuration required for one experiment."""

    experiment_name: str
    random_seed: int
    dataset_path: Path
    output_dir: Path
    id_columns: tuple[str, ...] = field(default_factory=tuple)
    protected_columns: tuple[str, ...] = field(default_factory=tuple)
    corruption_rate: float = 0.1
    corruption_types: tuple[str, ...] = field(default_factory=tuple)
    cleaners: tuple[str, ...] = field(default_factory=tuple)


class ConfigLoader:
    """Convert YAML configuration into an ExperimentConfig object."""

    def load(self, path: Path) -> ExperimentConfig:
        """Load and validate a configuration file."""
        pass

    def validate(self, config: ExperimentConfig) -> None:
        """Validate rates, paths, columns, and cleaner names."""
        pass
