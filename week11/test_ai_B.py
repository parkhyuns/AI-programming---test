import pytest

import load_scores


def test_loads_name_score_rows(tmp_path):
    csv_file = tmp_path / "scores.csv"
    csv_file.write_text("name,score\nAlice,85\nBob,0\n", encoding="utf-8")

    assert load_scores.load_scores(csv_file) == [("Alice", 85), ("Bob", 0)]


def test_accepts_score_boundaries_and_duplicate_names(tmp_path):
    csv_file = tmp_path / "scores.csv"
    csv_file.write_text(
        "name,score\nAlice,0\nAlice,100\n",
        encoding="utf-8",
    )

    assert load_scores.load_scores(csv_file) == [("Alice", 0), ("Alice", 100)]


@pytest.mark.parametrize(
    "row",
    [
        "Alice",
        "Alice,85,extra",
        ",85",
        "Alice,",
        "Alice,not-a-number",
        "Alice,-1",
        "Alice,101",
    ],
)
def test_invalid_row_raises_error_with_row_number(tmp_path, row):
    csv_file = tmp_path / "scores.csv"
    csv_file.write_text(f"name,score\n{row}\n", encoding="utf-8")

    with pytest.raises(ValueError) as exc_info:
        load_scores.load_scores(csv_file)

    assert "2" in str(exc_info.value)


def test_missing_file_raises_file_not_found_error(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_scores.load_scores(tmp_path / "missing.csv")


def test_invalid_header_raises_error(tmp_path):
    csv_file = tmp_path / "scores.csv"
    csv_file.write_text("student,points\nAlice,85\n", encoding="utf-8")

    with pytest.raises(ValueError):
        load_scores.load_scores(csv_file)
