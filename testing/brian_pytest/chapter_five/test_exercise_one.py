import os
import sys
"""
Pytest's parametrize 
The need to pass different data inputs to test the same function is being simplified by the Pytest's parametrize
To start, three different test cases are being written here to test the three different input data
"""
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cards_proj.src import cards


def test_start_from_done(cards_db):
    index = cards_db.add_card(cards.Card("second edition", state="done"))
    # The start API sets the card's state to "in prog"
    cards_db.start(index)

    card = cards_db.get_card(index)
    assert card.state == "in prog"


def test_start_from_in_prog(cards_db):
    index = cards_db.add_card(cards.Card("write a book", state="in prog"))
    # The start API sets the card's state to "in prog"
    cards_db.start(index)

    card = cards_db.get_card(index)
    assert card.state == "in prog"


def test_start_from_todo(cards_db):
    index = cards_db.add_card(cards.Card("create a course", state="todo"))
    # The start API sets the card's state to "in prog"
    cards_db.start(index)

    card = cards_db.get_card(index)
    assert card.state == "in prog"