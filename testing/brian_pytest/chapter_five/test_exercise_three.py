import pytest 
import os
import sys

"""
Pytest's parametrize using fixtures
The need to pass different data inputs to test the same function is being simplified by the Pytest's parametrize
parametrize decorator solves the pending problem in combining the test cases into one
This is for the 
"""
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cards_proj.src import cards

@pytest.fixture(params=["done", "in prog", "todo"])
def start_state(request):
    return request.param


def test_start(cards_db, start_state):
    initial_card = cards.Card("Pick a topic", state=start_state)
    index = cards_db.add_card(initial_card)

    # The start API sets the card's state to "in prog"
    cards_db.start(index)

    card = cards_db.get_card(index)

    assert card.state == "in prog"