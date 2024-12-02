import pytest 
import os
import sys
"""
Pytest's Markers - telling Pytest what to do.
Normal test and a good case for exception - using marker to name some smoke
This can be selectively tested
"""
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from cards_proj.src import cards 

@pytest.mark.smoke
def test_start(cards_db):
    """
    start changes state from 'todo' to 'in prog'
    """
    i = cards_db.add_card(cards.Card("foo", state="in prog"))
    cards_db.start(i)
    c = cards_db.get_card(i)

@pytest.mark.exception
def test_start_non_existent(cards_db):
    """
    Shouldn't be able to start a non-existent card
    """
    any_number = 123 # any number will be invalid since db is empty
    with pytest.raises(cards.InvalidCardId):
        cards_db.start(any_number)