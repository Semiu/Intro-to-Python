import pytest 
import os
import sys

"""
Pytest's parametrize using functions
The need to pass different data inputs to test the same function is being simplified by the Pytest's parametrize
parametrize decorator solves the pending problem in combining the test cases into one
"""
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cards_proj.src import cards


@pytest.mark.parametrize(
    "start_summary, start_state",
    [
        ("write a book", "done"),
        ("second edition", "in prog"),
        ("create a course", "todo")
    ]
)
def test_start(cards_db, start_summary, start_state):
    initial_card = cards.Card(summary=start_summary, state=start_state)
    index = cards_db.add_card(initial_card)

    # The start API sets the card's state to "in prog"
    cards_db.start(index)

    card = cards_db.get_card(index)

    assert card.state == "in prog"

"""
Since we're only interested in testing the start_state, we can take out the start_summary
"""
@pytest.mark.parametrize(
    "start_state",
    [
        ("done"),
        ( "in prog"),
        ("todo")
    ]
)
def test_start_simple(cards_db, start_state):
    initial_card = cards.Card("write a book", state=start_state)
    index = cards_db.add_card(initial_card)

    # The start API sets the card's state to "in prog"
    cards_db.start(index)

    card = cards_db.get_card(index)

    assert card.state == "in prog"