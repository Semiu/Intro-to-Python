import pytest 
import sys
import os
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from cards_proj.src.cards.api import CardsDB, Card

@pytest.fixture()
def cards_db():
    """CardsDB object connected to a temporary database"""
    with TemporaryDirectory() as cards_db_dir:
        cards_db_path = Path(cards_db_dir) # Pathlib as standard way of representing system paths. The 
        cards_db = CardsDB(cards_db_path) # Get the database object. These are all to set up the db object to be able to test the count

        yield cards_db # Set up
        cards_db.close() # Tear down


@pytest.fixture(scope="session")
def some_cards():
    """List of different card objects"""

    return [
        Card("write book", "Brian", "done"),
        Card("edit book", "Katie", "done"),
        Card("write 2nd edition", "Brian", "todo"),
        Card("edit 2nd edition", "Katie", "todo")

    ]

@pytest.fixture()
def non_empty_db(cards_db, some_cards):
    """ CardsDB object that's been populated with 'some_cards' """

    for card in some_cards:
        cards_db.add_card(card)
    
    return cards_db