class WordCaseSeparator:
    def __init__(self):
        self._words = []

    def add_word(self, word):
        self._words.append(word)

    def upper_case_words(self):
        return [w for w in self._words if w and w[0].isupper()]

    def lower_case_words(self):
        return [w for w in self._words if w and not w[0].isupper()]

separator = WordCaseSeparator()
separator.add_word("Apple")
separator.add_word("banana")
separator.add_word("Cherry")
separator.add_word("date")
print(separator.upper_case_words())
print(separator.lower_case_words())
