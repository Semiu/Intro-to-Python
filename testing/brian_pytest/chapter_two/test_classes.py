import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cards_proj.src.cards.api import Card

class TestEquality:
    def test_equality(self):
        card_1 = Card("something", "brian", "todo", 123)
        card_2 = Card("something", "brian", "todo", 123)

        assert card_1 == card_2
    
    def test_equality_with_diff_ids(self):
        card_1 = Card("something", "brian", "todo", 123)
        card_2 = Card("something", "brian", "todo", 4567)

        assert card_1 == card_2
    
    def test_inequality(self):
        card_1 = Card("something", "brian", "todo", 123)
        card_2 = Card("completely different", "okken", "done", 123)

        assert card_1 != card_2