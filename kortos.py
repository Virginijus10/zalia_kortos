import random

class Card:

    def __init__(self, suit: str = '', weight: int = 0, color: str = '', rank: str = ''):
        self.suit = suit
        self.weight = weight
        self.color = color
        self.rank = rank 
        

    def rank(self.2-9, T, J, Q, K, A):
        pass

    def suit(self.spades, clubs, hearts, diamonds):
        pass

    def sign(self.suit, rank):
        pass

    def set_weight(self):
        if self.valid.rank():
            if self.rank.isdigit():
                self.weight = int(self.rank)
            elif self.rank == 'T':
                self.weight = 10
            elif self.weight == ['J', 'Q', 'K']:
                self.weight = 10
            elif self.weight == 'A':
                self.weight = 11
            else:
               self.weight = 0
        else:
            self.weight = 0
        
    def get_rank(self):
        return self.rank

    def get_weight(self):
        return self.weight
       


class Deck:

    def __inir__(self, deck: list = []):
        self.deck = deck

    def shufle(self):
        random.shuffle(self.deck)

    def take_top(self):
        pass
    
    def take_bottom(self):
        pass

    def take_random(self):
        r_card = random.randint(1, 52)
        pass

class GameLogic():

    def __init__(self):
        pass

class Computer1():

    def __init__(self):
        pass



    def forkinimas(self):
      pass


# Kortų kaladė
# Korta: Objektas (Class)
# def rank (2-9, T, J, Q, K, A)
# def suit (spades, clubs, hearts, diamonds)
# def sign (suit + rank)
# def weight
# Kortų kaladė: Objektas (Class)
# def cards - kortų sąrašas []
# def shuffle
# def take from top
# def take from bottom
# def take random
# Mąstom apie žaidimą
