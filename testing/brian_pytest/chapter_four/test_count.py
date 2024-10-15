import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cards_proj.src.cards.api import Card

""" The demostration of the conftest.py file - where fixture is defined and implictly imported into the test file within the same directory 
The conftest.py file in this chapter 4 uses the PyTest's tmp_path_factory instead of TemporaryDirectory method from tempfile library
"""
def test_empty(db):
    # db is defined as a fixture in the conftest.py file
    assert db.count() == 0

def test_two(db):
    db.add_card(Card("first"))
    db.add_card(Card("second"))

    assert db.count() == 2