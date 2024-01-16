import random

class Card:

    card_rank = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    card_suit = ['Spades', 'Clubs', 'Hearts', 'Diamonds']

    def __init__(self, rank: int = 0, suit: int = 0, weight: int = 0):
        self.rank = rank
        self.suit = suit
        self.weight = weight
    
    def __repr__(self):
        card_print = f'{self.card_rank[self.rank]} of {self.card_suit[self.suit]}'
        return card_print
    
    def rank(self, card_rank):
        return card_rank
    
    def suit(self, card_suit):
        return card_suit

    def sign(self):
        if self.suit == 'Spades':
            return u"\u2660"
        if self.suit == 'Clubs':
            return u'\u2663'
        if self.suit == 'Hearts':
            return u'\u2665'
        if self.suit == 'Diamonds':
            return u'\u2666'
    
    def weight(self, rank):
        for i, card_rank in enumerate(self.rank(), start=1):
            if card_rank == rank:
                return i
        


class Deck:

    def __init__(self, deck: list = []):
        self.deck = deck
    
    def deck_creation(self):
        self.deck = []
        for rank in range(2, 15):
            for suit in range(4):
                self.deck.append(Card(rank, suit, rank))
        random.shuffle(self.deck)

    def shufle(self):
        random.shuffle(self.deck)

    def take_top(self):
        t_card = self.deck.pop(0)
        print(t_card)
        return t_card
    
    def take_bottom(self):
        b_card = self.deck.pop(len(self.deck)-1)
        print(b_card)
        return b_card

    def take_random(self):
        r_number = random.randint(0, 52)
        r_card = self.deck.pop(r_number)
        print(r_card)
        return r_card

    def card_weight_check_all(self):
        for card in self.deck:
            print(f'{card} - {card.weight}\n')
        
    def card_suit_check(self, card1: Card, card2: Card):
        if card1.suit == card2.suit:
            return True
        else:
            False
    
    def card_weight_check(self, card1: Card, card2: Card):
        if card1.weight == card2.weight:
            check = 0
        elif card1.weight > card2.weight:
            check = card1
        else:
            check = card2
        return check

    def card_weight_modifier(self, suit, value):
        for card in deck.deck:
            if card.suit == suit:
                card.weight += value


class Player:
    
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck, count):
        self.hand.extend(deck.cards[:count])
        del deck.cards[:count]

    def play_card(self, table, card):
        if card in self.hand:
            table.append(card)
            self.hand.remove(card)
            return True
        else:
            return False
             
    def choose_card_to_play(self, table, trump):
        playable_cards = self.get_playable_cards(table, trump)

        if playable_cards:
            better_cards = [card for card in playable_cards if card.rank > table[-1].rank and card.suit == table[-1].suit]
            if better_cards:
                return max(better_cards, key=lambda card: self.get_card_rank(card))
            return min(playable_cards, key=lambda card: self.get_card_rank(card))
        else:
            return min(self.hand, key=lambda card: self.get_card_rank(card))


class GameLogic():

    def __init__(self, players_count):
        self.players_count = players_count
        self.players = [Player(f"Player {i+1}") for i in range(players_count)]
        self.deck = Deck()
        self.deck.shuffle()
        self.table = []
        self.trump = None

    def deal_cards(self, count):
        for player in self.players:
            player.draw(self.deck, count)

    def start_game(self):
        self.deal_cards(6)
        self.trump = self.deck.cards.pop(0)
        self.table.append(self.trump)

    def play_round(self):
        for player in self.players:
            card_to_play = self.choose_card_to_play(player)
            player.play_card(self.table, card_to_play)

    def play_round(self):
        for player in self.players:
            card_to_play = self.choose_card_to_play(player)
            if card_to_play is not None:
                player.play_card(self.table, card_to_play)


class Computer1():

    def __init__(self):
        pass

deck = Deck()
deck.deck_creation()
print(deck.deck)
deck.take_top()
deck.take_bottom()
deck.take_random()
deck.card_weight_check_all()



# Kortų kaladė
# Korta: Objektas (Class)
# def __init__
# def rank (2-9, T, J, Q, K, A)
# def suit (spades, clubs, hearts, diamonds)
# def sign (suit + rank)
# def weight
# Kortų kaladė: Objektas (Class)
# def deck - kortų sąrašas []
# def shuffle
# def take from top
# def take from bottom
# def take random
# Mąstom apie žaidimą