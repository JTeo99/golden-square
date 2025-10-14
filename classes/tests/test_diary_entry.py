from lib.diary_entry import DiaryEntry
import pytest

'''
given an empty title
raises error
'''
def test_errors_on_empty_title():
    with pytest.raises(Exception) as e:
        DiaryEntry("","My Contents")
    assert str(e.value) == "Diary entries must have a title or contents"



'''
given an empty contents
raises error
'''
def test_errors_on_empty_contents():
    with pytest.raises(Exception) as e:
        DiaryEntry("My Title","")
    assert str(e.value) == "Diary entries must have a title or contents"



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
given a contents and a reading speed in wpm
#reading_time returns an integer with an estimation of the reading time of the contents
'''

def test_reading_speed_for_2_words_and_2_wpm():
    diary_entry = DiaryEntry("My Title", "Some Contents")
    result = diary_entry.reading_time(2)
    assert result == 1



'''
given a wpm of 2 and a text of 4 words
#reading_time returns 2
'''

def test_reading_speed_for_2_words_and_2_wpm():
    diary_entry = DiaryEntry("My Title", "Even Some More Contents")
    result = diary_entry.reading_time(2)
    assert result == 2



'''
given a wpm of 2 and a text of 3 words
#reading_time returns 2 minutes
'''

def test_reading_speed_for_2_words_and_2_wpm():
    diary_entry = DiaryEntry("My Title", "Even More Contents")
    result = diary_entry.reading_time(2)
    assert result == 2



'''
Given a wpm of 0
#reading_time raises an error
'''
def test_reading_time_wpm_is_0():
    diary_entry = DiaryEntry("My Title", "Even More Contents")
    with pytest.raises(Exception) as e:
        diary_entry.reading_time(0)
    assert str(e.value) == "wpm cannot be 0"
        


'''
Given a contents of nine words
And a wpm of 2
And 2 minutes
#reading_chunk returns the first 4 words
'''
def test_reading_chunk_with_2_wpm_and_two_minutes():
    diary_entry = DiaryEntry("My Title", "Even More amazing contents that really are extremely interesting")
    result = diary_entry.reading_chunk(2, 2)
    assert result == "Even More amazing contents"



'''

'''
'''
Given a contents of nine words
And a wpm of 2
And 1 minutes
#reading_chunk returns the first 4 words
'''
def test_reading_chunk_with_2_wpm_and_one_minute():
    diary_entry = DiaryEntry("My Title", "Even More amazing contents that really are extremely interesting")
    result = diary_entry.reading_chunk(2, 1)
    assert result == "Even More"



'''
Given a contents of nine words
and a wpm of 2 
and 1 minutes
#reading_chunk returns "Even More"
next time, "amazing contents"
'''
def test_reading_chunk_with_two_wpm_and_one_minute_called_twice():
    diary_entry = DiaryEntry("My Title", "Even More amazing contents that really are extremely interesting")
    assert diary_entry.reading_chunk(2, 1) == "Even More"
    assert diary_entry.reading_chunk(2, 1) == "amazing contents"



'''
Given a contents of nine words
#reading_chunk called multiple times with different wpm
#reading_chunk returns "Even More"
next time, "amazing contents"
'''
def test_reading_chunk_with_two_wpm_and_one_minute_called_twice():
    diary_entry = DiaryEntry("My Title", "Even More amazing contents that really are extremely interesting")
    assert diary_entry.reading_chunk(3, 2) == "Even More amazing contents that really"
    assert diary_entry.reading_chunk(2, 2) == "are extremely interesting"
    assert diary_entry.reading_chunk(1, 3) == "Even More amazing"



'''
Given a contents of nine words
#reading_chunk called multiple times with different wpm to get exact contents
'''
def test_reading_chunk_with_two_wpm_and_one_minute_called_twice():
    diary_entry = DiaryEntry("My Title", "Even More amazing contents that really are extremely interesting")
    assert diary_entry.reading_chunk(3, 2) == "Even More amazing contents that really"
    assert diary_entry.reading_chunk(1, 3) == "are extremely interesting"
    assert diary_entry.reading_chunk(1, 3) == "Even More amazing"