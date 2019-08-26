import unittest
import word_ladder_class

class TestWordLadder(unittest.TestCase):

    def test_wordladder_same(self):
        word_game = word_ladder_class.WordLadder()
        self.assertEqual(word_game.same('gien','gold'), 1)

    def test_wordladder_start(self):
        pass

if __name__ == '__main__':
    unittest.main()