'''
Date : November 9, 2020

Deck of card class
'''

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return ' of '.join((self.value, self.suit))

class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in ['Hearts', 'Spades', 'Clubs', 'Diamonds'] for value in
        ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']]

    def shuffle(self):
        import random
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)

class Hand:
    def __init__(self, dealer = False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def addCard(self, card):
        self.cards.append(card)
    
    def cardValue(self):
        self.value = 0
        isAce = bool
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            elif card.value == 'Jack' or card.value == 'Queen' or card.value == 'King':
                self.value += 10
            else:
                if card.value == 'A':
                    isAce = True
                    self.value += 11
                else:
                    self.value += 1
            
        if isAce and self.value > 21:
            self.value -= 10

    
    def getValue(self):
        self.cardValue()
        return self.value

    def display(self):
        if self.dealer:
            print('Hidden')
            print(self.cards[1])
        else:
            for card in self.cards:
                print(card)
            print('Value:', self.getValue())

