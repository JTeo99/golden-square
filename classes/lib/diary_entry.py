import math

class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("Diary entries must have a title or contents")
        self._title = title
        self._contents = contents
        self._read_so_far = 0

    def format(self):
        return f"{self._title}: {self._contents}"

    def count_words(self):
        words = self.format().split()
        return len(words)


    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("wpm cannot be 0")
        counted_words = self._contents.split()
        reading_speed = len(counted_words) / wpm
        return math.ceil(reading_speed)

    def reading_chunk(self, wpm, minutes):
        readable = wpm * minutes
        words = self._contents.split()
        if self._read_so_far >= len(words):
            self._read_so_far = 0
        chunk_beginning = self._read_so_far
        chunk_ending = self._read_so_far + readable
        chunk_words = words[chunk_beginning: chunk_ending]
        self._read_so_far = chunk_ending
        return " ".join(chunk_words)
