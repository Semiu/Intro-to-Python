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