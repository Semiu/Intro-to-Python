import sys
import os
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cards_proj.src.cards.db import DB
from cards_proj.src.cards.api import CardsDB

def test_empty_db():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir) # Pathlib as standard way of representing system paths. The 
        db = DB(db_path, "count") # Get the database object. These are all to set up the db object to be able to test the count

        count = db.count()
        db.close()

        assert count == 0

def test_empty_cardsdb():
    with TemporaryDirectory() as cards_db_dir:
        cards_db_path = Path(cards_db_dir) # Pathlib as standard way of representing system paths. The 
        cars_db = CardsDB(cards_db_path) # Get the database object. These are all to set up the db object to be able to test the count

        count = cars_db.count()
        cars_db.close()

        assert count == 0