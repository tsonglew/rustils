def test_basic():
    """A basic test to verify pytest is working"""
    assert True

def test_version():
    """Test that version is available"""
    from rustils import __version__
    assert isinstance(__version__, str)
    assert len(__version__) > 0

import pytest
from rustils import str_to_bool

def test_str_to_bool_true():
    """Test string to bool conversion for true values"""
    assert str_to_bool("true")
    assert str_to_bool("True")
    assert str_to_bool("1")
    assert str_to_bool("yes")
    assert str_to_bool("Y")
    assert str_to_bool("on")

def test_str_to_bool_false():
    """Test string to bool conversion for false values"""
    assert not str_to_bool("false")
    assert not str_to_bool("False")
    assert not str_to_bool("0")
    assert not str_to_bool("no")
    assert not str_to_bool("N")
    assert not str_to_bool("off")

def test_str_to_bool_invalid():
    """Test string to bool conversion with invalid input"""
    with pytest.raises(ValueError):
        str_to_bool("invalid")
    with pytest.raises(ValueError):
        str_to_bool("")
