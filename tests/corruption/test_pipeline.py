from cleanbench.corruption.formatting import (
    CaseCorruptor,
    WhitespaceCorruptor,
)
from cleanbench.corruption.pipeline import (
    CorruptionCandidate,
    CorruptionPipeline,
)

import pandas as pd

import pytest


def test_pipeline_stores_an_independent_corruptor_sequence():
    """Verify that the pipeline keeps a stable copy of its corruptors."""
    whitespace_corruptor = WhitespaceCorruptor()
    case_corruptor = CaseCorruptor()

    original_list = [
        whitespace_corruptor,
        case_corruptor,
    ]

    pipeline = CorruptionPipeline(original_list)
    original_list.clear()

    assert pipeline.corruptors == (
        whitespace_corruptor,
        case_corruptor,
    )


def test_select_candidates_excludes_protected_columns():
    """Verify that only eligible, unprotected cells become candidates."""
    whitespace_corruptor = WhitespaceCorruptor()
    case_corruptor = CaseCorruptor()

    pipeline = CorruptionPipeline([whitespace_corruptor, case_corruptor])

    clean_frame = pd.DataFrame(
        {
            "patient_id": ["P001"],
            "name": ["Alice"],
            "private_note": ["Do not modify"],
        }
    )

    candidates = pipeline.select_candidates(
        clean_frame=clean_frame,
        id_column="patient_id",
        protected_columns={"private_note"},
    )

    assert candidates == [
        CorruptionCandidate(
            row_position=0,
            column="name",
            corruptor=whitespace_corruptor,
        ),
        CorruptionCandidate(
            row_position=0,
            column="name",
            corruptor=case_corruptor,
        ),
    ]


def test_run_with_zero_rate_returns_unchanged_copy():
    """Verify that a zero rate returns a new unchanged DataFrame."""
    pipeline = CorruptionPipeline([])
    clean_frame = pd.DataFrame(
        {
            "patient_id": ["P001"],
            "name": ["Alice"],
        }
    )

    dirty_frame, records = pipeline.run(
        clean_frame=clean_frame,
        id_column="patient_id",
        protected_columns=set(),
        corruption_rate=0,
        seed=42,
    )

    assert dirty_frame is not clean_frame
    pd.testing.assert_frame_equal(dirty_frame, clean_frame)
    assert records == []


@pytest.mark.parametrize("invalid_rate", [-0.1, 1.1])
def test_run_rejects_invalid_corruption_rate(invalid_rate):
    """Verify that corruption rates outside zero to one are rejected."""
    pipeline = CorruptionPipeline([])
    clean_frame = pd.DataFrame(
        {
            "patient_id": ["P001"],
            "name": ["Alice"],
        }
    )

    with pytest.raises(
        ValueError,
        match="corruption_rate must be between 0 and 1",
    ):
        pipeline.run(
            clean_frame=clean_frame,
            id_column="patient_id",
            protected_columns=set(),
            corruption_rate=invalid_rate,
            seed=42,
        )
