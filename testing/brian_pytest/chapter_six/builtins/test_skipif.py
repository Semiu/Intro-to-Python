import pytest 
import os
import sys
from packaging.version import parse
"""
Pytest's Markers - telling Pytest what to do.
Skip a test when a condition is met and report the reason
"""
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from cards_proj.src import cards



@pytest.mark.skipif(
        parse(cards.__version__).major < 2,
        reason="Card < comparison not supported in 1.x",
)
def test_less_than():
    c1 = cards.Card("a task")
    c2 = cards.Card("b task")

    assert c1 < c2