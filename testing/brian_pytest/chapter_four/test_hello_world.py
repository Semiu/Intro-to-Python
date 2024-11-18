import pytest

from pathlib import Path

def test_hello_no_fixture():
    with open("hello.txt", "r") as f:
        file_content = f.read()
    
    assert file_content == "Hello World!\n"


def test_hello_with_fixtures(monkeypatch, tmp_path):
    # Change current working direction to tmp_path
    monkeypatch.chdir(tmp_path)

    print(tmp_path)

    file_ = tmp_path / "hello.txt"
    file_.write_text("Hello World!")

    assert file_.read_text() == "Hello World!"
    assert tmp_path == Path.cwd()
