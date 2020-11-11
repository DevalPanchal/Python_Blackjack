from Cards import Deck
from Cards import Card
from Cards import Hand

class Game:
    '''
    Blackjack Game class
    '''
    def __init__(self):
        pass

    def play(self):
        '''
        Blackjack gameplay mechanics
        '''
        playing = True
        
        while playing:
            self.deck = Deck()
            self.deck.shuffle()

            self.playerHand = Hand()
            self.dealerHand = Hand(dealer = True)


            # deal cards to players
            for i in range(2):
                self.dealerHand.addCard(self.deck.deal())
                self.playerHand.addCard(self.deck.deal())

            # Show player their hand
            print("\nYour hand is:")
            self.playerHand.display()

            print('\n')

            # Show dealer their hand
            print("Dealer hand is:")
            self.dealerHand.display()

            gameOver = False

            while not gameOver:
                playerHasBlackJack, dealerHasBlackJack = self.checkBlackJack()

                # check if player or dealer hand Blackjack
                if playerHasBlackJack or dealerHasBlackJack:
                    gameOver = True
                    continue
                
                # Prompt player to stay or hit
                choice = input("Do you want to [stay or hit]? ")

                # Keep prompting player if they put wrong input to continue
                while choice not in ['h', 's', 'hit', 'stay']:
                    choice = input('Do you want to [stay or hit]? ')
                
                # If player chooses to hit then deal a card to them
                if choice in ['h', 'hit']:
                    self.playerHand.addCard(self.deck.deal())
                    self.playerHand.display()
                
                # If players card value is greater than 21 then they bust and game ends
                if self.playerIsOver():
                    print('You Bust!')
                    gameOver = True
                    playing = False
                else:
                    # show values of player and dealer cards
                    playerHandValue = self.playerHand.getValue()
                    dealerHandValue = self.dealerHand.getValue()

                    # Show final results
                    print('\n-----Final Result-----')
                    print('You hand:', playerHandValue)
                    print('Dealer Hand:', dealerHandValue)

                    # if player card value is greater than dealer card value
                    if playerHandValue > dealerHandValue:
                        # is player card value is greater than dealer card value then player wins
                        print("Congratulations, You Win!")
                        gameOver = True
                        playing = False
                    # if player card value is equal to dealer hand value then both tie
                    elif playerHandValue == dealerHandValue:
                        print('Tie!')
                        gameOver = True
                        playing = False
                    # otherwise the dealer wins
                    else:
                        print('Dealer Wins!\n')
                        gameOver = True
                        playing = False
                    gameOver = True
    
    def checkBlackJack(self):
        '''
        check if player has blackjack
        '''
        player = False
        dealer = False

        if self.playerHand.getValue() == 21:
            player = True
        if self.dealerHand.getValue() == 21:
            dealer = True

        return player, dealer
    
    def playerIsOver(self):
        '''
        check if playerHand is greater than 21
        '''
        return self.playerHand.getValue() > 21

if __name__ == "__main__":
    print("Welcome to blackjack!")
    print("The goal is for you beat the dealer by getting a count as close to 21 as possible, without going over 21.")
    print("You can choose to either stay at your current value or hit to try your luck on getting blackjack.")
    print("Good luck!")
    game = Game()
    game.play()   