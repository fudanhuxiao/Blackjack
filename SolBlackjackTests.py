# Xiao Hu and Yujie (Lydia) Li

from SolBlackjack import *
import unittest

class Test_Blackjack(unittest.TestCase):
    def setUp(self):
        self.newBlackJack=BlackJack()
        

    def test_init(self):
        self.assertEqual([1,2,3,4,5],self.newBlackJack.row1,'init row 1')
        self.assertEqual(list,type(self.newBlackJack.table.values()[1]),'init table')
        self.assertEqual(4,len(self.newBlackJack.table.keys()),'init table keys')
        self.assertFalse(self.newBlackJack.table.has_key('row5'),'init table keys dne')
        self.assertTrue(self.newBlackJack.table.has_key('row3'),'init table keys exits')
        self.assertEqual(4,len(self.newBlackJack.discardList),'init discard')
        self.assertEqual(0,len(self.newBlackJack.dealt),'init dealt')

    # DisplayInitial not tested, since it simply prints the game status

    def test_placeCard(self):
        self.newBlackJack.dealt='KD'
        self.newBlackJack.placeCard(5)
        self.assertEqual('KD',self.newBlackJack.row1[4],'place the dealt card-row 1')
        self.newBlackJack.placeCard(11)
        self.assertEqual('KD',self.newBlackJack.row3[0],'place the dealt-row 3')
        self.newBlackJack.placeCard(18)
        self.assertEqual('KD',self.newBlackJack.discardList[1],'discard the dealt')
        self.assertRaises(IndexError,self.newBlackJack.placeCard,21)

    def test_errorCheck(self):
        self.assertTrue(self.newBlackJack.errorCheck('a'),'errorCheck non-integer')
        self.assertTrue(self.newBlackJack.errorCheck('1.8'),'errorCheck non-integer')
        self.assertTrue(self.newBlackJack.errorCheck('21'),'errorCheck >20')
        self.newBlackJack.dealt='KD'
        self.newBlackJack.placeCard(5)
        self.assertTrue(self.newBlackJack.errorCheck('5'),'errorCheck spot taken')
        self.assertFalse(self.newBlackJack.errorCheck('6'),'errorCheck no error')

    def test_checkGameEnd(self):
        self.newBlackJack.discardList=[17,18,19,20]
        self.assertEqual(1,self.newBlackJack.checkGameEnd(15),'table filled, no card discarded, game should end')
        self.newBlackJack.discardList=['AH',18,19,20]
        self.assertEqual(1,self.newBlackJack.checkGameEnd(16),'table filled, one card discarded, game should end')
        self.newBlackJack.discardList=['AH',18,'KD',20]
        self.assertEqual(1,self.newBlackJack.checkGameEnd(17),'table filled, two cards discarded, game should end')
        self.newBlackJack.discardList=['AH',18,'KD','1S']
        self.assertEqual(1,self.newBlackJack.checkGameEnd(18),'table filled, three cards discarded, game should end')
        self.assertEqual(0,self.newBlackJack.checkGameEnd(15),'discarded almost, yet table not filled')
        self.assertEqual(0,self.newBlackJack.checkGameEnd(10),'table not filled')

    # gameDisplay not tested, since it only prints

    def test_handToPoint(self):
        self.assertEqual(5,self.newBlackJack.handToPoint(20),'hand to points, almost There')
        self.assertEqual(1,self.newBlackJack.handToPoint(16),'hand to points, lowerlimit')
        self.assertEqual(0,self.newBlackJack.handToPoint(22),'hand to points, lowest')

    def test_scoresOneHand(self):
        self.assertEqual(10,self.newBlackJack.scoresOneHand(['AH','KQ']),'Black Jack!')
        self.assertEqual(5,self.newBlackJack.scoresOneHand(['9S','AD']),'2-card hand, w/ one Ace')
        self.assertEqual(1,self.newBlackJack.scoresOneHand(['AS','AD']),'2-card hand, w/ two Aces, one 1 one 11')
        self.assertEqual(5,self.newBlackJack.scoresOneHand(['JS','10S']),'2-card hand, w/o Ace')
        self.assertEqual(1,self.newBlackJack.scoresOneHand(['AD','5H','6S']),'3+card-hand w/ one Ace,scores 1 or 0 pt depending on Ace value')
        self.assertEqual(3,self.newBlackJack.scoresOneHand(['2S','2H','2D','AH','AC']),'3+card-hand w/ two Aces,one 1 one 11')
        self.assertEqual(5,self.newBlackJack.scoresOneHand(['AS','2H','AD','AH','5C']),'3+card-hand w/ three Aces,two 1 one 11')
        self.assertEqual(4,self.newBlackJack.scoresOneHand(['AS','AH','AD','AC','5C']),'3+card-hand w/ Four Aces,three 1 one 11')
        self.assertEqual(7,self.newBlackJack.scoresOneHand(['3S','3C','6H','9D']),'3+card-hand w/o Ace')

    def test_scoresTable(self):
        self.newBlackJack.row1=['AS','2S','3S','5S','JS']
        self.newBlackJack.row2=['10S','4S','3C','3D','AC']
        self.newBlackJack.row3=['QS','AD','10D']
        self.newBlackJack.row4=['5D','4D','3H']
        self.assertEqual( 63,self.newBlackJack.scoresTable(),'scoring the table')

    #compareHigh is not tested, since it only reads and prints or writes after comparison.
    #play() is not tested followed the instruction on piazza. 
        
unittest.main()
