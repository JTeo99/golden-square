from lib.high_value import *

def test_class_attributes_first():
    highvalue = HighValue(7, 2)
    value = highvalue.value_first
    assert value == 7

def test_class_attributes_second():
    highvalue = HighValue(5, 1)
    value = highvalue.value_second
    assert value == 1

def test_high_value_attributes():
    highvalue = HighValue(5, 9)
    result = highvalue.get_highest()
    assert result == "Second value is higher"

def test_negative_attributes():
    highvalue = HighValue(5, -9)
    result = highvalue.get_highest()
    assert result == "First value is higher"

def test_equal_values():
    highvalue = HighValue(5, 5)
    result = highvalue.get_highest()
    assert result == "Values are equal"

def test_add_value_to_first():
    highvalue = HighValue(4, 8)
    highvalue.add(3, "first")
    result = highvalue.value_first
    assert result == 7

def test_add_value_to_second():
    highvalue = HighValue(5, 9)
    highvalue.add(5, "second")
    result = highvalue.value_second
    assert result == 14

def test_combined_add_first():
    highvalue = HighValue(5, 5)
    highvalue.add(5, "first")
    result = highvalue.get_highest()
    assert result == "First value is higher"

def test_combined_add_second():
    highvalue = HighValue(6, 3)
    highvalue.add(4, "second")
    result = highvalue.get_highest()
    assert result == "Second value is higher"

def test_using_negative_and_zero():
    highvalue = HighValue(0, 0)
    highvalue.add(-5, "second")
    result = highvalue.get_highest()
    assert result == "First value is higher"

def test_zero_as_argument():
    highvalue = HighValue(5, 5)
    highvalue.add(0, "second")
    result = highvalue.get_highest()
    assert result == "Values are equal"
