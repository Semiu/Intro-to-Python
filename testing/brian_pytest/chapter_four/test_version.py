import subprocess
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cards_proj.src import cards


def test_version_v1():
    """
    Testing what prints to the CLI. For example, print(cards.__version__) outputs '1.0.0'
    Using subprocess library to capture the output
    """
    process = subprocess.run(["cards", "version"], capture_output=True, text=True)
    output = process.stdout.rstrip()

    assert output == cards.__version__


def test_version_v2(capsys):
    """
    Using the PyTest capsys fixture, instead of using subprocess
    """
    cards.cli.version() # Writes the version to CLI
    output = capsys.readouterr().out.rstrip() # Reads and formats what is written to the CLI

    assert output == cards.__version__
