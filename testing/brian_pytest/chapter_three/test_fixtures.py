import pytest


@pytest.fixture()
def some_data():
    """ Return answer to a question """
    return 40

@pytest.fixture()
def get_list():
    """A list of integer"""
    return [9, 13, 2, 10, 6]

@pytest.fixture(scope="module")
def get_student_data():
    """Mocked student data"""
    
    print("== Before the data - setup ==")
    yield {
        "0": {"name":"Ade", "age":50, "sex":"male"},
        "1": {"name":"Busola", "age":22, "sex":"female"},
        "2": {"name":"Malik", "age":31, "sex": "male"}
    }
    print("== After the data - teardown ==")


def test_some_data(some_data):
    """ Use the some_data fixture return value in a test """
    assert some_data == 40

def test_list_member(get_list):
    """ Use the get_list fixture return value in a test """
    assert 13 in get_list

def test_student_data(get_student_data):
    """ Use the get_list fixture return value in a test """
    assert get_student_data["0"] == {"name":"Ade", "age":50, "sex":"male"}

def test_student_data_keys(get_student_data):
    """ Use the get_list fixture return value in a test """
    assert "0" in get_student_data