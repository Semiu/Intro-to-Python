import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cards_proj.src.cards.api import CardsDB

""" Using PyTest's tmp_path_factory instead of TemporaryDirectory method from tempfile library """

@pytest.fixture(scope="session")
def db(tmp_path_factory):
    """ CardDB object connected to temporary database """
    db_path = tmp_path_factory.mktemp("cards_db")
    db_ = CardsDB(db_path)
    yield db_
    db_.close()