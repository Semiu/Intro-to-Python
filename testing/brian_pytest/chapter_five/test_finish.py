import os
import sys

"""
Pytest's parametrize 
The need to pass different data inputs to test the same function is being simplified by the Pytest's parametrize
Three different test cases are being written here to test the three different input data
"""
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cards_proj.src import cards


def test_finish_from_in_prog(cards_db):
    index = cards_db.add_card(cards.Card("second edition", state="in prog"))
    # The finish API sets the card's state to "done"
    cards_db.finish(index)

    card = cards_db.get_card(index)

    assert card.state == "done"

def test_finish_from_done(cards_db):
    index = cards_db.add_card(cards.Card("write a book", state="done"))
    # The finish API sets the card's state to "done"
    cards_db.finish(index)

    card = cards_db.get_card(index)

    assert card.state == "done"


def test_finish_from_todo(cards_db):
    index = cards_db.add_card(cards.Card("create a course", state="todo"))
    # The finish API sets the card's state to "done"
    cards_db.finish(index)

    card = cards_db.get_card(index)

    assert card.state == "done"