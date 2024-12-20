import pytest 
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from cards_proj.src import cards

"""
Combining markers with fixtures. The builtin markers took parameters while the custom ones do not.
Set to create new marker called num_cards which can be passed to the cards fixture
"""
@pytest.fixture(scope="function")
def cards_db(session_cards_db):
    """
    original fixture for tests that expect empty database
    """
    db = session_cards_db
    db.delete_all()
    return db


@pytest.fixture(scope="function")
def cards_db_three_cards(session_cards_db):
    """
    the new fixture for tests that expect the database 
    """
    db = session_cards_db
    # start with empty
    db.delete_all()

    # add three cards
    db.add_card(cards.Card("Learn something new"))
    db.add_card(cards.Card("Build useful tools"))
    db.add_card(cards.Card("Teach others"))
    return db

"""
These options give zero or three. But do we need to write fixture for each of the numbers we intend testing?
It is better we can tell the fixture the number of crds we want
This can be done with Markers as whon in test_num_cards.py
"""
def test_zero_card(cards_db):
    """
    uses the original fixture of empty database
    """
    assert cards_db.count() == 0

def test_three_card(cards_db_three_cards):
    """
    uses the new fixture of three cards
    """
    cards_db = cards_db_three_cards
    assert cards_db.count() == 3
