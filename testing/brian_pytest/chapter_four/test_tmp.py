"""
tmp_path and tmp_path_factory are PyTest fixtures to create temporary directories
pytest --fixtures
"""
def test_tmp_path(tmp_path):
    # Function scope that returns a pathlib.Path
    file = tmp_path / "file.txt"
    file.write_text("Hello, PyTest!")
    assert file.read_text() == "Hello, PyTest!"


def test_tmp_path_factory(tmp_path_factory):
    # Session scope that returns TempPathFactory object
    path = tmp_path_factory.mktemp("sub")
    file = path / "file.txt"
    file.write_text("Hello, PyTest!")
    assert file.read_text() == "Hello, PyTest!"