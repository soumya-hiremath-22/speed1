import pytest
from Speed import calculate_speed
def test_calculate_speed():
    result=calculate_speed(100, 2)
    expected=50
    
    assert result==expected