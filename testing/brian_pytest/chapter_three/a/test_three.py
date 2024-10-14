import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from cards_proj.src.cards.api import Card

""" The demostration of the conftest.py file - where fixture is defined and implictly imported into the test file within the same directory """

def test_three(cards_db):
    # cards_db is defined as a fixture in the conftest.py file
    cards_db.add_card(Card("first"))
    cards_db.add_card(Card("second"))
    cards_db.add_card(Card("third"))

    assert cards_db.count() == 3