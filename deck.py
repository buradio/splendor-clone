import random

class Card(object):
    """
    basic Card object.

    attributes:
        name: the name of the card
        isfacedown: boolean stating if the card is faced down; faced down cards' names are not shown in repr
    """
    def __init__(self,name,facedown=False):
        """construct a card from a string name. defaults face-up"""
        self.name = name
        self.isfacedown = facedown

    def __str__(self):
        if(self.isfacedown):
            return "card: face-down"
        else:
            return "card: " + self.name
    
    def __repr__(self):
        if(self.isfacedown):
            return "card: face-down"
        else:
            return "card: " + self.name

    def tofaceup(self):
        """forces the card into face-up state"""
        self.isfacedown=False
    def tofacedown(self):
        """forces the card into face-down state"""
        self.isfacedown=True
    def flip(self):
        self.isfacedown = not self.isfacedown

class Deck(object):
    """
    Deck is a pile of cards with ordered arrangement.

    attributes:
        deck: list of cards in the deck with 0 is the index of the top card.
    """
    def __init__(self,cards=None):
        """construct a Deck object with container containing Card objects as .deck"""
        if cards != None:
            self.deck = list(cards)
        else:
            cards = []
        
    def cards_in_deck(self):
        return len(self.deck)
    
    def add_card_totop(self,card):
        """add a card to the top of the deck, equivalent to insert_card(0,card)"""
        self.deck.insert(0,card)

    def add_card_tobottom(self,card):
        """add a card to the bottom of the deck"""
        self.deck.append(card)

    def add_cards_totop(self,cards):
        """add a pile of cards to the top of the deck"""
        self.deck = self.deck + list(cards)

    def add_cards_tobottom(self,cards):
        """add a pile of cards to the bottom of the deck"""
        self.deck = list(cards) + self.deck
        
    def insert_card(self,index,card):
        """insert a card to the deck, similar to list.insert"""
        self.deck.insert(index,card)

    def insert_card_random(self,card):
        """insert a card into a random place in the deck"""
        self.deck.insert(random.randint(0,len(self.deck)),card)
        
    def top_card(self):
        """returns the top card of the deck"""
        try:
            return self.deck[0]
        except:
            raise ValueError("top_card error") 
    
    def draw_card(self):
        """removes the top card from the deck and returns it"""
        try:
            card_drawn = self.deck.pop(0)
            return card_drawn
        except:
            raise ValueError("draw_card error")
        
    def shuffle(self):
        """shuffles the cards in the deck using random.shuffle"""
        random.shuffle(self.deck)
