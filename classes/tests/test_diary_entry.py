from lib.diary_entry import DiaryEntry
import pytest

'''
Given a title and contents
#format returns a formatted entry, like:
"My Title: These are the contents"
'''

def test_formats_with_title_and_contents():
    diary_entry = DiaryEntry("My Title", "Some Contents")
    result = diary_entry.format()
    assert result == "My Title: Some Contents"

'''
given a title and contents
#count_words returns an integer that is the number of words in the diary entry
'''

def test_counts_words_in_diary_entry():
    diary_entry = DiaryEntry("My Title", "Some Contents")
    result = diary_entry.count_words()
    assert result == 4

'''
given an empty title and contents
raises error
'''
def test_errors_on_empty_title_and_contents():
    with pytest.raises(Exception) as e:
        DiaryEntry("","")
    assert str(e.value) == "Diary entries must have a title or contents"
