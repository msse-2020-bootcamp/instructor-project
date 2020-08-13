"""
Tests for the coord module
"""
import os
import sys

# Add our folder to the system path so python can find our code.
current_location = os.path.dirname(__file__)
sys.path.append(os.path.join(current_location, '..'))

from mcsim.coordinates import calculate_distance

def test_calculate_distance():
    point_1 = [0, 0, 0]
    point_2 = [1, 0, 0]

    expected_distance = 1
    dist1 = calculate_distance(point_1, point_2)
    
    assert dist1 == expected_distance