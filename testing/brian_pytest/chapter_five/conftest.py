import pytest 
import sys
import os
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cards_proj.src.cards.api import CardsDB

@pytest.fixture(scope="session")
def cards_db():
    """CardsDB object connected to a temporary database"""
    with TemporaryDirectory() as cards_db_dir:
        cards_db_path = Path(cards_db_dir) # Pathlib as standard way of representing system paths. The 
        cards_db = CardsDB(cards_db_path) # Get the database object. These are all to set up the db object to be able to test the count

        yield cards_db # Set up
        cards_db.close() # Tear down