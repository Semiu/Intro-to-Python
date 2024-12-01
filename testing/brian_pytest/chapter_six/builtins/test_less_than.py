import pytest 
import os
import sys

"""
Pytest's Markers - telling Pytest what to do.
This sets the tone for what to follow
"""
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from cards_proj.src import cards

def test_less_than():
    c1 = cards.Card("a task")
    c2 = cards.Card("b task")

    assert c1 < c2


def test_equality():
    c1 = cards.Card("a task")
    c2 = cards.Card("b task")

    assert c1 == c2
    