from cleanbench.corruption.formatting import (
    CaseCorruptor,
    WhitespaceCorruptor,
)
from cleanbench.corruption.pipeline import CorruptionPipeline


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