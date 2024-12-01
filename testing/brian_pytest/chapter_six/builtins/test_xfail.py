import pytest 
import os
import sys
from packaging.version import parse
"""
Pytest's Markers - telling Pytest what to do.
Different flavors of XFAIL
"""
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from cards_proj.src import cards


@pytest.mark.xfail(
        parse(cards.__version__).major < 2,
        reason="Card < comparison not supported in 1.x",
)
def test_less_than():
    """
    This will XFAIL. Fail test, but reason for failure is listed
    """
    c1 = cards.Card("a task")
    c2 = cards.Card("b task")

    assert c1 < c2

@pytest.mark.xfail(
        reason="XPASS demo",
)
def test_xpass():
    """
    This is XPASS because it is passing test and no strict=True param is added, 
    even though it is with xfail marker
    """
    c1 = cards.Card("a task")
    c2 = cards.Card("a task")

    assert c1 == c2

@pytest.mark.xfail(
        reason="strict demo",
        strict=True
)
def test_xfail_strict():
    """
    This is FAIL test because strict is set to True,
    even though the test should ordinarily pass
    """
    c1 = cards.Card("a task")
    c2 = cards.Card("a task")

    assert c1 == c2