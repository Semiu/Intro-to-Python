import pytest 
import os
import sys

"""
Pytest's Markers - telling Pytest what to do.
Skip a test and report the reason
"""
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from cards_proj.src import cards

@pytest.mark.skip(reason="Card doesn't support < comparison yet")
def test_less_than():
    c1 = cards.Card("a task")
    c2 = cards.Card("b task")

    assert c1 < c2


def test_equality():
    c1 = cards.Card("a task")
    c2 = cards.Card("a task")

    assert c1 == c2


