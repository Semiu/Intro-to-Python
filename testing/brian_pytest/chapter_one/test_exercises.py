"""Tesing demo for exercise 5 in chapter 1"""

def test_exercise_fail():
    assert 1 in (2,3,4)
    assert 'fizz' not in 'fizzbuzz'

def test_exercise_pass():
    a = 3
    b = 5
    assert a < b
    assert 3 in (2,5,3)