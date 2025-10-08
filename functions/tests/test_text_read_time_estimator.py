from lib.text_read_time_estimator import *

def test_200_words():
    result = text_read("word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word")
    assert result == "60 seconds"

def test_100_words():
    result = text_read("word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word")
    assert result == "30 seconds"


def test_50_words():
    result = text_read("word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word \
                word word word word word word word word word word")
    assert result == "15 seconds"