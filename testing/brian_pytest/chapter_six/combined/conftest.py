import pytest 
import sys
import os
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from cards_proj.src.cards.api import CardsDB
from cards_proj.src import cards

@pytest.fixture(scope="session")
def cards_db():
    """CardsDB object connected to a temporary database"""
    with TemporaryDirectory() as cards_db_dir:
        cards_db_path = Path(cards_db_dir) # Pathlib as standard way of representing system paths. The 
        cards_db = CardsDB(cards_db_path) # Get the database object. These are all to set up the db object to be able to test the count

        yield cards_db # Set up
        cards_db.close() # Tear down

@pytest.fixture(scope="function")
def cards_db_session(cards_db, request, faker):
    """
    request: to get a MArker object if the test is marked 'num_cards'
    faker: 
    page 90 of the Brian Okken's book for further details
    """
    db = cards_db
    db.delete_all()

    # support for `@pytest.mark.num_cards(<some numbers)` in the test_num_cards.py
    # random seed
    faker.seed_instance(101)
    m = request.node.get_closest_marker("num_cards")
    if m and len(m.args) > 0:
        num_cards = m.args[0]
        for _ in range(num_cards):
            db.add_card(
                cards.Card(summary=faker.sentence(), owner=faker.first_name())
            )
    return db
