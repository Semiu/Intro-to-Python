from typer.testing import CliRunner
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cards_proj.src import cards

def run_cards(*params):
    """ Gets the CLI output from the cards version output command"""
    runner = CliRunner()
    result = runner.invoke(cards.app, params)
    return result.output.rstrip()

def test_run_cards():
    """ Test function for the run_cards (helper) function """
    assert run_cards("version") == cards.__version__


def test_patch_get_path(monkeypatch, tmp_path):
    """ Taking two Pytest inbuilt fixtures """
    def fake_get_path():
        return tmp_path
    
    """
    This is replacing the get_path attribute of the cards.cli class with fake_get_path
    A callable function must be replaced with another callable function and this is why we cannot just replace get_path with tmp_path which is
    a pathlib.Path object which is not callable
    """
    monkeypatch.setattr(cards.cli, "get_path", fake_get_path)

    assert run_cards("config") == str(tmp_path)

def test_patch_home(monkeypatch, tmp_path):
    """
    Replacing the home() in pathlib.Path with similar patch
    """
    full_cards_dir = tmp_path / "cards_db"
    def fake_home():
        return tmp_path
    # Patching the home attribute of cards.cli.pathlib.Path since cards.cli imports pathlib
    monkeypatch.setattr(cards.cli.pathlib.Path, "home", fake_home)

    assert run_cards("config") == str(full_cards_dir)

def test_patch_env_var(monkeypatch, tmp_path):
    """
    Tests environment variable setting
    """
    monkeypatch.setenv("CARDS_DB_DIR", str(tmp_path))

    assert run_cards("config") == str(tmp_path)
    