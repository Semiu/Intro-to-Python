import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cards_proj.src.cards.api import Card

def test_equality_fail():
    c1 = Card("sit there", "brian")
    c2 = Card("do something", "okken")

    assert c1 == c2



if __name__ == "__main__":
    test_equality_fail()