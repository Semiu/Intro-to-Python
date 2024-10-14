import pytest 

@pytest.fixture(name="ultimate_answer")
def ultimate_answer_fixture():
    # Fixture name is changed with the decorator to 'ultimate_answer'
    return 42

def test_everything(ultimate_answer):
    # Then, 'ultimate_answer' is used
    assert ultimate_answer == 42