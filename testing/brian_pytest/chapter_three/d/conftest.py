import pytest 
import sys
import os
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from cards_proj.src.cards.api import CardsDB

def db_scope(fixture_name, config):
    if config.getoption("--func-db", None):
        return "function"
    return "session"

@pytest.fixture(scope=db_scope)
def db():
    """CardsDB object connected to a temporary database"""
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir) # Pathlib as standard way of representing system paths. The 
        db_ = CardsDB(db_path) # Get the database object. These are all to set up the db object to be able to test the count

        yield db_ # Set up
        db_.close() # Tear down

@pytest.fixture(scope="function")
def cards_db(db):
    """CardsDB object emptied"""
    db.delete_all()
    return db

def pytest_addoption(parser):
    parser.addoption(
        "--func-db",
        action="store_true",
        default=False,
        help="new db for each test"
    )

