import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

def test_add_some(cards_db, some_cards):
    expected_count = len(some_cards)

    for card in some_cards:
        cards_db.add_card(card)
    
    assert cards_db.count() == expected_count

def test_non_empty(non_empty_db):
    assert non_empty_db.count() > 0