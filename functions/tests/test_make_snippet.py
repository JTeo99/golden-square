from lib.make_snippet import *

'''
Function wants to take a string as an argument and return the first
five words and add ... to the end if there is more than that
'''

'''
Testing for strings longer than 5 characters
'''
def test_snippet_is_longer_than_five():
    result = make_snippet("This string is longer than 5 characters")
    assert result == "This string is longer than..."

'''
Testing for strings shorter than 5 characters
'''
def test_snippet_is_shorter_than_five():
    result = make_snippet("This is a string")
    assert result == "This is a string"

'''
Testing for 5 words
'''
def test_5_word_str():
    result = make_snippet("This is a  nice string")
    assert result == "This is a nice string..."