import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cards_proj.src.cards.db import DB


def test_no_path_raises():
    with pytest.raises(TypeError):
        DB()

def test_raises_with_info():
    match_regex = "missing 2 .* positional arguments"
    with pytest.raises(TypeError, match=match_regex):
        DB()
    

def test_raises_with_info_alt():
    with pytest.raises(TypeError) as exc_info:
        DB()
    expected = "missing 2 required positional arguments"
    assert expected in str(exc_info.value)