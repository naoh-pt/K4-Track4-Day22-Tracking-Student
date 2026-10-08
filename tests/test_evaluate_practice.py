"""Kiểm tra chuẩn bị dữ liệu chấm bằng các file giả, không dùng dữ liệu lab."""

import json
from pathlib import Path

import pytest

import evaluate_practice
from evaluate_practice import _load_eval_config, stage


def test_load_eval_config(tmp_path: Path) -> None:
    video = tmp_path / "video_1"
    video.mkdir()
    config = {"benchmark": "LAB21", "split": "train"}
    (video / "eval_config.json").write_text(json.dumps(config), encoding="utf-8")
    assert _load_eval_config(tmp_path) == config


def test_missing_eval_config(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError, match="eval_config.json"):
        _load_eval_config(tmp_path)


@pytest.mark.parametrize("split", ["train", "test"])
def test_stage_uses_selected_split(tmp_path: Path, split: str) -> None:
    lab = tmp_path / "lab"
    video = lab / "video_1"
    (video / "gt").mkdir(parents=True)
    (video / "gt" / "gt.txt").write_text("nhãn giả", encoding="utf-8")
    (video / "seqinfo.ini").write_text("cấu hình giả", encoding="utf-8")
    submission = tmp_path / "video_1.txt"
    submission.write_text("kết quả giả", encoding="utf-8")
    root = tmp_path / "trackeval"
    stage(root, lab, submission, "nhom", "LAB21", split)
    gt = root / "data/gt/mot_challenge" / f"LAB21-{split}" / "video_1"
    tracks = root / "data/trackers/mot_challenge" / f"LAB21-{split}" / "nhom/data"
    assert (gt / "gt/gt.txt").read_text(encoding="utf-8") == "nhãn giả"
    assert (gt / "seqinfo.ini").read_text(encoding="utf-8") == "cấu hình giả"
    assert (tracks / "video_1.txt").read_text(encoding="utf-8") == "kết quả giả"
    assert not (gt.parent / "video_2").exists()


def test_stage_requires_practice_labels(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError, match="thiếu gt"):
        stage(tmp_path / "trackeval", tmp_path / "lab", tmp_path / "video_1.txt", "nhom", "LAB21")


@pytest.mark.parametrize("index", [2, 3, 4, 5])
def test_only_practice_video_can_be_scored(monkeypatch: pytest.MonkeyPatch, index: int) -> None:
    monkeypatch.setattr(evaluate_practice, "_patch_numpy_aliases", lambda: None)
    monkeypatch.setattr("sys.argv", [
        "evaluate_practice.py", "--trackeval-root", "trackeval", "--lab-data-root", "lab",
        "--submission", f"video_{index}.txt", "--run-name", "nhom",
    ])
    with pytest.raises(SystemExit, match="chỉ chấm video_1"):
        evaluate_practice.main()
