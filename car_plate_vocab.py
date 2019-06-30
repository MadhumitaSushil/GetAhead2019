import math
from collections import Counter

"""
Car Plates Vocabulary 
We need to find the shortest word from a vocabulary that includes all the letters from a given licence plate. The shorter the word, the better. The licence plates start with two or three letters, then they are followed by 5 characters, from which at most 2 are letters, the rest are digits.

Write a solution that will find the shortest words for 1000 licence plates. 

You are given a vocabulary containing all valid words. 

Keep duplicate letters
Ordering is irrelevant
Case is irrelevant
The vocabulary is sorted lexicographically
The vocabulary contains about 4 million entries


Example: 

For the licence plate RT 123SO the shortest word would be SORT:

for RC 10014 the shortest word would be CAR.
 
"""


class Lexicon:
    def __init__(self, dictionary: list):
        self.lexicon = dictionary

    def get_idx(self, item, char_only_match=False, cased=False):
        """
        O(logn) item search using binary search.
        Since the lexicon has 4 million entries sorted in lexicographic order,
        binary search is efficient.
        :param item: item to search for in the lexicon
        :param char_only_match: if True, match only the starting character instead of complete sequence
        :param cased: True if cases are distinct.
        :return: index of items starting with char
        """

        if not cased:
            item = item.lower()

        if char_only_match:
            item = item[0]

        i = 0
        j = len(self.lexicon) - 1

        while i <= j:
            mid = math.floor((i + j) / 2)

            if not cased:
                lexicon_item = self.lexicon[mid].lower()
            else:
                lexicon_item = self.lexicon[mid]

            if char_only_match:
                lexicon_item = lexicon_item[0]

            if lexicon_item < item:
                i = mid + 1
            elif lexicon_item > item:
                j = mid - 1
            else:
                return mid

        return -1

    def __len__(self):
        return len(self.lexicon)

    def __getitem__(self, item):
        return self.lexicon[item]


class SmallestMatch:
    def __init__(self, seq, lexicon, cased=False):
        self.seq_counter = Counter(self.get_alpha(seq, cased))
        self.lexicon = lexicon

    def get_alpha(self, seq, cased) -> str:
        """
        :param seq: Alphanumeric sequence
        :return: Alphabetical subset of a sequence
        """
        alpha_str = ''
        for char in seq:
            if char.isalpha():
                alpha_str += char

        if not cased:
            alpha_str = alpha_str.lower()

        return alpha_str

    def _find_matching_entry(self, start_letters):
        """
        binary search over lexicon to find words with different start letter options.
        Iterate until a match is found, i.e., a lexicon item contains all characters of carplate seq.
        Return matching minimum length words as the right word
        :param start_letters: Characters that the matching word can start with
        :return: matching word
        """

        min_len = 0
        word = ""

        for cur_char in start_letters:

            lexicon_idx = self.lexicon.get_idx(cur_char, char_only_match=True)
            if lexicon_idx == -1:
                continue

            if min_len == 0 or len(self.lexicon[lexicon_idx]) < min_len:
                next_char_idx = self.lexicon.get_idx(chr(ord(cur_char) + 1), char_only_match=True)
                if next_char_idx == -1:
                    next_char_idx = len(self.lexicon)

                for idx in range(lexicon_idx, next_char_idx):
                    if len(self.seq_counter - Counter(self.lexicon[lexicon_idx].lower())) == 0:
                        min_len = len(self.lexicon[lexicon_idx])
                        word = self.lexicon[lexicon_idx]
                        break

        return word

    def get_nearest_word(self):

        # find matching lexicon item for words that start with letters in the carplate
        word = self._find_matching_entry(self.seq_counter.keys())

        if len(word) == 0:
            # case that the word starts with a letter not present in the carplate vocab
            ascii = 'abcdefghijklmnopqrstuvwxyz'  # assuming words are made of these letters
            remaining = ascii - self.seq_counter.keys()
            word = self._find_matching_entry(remaining)

        print(word)
        return word


if __name__ == '__main__':

    lexicon = Lexicon(['Art', 'caR', 'SORT'])
    carplate1 = SmallestMatch("RT 123SO", lexicon)
    carplate2 = SmallestMatch("RC 10014", lexicon)
    carplate3 = SmallestMatch("RT 10014", lexicon)

    assert 'SORT' == carplate1.get_nearest_word()
    assert 'caR' == carplate2.get_nearest_word()
    assert 'Art' == carplate3.get_nearest_word()








