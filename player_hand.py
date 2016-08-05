import random

class Player(object):
    def __init__(self,name):
        self.name = name
        self.hand = Hand()

class Hand(object):
    """
    Hand is a list of cards in a player's hand
    
    attributes:
        cards: list of cards in hand
    """
    
    def __init__(self,cards=None):
        """construct a Hand object from cards"""
        if cards != None:
            self.cards = list(cards)
        else:
            self.cards = []
    def number_of_cards(self):
        """returns total number of cards in hand"""
        return len(self.cards)
    def add_card(self,card):
        """add a card to hand"""
        self.cards.append(card)
    def shuffle(self):
        """shuffle cards in hand"""
        random.shuffle(self.cards)
    def discard_index(self,index):
        """remove the card of the index from hand.cards and returns it"""
        discarding = self.pop(index)
        return discarding
    def discard(self,card):
        """remove the specified card of the hand and returns it, return None if there are no cards of specified type in the hand"""
        if card in self.cards:
            ret = card
            self.cards.remove(card)
            return ret
        else:
            return None
    def discard_random(self):
        """remove a random card from the hand and returns it"""
        discarding = self.pop(random.randint(0,len(cards)))
        return discarding
