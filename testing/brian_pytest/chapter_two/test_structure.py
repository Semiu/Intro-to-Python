import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cards_proj.src.cards.api import Card

def test_to_dict():
    # GIVEN a card object with known contents
    # ARANGE starting state
    c1 = Card("something", "brian", "todo", 123)
    # WHEN we call to_dict() on the object
    # ACT to perform some action
    c2 = c1.to_dict()
    # THEN the result would be dictionary with a known content
    # ASSERT the expected result
    c2_expected = {
        "summary": "something",
                   "owner": "brian",
                   "state": "todo",
                   "id": 123
    }
    assert c2 == c2_expected