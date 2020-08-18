# Xiao Hu and Yujie (Lydia) Li

from cards import *
import unittest

class Test_Cards(unittest.TestCase):
    def setUp(self):
        self.card1=Card('q','h')
        self.deck1=Deck()

    def test_init_card(self):
        self.assertEqual(self.card1.r,'Q','init ranks')
        self.assertEqual(self.card1.s,'H','init suit')

    def test_get_rank(self):
        self.assertEqual(self.card1.get_rank(),'Q','get rank')

    def test_get_suit(self):
        self.assertEqual(self.card1.get_suit(),'H','get suit')

    def test_str_card(self):
        self.assertEqual(str(self.card1),'QH','print card')

    def test_init_deck(self):
        self.assertTrue('AH' in self.deck1.get_deck(),'init deck')
        self.assertEqual(52,len(self.deck1.get_deck()),'init deck length')

    #def test_shuffle(self):
        #No need to test shuffle functions

    #def test_get_deck(self):
        #No need to test since already tested in __init__

    def test_deal(self):
        self.assertEqual('KD',self.deck1.deal(),'deal card')

    def test_str_deck(self):
        self.assertEqual(52,len(str(self.deck1).split()),'print deck')
        self.assertTrue('2D' in str(self.deck1),'print 2D')

unittest.main()
