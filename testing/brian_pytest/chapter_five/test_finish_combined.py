import os
import sys

"""
Pytest's parametrize 
The need to pass different data inputs to test the same function is being simplified by the Pytest's parametrize
Instead of three different tests as written in test_finish.py, this combines them into one.
But this is problematic because it treats them just as a single test case
"""
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cards_proj.src import cards


def test_finish(cards_db):
    for c in [
        cards.Card("write a book", state="done"),
        cards.Card("second edition", state="in prog"),
        cards.Card("create a course", state="todo")
    ]:
        index =  cards_db.add_card(c)
        # The finish API sets the card's state to "done"
        cards_db.finish(index)

        card = cards_db.get_card(index)

        assert card.state == "done"