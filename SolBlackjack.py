# Xiao Hu and Yujie (Lydia) Li

import cards

class BlackJack(object):
    def __init__(self):
        self.row1 = [1, 2, 3, 4, 5]
        self.row2 = [6, 7, 8, 9, 10]
        self.row3 = [11, 12, 13]
        self.row4 = [14, 15, 16]
        self.table = {'row1': self.row1, 'row2': self.row2, 'row3': self.row3, 'row4': self.row4}
        self.discardList = [17, 18, 19, 20]
        self.dealt=[]

    def DisplayInitial(self):
        '''Display the initial state of the game'''
        print "Welcome to Blackjack Solitaire!!\nThe initial state of the 16 grid spots are:"
        print "row1= ",self.table['row1']
        print "row2= ",self.table['row2']
        print "row3= ",self.table['row3']
        print "row4= ",self.table['row4']
        print "And the initial state of the 4 discard spots are:"
        print "discardList= ",self.discardList
        print "\n"

    def placeCard(self, position):
        '''Place the dealt card into the position the player entered'''
        if position<6:
            self.row1[position-1]=self.dealt
        elif position<11:
            self.row2[position-6]=self.dealt
        elif position<14:
            self.row3[position-11]=self.dealt
        elif position<17:
            self.row4[position-14]=self.dealt
        else:
            self.discardList[position-17]=self.dealt
    
    def errorCheck(self, position):
        '''Check the potential error in the player's input'''
        if not position.isdigit():
            return 1
        elif not 1<=int(position)<=20:
            return 2
        elif not int(position) in (self.row1+self.row2+self.row3+self.row4+self.discardList):
            return 3
        
    def checkGameEnd(self, i):            #i would equal to the number of dealt cards 
        '''Check if all the 16 girds have been filled'''
        if i==15 and self.discardList==[17, 18, 19, 20]:
            return 1
        elif i==16 and len(filter(lambda x:type(x)==int,self.discardList))==3:  #count the number of cards in discard spots
            return 1
        elif i==17 and len(filter(lambda x:type(x)==int,self.discardList))==2:
            return 1
        elif i==18 and len(filter(lambda x:type(x)==int,self.discardList))==1:
            return 1
        else:
            return 0

    def gameDisplay(self):
        '''Display the state of the game'''
        print "\n\nNow the state of the 16 grid spots are:"
        print "row1= ",self.table['row1']
        print "row2= ",self.table['row2']
        print "row3= ",self.table['row3']
        print "row4= ",self.table['row4']
        print "And now of the 4 discard spots are:"
        print "discardList= ",self.discardList
        print "\n"

    def handToPoint(self,handnum):
        '''convert the hand, except Blackjack, into point, this function would be useful in scoresOneHand(lst)'''
        dictscore={21:7,20:5,19:4,18:3,17:2}
        if handnum<=16:
            return 1
        elif handnum>=22:
            return 0
        else:
            return dictscore[handnum]
        
    def scoresOneHand(self,lst):
        '''this function scores one hand, would be useful in scoresTable()'''
        ranklist=map(lambda x: x[0] if len(x)==2 else x[:2],lst)      #delete suits, create a list with only ranks
        for i in range(0,len(ranklist)):                              #Set cards 'K' 'J' 'Q' to '10'
            if ranklist[i] in ['K','J','Q']:
                ranklist[i]='10'
            elif ranklist[i]=='A':                                    #Set cards 'A' to '1'
                ranklist[i]='1'
        ranklist=map(int,ranklist)                                    #convert ['int'] into [int]
        ###scores a hand with only 2 cards    
        if len(ranklist)==2:                  
            if 1 in ranklist:
                #scores 2 cards that contain ace
                if 10 in ranklist:            #scores the Blackjack
                    return 10
                else:                         
                    return self.handToPoint(sum(ranklist)+10)  #ace+10 would make the score higher in this senario
            else:  #scores 2 cards without ace
                return self.handToPoint(sum(ranklist))

        ###scores a hand with 3,4 or 5 cards
        else:
            if 1 in ranklist: #scores a hand that contains ace
                sum_ace1=sum(ranklist)        #calculate the hand if all aces count for 1
                sum_ace11=sum_ace1+10         #calculate the hand if an ace counts for 11
                return max(self.handToPoint(sum_ace1),self.handToPoint(sum_ace11))
            else:   #scores a hand without ace
                return self.handToPoint(sum(ranklist))

    def scoresTable(self):
        '''this function scores the entire table by calling scoresOneHand(lst) nine times'''
        hand1=self.row1                       #the list of hands
        hand2=self.row2
        hand3=self.row3
        hand4=self.row4
        hand5=[self.row1[0], self.row2[0]]
        hand6=[self.row1[1], self.row2[1], self.row3[0], self.row4[0]]
        hand7=[self.row1[2], self.row2[2], self.row3[1], self.row4[1]]
        hand8=[self.row1[3], self.row2[3], self.row3[2], self.row4[2]]
        hand9=[self.row1[4], self.row2[4]]
        firstHand=self.scoresOneHand(hand1)        #scores each hand
        secondHand=self.scoresOneHand(hand2)
        thirdHand=self.scoresOneHand(hand3)
        fourthHand=self.scoresOneHand(hand4)
        fifthHand=self.scoresOneHand(hand5)
        sixthHand=self.scoresOneHand(hand6)
        seventhHand=self.scoresOneHand(hand7)
        eighthHand=self.scoresOneHand(hand8)
        ninthHand=self.scoresOneHand(hand9)
        totalScore=firstHand+secondHand+thirdHand+fourthHand+fifthHand+sixthHand+seventhHand+eighthHand+ninthHand
        return totalScore                     #calculate the sum of 9 hands

    def compareHigh(self,score):
        '''compare the score of table with the highest score in file'''
        f=open("highScore.txt",'rU')
        highest=f.read(2)
        if score>int(highest):
            print "Congratulation! You get the highest score in the system's record!"
            f.close()
            f=open("highScore.txt",'w')
            f.write(str(score))
        f.close()
                    

    def play(self):
        '''the play function, includes the entire process of the game'''
        self.DisplayInitial()  #Display the initial state of the game
        deck=cards.Deck()
        deck.shuffle()         #Shuffle deck

        ###loop now until all 16 grids are filled###
        for i in range(0,20):
            print "Next, you are given a card, the dealt card is:"
            self.dealt=deck.deal()        #Deal a card
            print self.dealt
            position=raw_input("\nNotice that the 16 grid spots and 4 discard spots are numbered 1-20.\nPlease enter the position number you want to place the dealt:")
            while self.errorCheck(position):   #Check input error
                if self.errorCheck(position)==1:
                    print "The input is not an integer, please check!"
                elif self.errorCheck(position)==2:
                    print "The input is an out of range number, please check!"
                elif self.errorCheck(position)==3:
                    print "That number of spot already has a card!"
                position=raw_input("Please enter the position number again:") 
            self.placeCard(int(position))      #Place the card dealt
            self.gameDisplay()            #Display the game
            if self.checkGameEnd(i):
               break

        ###end of the game, now going to score###
        print "The tableau was full!! Now the system is scoring the hands..."
        scoreOfGame=self.scoresTable()
        print "Your total score is:"
        print scoreOfGame

        ###In the end, compare the score with the score in highScore.txt
        self.compareHigh(scoreOfGame)
        print "The game is over!"


def main():
    '''the main function'''
    bj_solitaire=BlackJack()
    bj_solitaire.play()

if __name__=='__main__':
    main()
        
        

        
        

        
        
            
        
        
        
        
        
