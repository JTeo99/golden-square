from lib.diary_entry import DiaryEntry

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

'''