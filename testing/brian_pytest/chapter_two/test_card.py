import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cards_proj.src.cards.api import Card


def test_field_access():
    card = Card("something", "brian", "todo", 123)

    assert card.summary == "something"
    assert card.owner == "brian"
    assert card.state == "todo"
    assert card.id == 123

def test_defaults():
    card = Card()

    assert card.summary is None
    assert card.owner is None
    assert card.state == "todo"
    assert card.id is None

def test_equality():
    card_1 = Card("something", "brian", "todo", 123)
    card_2 = Card("something", "brian", "todo", 123)

    assert card_1 == card_2

def test_equality_with_diff_ids():
    card_1 = Card("something", "brian", "todo", 123)
    card_2 = Card("something", "brian", "todo", 4567)

    assert card_1 == card_2

def test_inequality():
    card_1 = Card("something", "brian", "todo", 123)
    card_2 = Card("completely different", "okken", "done", 123)

    assert card_1 != card_2

def test_from_dict():
    card_1 = Card("something", "brian", "todo", 123)
    card_2_dict = {"summary": "something",
                   "owner": "brian",
                   "state": "todo",
                   "id": 123
                   }
    card_2 = Card.from_dict(card_2_dict)

    assert card_1 == card_2

def test_to_dict():
    card_1 = Card("something", "brian", "todo", 123)
    card_2 = card_1.to_dict()

    card_2_expected = {
        "summary": "something",
                   "owner": "brian",
                   "state": "todo",
                   "id": 123
    }
    assert card_2 == card_2_expected

