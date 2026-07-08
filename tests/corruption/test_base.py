from cleanbench.corruption.formatting import WhitespaceCorruptor
from cleanbench.domain.models import CellAddress, CorruptionType


def test_build_record_stores_corruption_ground_truth():
    """Verify that a corruptor builds a complete ground-truth record."""
    corruptor = WhitespaceCorruptor()
    address = CellAddress(row_id="P001", column="name")

    record = corruptor.build_record(
        address=address,
        clean_value="Alice",
        corrupted_value=" Alice ",
        seed=42,
        metadata={"strategy": "surrounding"},
    )

    assert record.address == address
    assert record.clean_value == "Alice"
    assert record.corrupted_value == " Alice "
    assert record.corruption_type is CorruptionType.WHITESPACE
    assert record.seed == 42
    assert record.metadata == {"strategy": "surrounding"}
