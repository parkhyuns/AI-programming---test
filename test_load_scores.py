def test_일부러_틀린_테스트():
    kept, skipped = load_scores("scores.csv")
    assert len(kept) == 99

pytest
test_load_scores.py .F