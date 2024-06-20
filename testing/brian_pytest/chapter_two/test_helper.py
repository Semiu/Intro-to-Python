import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cards_proj.src.cards.api import Card


def assert_identical(c1: Card, c2: Card):
    """
    Assertion helper function
    """
    __tracebackhide__ = True # This would hide the assert_identical function code in the traceback

    assert c1 == c2
    if c1.id != c2.id:
        pytest.fail(f"id's don't match. {c1.id} != {c2.id}")

def test_identical():
    c1 = Card("foo", id=123)
    c2 = Card("foo", id=123)

    assert_identical(c1, c2)

def test_identical_fail():
    c1 = Card("foo", id=123)
    c2 = Card("foo", id=456)

    assert_identical(c1, c2)

