import pytest

import load_scores


def test_loads_valid_scores_and_preserves_duplicate_names(tmp_path):
    csv_file = tmp_path / "scores.csv"
    csv_file.write_text(
        "\ufeff이름,점수\n김민수, 0 \n\n김민수,100\n",
        encoding="utf-8",
    )

    kept, skipped = load_scores.load_scores(csv_file)

    assert kept == [("김민수", 0), ("김민수", 100)]
    assert skipped == []


def test_header_only_file_returns_empty_lists(tmp_path):
    csv_file = tmp_path / "scores.csv"
    csv_file.write_text("이름,점수\n", encoding="utf-8")

    assert load_scores.load_scores(csv_file) == ([], [])


@pytest.mark.parametrize(
    ("row", "original", "reason"),
    [
        ("학생", "학생", "열 개수가 2가 아님"),
        ("학생,90,추가", "학생,90,추가", "열 개수가 2가 아님"),
        (",90", ",90", "이름이 비어 있음"),
        ("학생,", "학생,", "점수가 비어 있음"),
        ("학생,abc", "학생,abc", "점수가 정수가 아님"),
        ("학생,-1", "학생,-1", "점수가 0~100 밖"),
        ("학생,101", "학생,101", "점수가 0~100 밖"),
    ],
)
def test_records_invalid_rows(tmp_path, row, original, reason):
    csv_file = tmp_path / "scores.csv"
    csv_file.write_text(f"이름,점수\n{row}\n", encoding="utf-8")

    kept, skipped = load_scores.load_scores(csv_file)

    assert kept == []
    assert skipped == [(2, original, reason)]


def test_missing_file_raises_file_not_found_error(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_scores.load_scores(tmp_path / "missing.csv")
