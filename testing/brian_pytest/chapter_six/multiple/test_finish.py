import pytest 
import os
import sys
"""
Pytest's Markers - telling Pytest what to do.
Normal test and a good case for exception - using marker to name some smoke
This can be selectively tested
"""
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from cards_proj.src.cards import Card, InvalidCardId

# With this pytestmark attribute, pytest applies the marker(s) (finish) to all the tests in the module
# It can be more than one marker, e.g. pytestmark = [pytest.mark.marker_one, pytest.mark.marker_two]
pytestmark = pytest.mark.finish

"""
Another way is class level for multiple test at once
"""
@pytest.mark.smoke
class TestFinish:
    """
    With the decorator marker on the class TestFinish, all methods therein are now marked the same marker
    """
    def test_finish_from_todo(self, cards_db):
        i = cards_db.add_card(Card("foo", state="todo"))
        cards_db.finish(i)

        c = cards_db.get_card(i)
        assert c.state == "done"
    def test_finish_from_in_prog(self, cards_db):
        i = cards_db.add_card(Card("foo", state="in prog"))
        cards_db.finish(i)

        c = cards_db.get_card(i)
        assert c.state == "done"
    def test_finish_from_done(self, cards_db):
        i = cards_db.add_card(Card("foo", state="done"))
        cards_db.finish(i)

        c = cards_db.get_card(i)
        assert c.state == "done"


@pytest.mark.parametrize(
    "start_state",
    [
        "todo",
        pytest.param("in prog", marks=pytest.mark.smoke),
        "done",
    ]
)
def test_finish_func(cards_db, start_state):
        """
        The decorator marks specific param - "in prog"
        More than one marker can be used marks=[pytest.mark.one, pytest.mark.two]
        If marking all test cases of a parametrized test, then add a mark as it would done for a regular function
        """
        i = cards_db.add_card(Card("foo", state=start_state))
        cards_db.finish(i)

        c = cards_db.get_card(i)
        assert c.state == "done"


@pytest.fixture(
    params=[
        "todo",
        pytest.param("in prog", marks=pytest.mark.smoke),
        "done",
    ]
)
def start_state_fixture(request):
    """
    for fixture parameterization
    """
    return request.param

def test_finish_fix(cards_db, start_state_fixture):
    i = cards_db.add_card(Card("foo", state=start_state_fixture))
    cards_db.finish(i)

    c = cards_db.get_card(i)
    assert c.state == "done"

@pytest.mark.smoke
@pytest.mark.exception
def test_finish_non_existent(cards_db):
    """
    Two markers on a function
     
    """
    i = 123
    with pytest.raises(InvalidCardId):
        cards_db.finish(i)