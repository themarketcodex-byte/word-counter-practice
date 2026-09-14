import unittest

from word_count import count_words


class TestCountWords(unittest.TestCase):
    def test_counts_total_words(self):
        total, _ = count_words("the quick brown fox jumps over the lazy dog")
        self.assertEqual(total, 9)

    def test_finds_most_common_word(self):
        _, top_words = count_words("cat dog cat bird cat dog")
        self.assertEqual(top_words[0], ("cat", 3))

    def test_empty_string(self):
        total, top_words = count_words("")
        self.assertEqual(total, 0)
        self.assertEqual(top_words, [])


if __name__ == "__main__":
    unittest.main()
