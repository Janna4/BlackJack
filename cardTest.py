import unittest
from card import Card

#class CardTestCase(unittest.TestCase):
#    """I'm still figuring this out :')"""
#    def test_something(self):
#        self.assertEqual(True, False)

class CardTest(unittest.TestCase):
    def test_name(self):
        c = Card('king', 'spades')
        c.set_visible(True)
        assert c.get_name() == 'king'

    def test_suit(self):
        c = Card('king', 'spades')
        c.set_visible(True)
        assert c.get_suit() == 'spades'

    def test_hard_value(self):
        c = Card('ace', 'spades')
        c.set_visible(True)
        assert c.get_hard_value() == 11

    def test_soft_value(self):
        c = Card('ace', 'spades')
        c.set_visible(True)
        assert c.get_soft_value() == 1

    def test_color(self):
        c = Card('king', 'spades')
        c.set_visible(True)
        assert c.get_color() == 'black'

    def test_flip(self):
        c = Card('king', 'spades')
        c.flip()
        assert c.get_visibility() == True

    def test_hidden_name(self):
        c = Card('king', 'spades')
        assert c.get_name() == "unknown"

    def test_hidden_suit(self):
        c = Card('king', 'spades')
        assert c.get_suit() == "unknown"

    def test_hidden_color(self):
        c = Card('king', 'spades')
        assert c.get_color() == "unknown"

    def test_hidden_hard_value(self):
        c = Card('king', 'spades')
        assert c.get_hard_value() == "unknown"

    def test_hidden_soft_value(self):
        c = Card('king', 'spades')
        assert c.get_soft_value() == "unknown"

if __name__ == '__main__':
    unittest.main()
