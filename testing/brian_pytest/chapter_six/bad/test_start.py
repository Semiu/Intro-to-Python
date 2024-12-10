import pytest 
import os
import sys
"""
Pytest's Markers - telling Pytest what to do.
A case for exception - to explain marking concepts in Pytest
Strict with Markers
"""
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from cards_proj.src import cards 

"""
When run with pytest -m smoke for the `smok` marker (mistake/error), we get the usual is this typo warning.
To ensure this comes as error, run as pytest --strict-markers -m smoke
"""

@pytest.mark.smok
@pytest.mark.exception
def test_start_non_existent(cards_db):
    """
    Shouldn't be able to start a non-existent card
    """
    any_number = 123 # any number will be invalid since db is empty
    with pytest.raises(cards.InvalidCardId):
        cards_db.start(any_number)