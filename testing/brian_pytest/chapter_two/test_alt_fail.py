import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cards_proj.src.cards.api import Card



def test_equality_fail():
    c1 = Card("sit there", "brian")
    c2 = Card("do something", "okken")

    if c1 != c2:
        pytest.fail("They don't match!")
