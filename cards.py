# Xiao Hu and Yujie (Lydia) Li

import random  # needed for shuffling a Deck

class Card(object):
   
    def __init__(self, r, s):
        self.r=r.upper()
        self.s=s.upper()

    def __str__(self):
        return self.r+self.s

    def get_rank(self):
        '''return the rank of a card'''
        return self.r

    def get_suit(self):
        '''return the suit of a card'''
        return self.s

class Deck():
    '''Denote a deck to play cards with'''
    
    def __init__(self):
        '''Initialize deck as a list of all 52 cards:
           13 cards in each of 4 suits'''
        self.__deck = []
        lst_suit=['S','C','H','D']
        lst_rank=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        for i in lst_suit:
            for j in lst_rank:
                card=Card(j,i)
                self.__deck.append(card)

    def shuffle(self):
        '''Shuffle the deck'''
        random.shuffle(self.__deck)

    def get_deck(self):
        '''return a list of the whole deck'''
        card_deck=[]
        for i in self.__deck:
            card_deck.append(str(i))
        return card_deck

    def deal(self):
        '''get the last card in the deck'''
        # simulates a pile of cards and getting the top one
        s=self.__deck[-1]          
        self.__deck.pop()           
        return str(s)
    
    def __str__(self):
        '''Represent the whole deck as a string for printing -- very useful during code development'''
       #the deck is a list of cards
       #this function just calls str(card) for each card in list
       # put a '\n' between them
        s=[]
        for i in self.__deck:
            s.append(str(i)+'\n')
        return ''.join(s)
            
            
