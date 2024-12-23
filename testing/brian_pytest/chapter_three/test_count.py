import pytest 
import sys
import os
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cards_proj.src.cards.api import Card, CardsDB

""" Fixture used. Therefore, the cards_db needs to be defined once. Then, used in the two test functions """

@pytest.fixture()
def cards_db():
    with TemporaryDirectory() as cards_db_dir:
        cards_db_path = Path(cards_db_dir) # Pathlib as standard way of representing system paths. The 
        cards_db = CardsDB(cards_db_path) # Get the database object. These are all to set up the db object to be able to test the count

        yield cards_db # Set up
        cards_db.close() # Tear down

def test_empty(cards_db):
    assert cards_db.count() == 0

def test_count(cards_db):
    # Test runs immediately after the yield statement (set up)
    # It is after the test run that the DB object closes (tear down)
    cards_db.add_card(Card("first"))
    cards_db.add_card(Card("second"))

    assert cards_db.count() == 2