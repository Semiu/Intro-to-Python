import pytest


@pytest.fixture()
def some_data():
    """ Return answer to a question """
    return 40

def test_some_data(some_data):
    """ Use the fixture return value in a test """
    assert some_data == 42