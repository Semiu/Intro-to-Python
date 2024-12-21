import pytest

def test_no_marker(cards_db_session):
    assert cards_db_session.count() == 0

@pytest.mark.num_cards
def test_three_cards(cards_db_session):
    assert cards_db_session.count() == 0

@pytest.mark.num_cards(3)
def test_three_cards(cards_db_session):
    assert cards_db_session.count() == 3
    # Seeing what the faker does
    print()
    for c in cards_db_session.list_cards():
        print(c)

@pytest.mark.num_cards(10)
def test_three_cards(cards_db_session):
    assert cards_db_session.count() == 10