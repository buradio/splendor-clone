import deck
import splendorcard
from splendorplayer import *

class gamelogic:
    def __init__(self,number_of_players):
        #initialize players
        self.player = []
        for i in range(number_of_players):
            self.player.append(Splendor_player("Player "+ str(i+1) ))
            
        #initialize decks
        #tier1
        self.t1deck = deck.Deck()
        #tier2
        self.t2deck = deck.Deck()
        #tier3
        self.t3deck = deck.Deck()

        #initialize token pool
        self.token_pool = Token_pool(7,7,7,7,7)

        #initialize nobles
        self.nobles = [None]*number_of_players
        for i in range(number_of_players):
            #randomize nobles
            pass

        #current_turn
        self.current_turn = 0
