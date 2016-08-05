import deck
import splendorcard
from splendorplayer import *

def loadcards(filename):
    t = []
    infile = open(filename)
    for line in infile:
        t.append(splendorcard.load_card_data("",line.split(",")[1:]))

    print("loaded "+str(len(t))+" cards from "+filename)
    return t

class gamelogic:
    def __init__(self,number_of_players):
        #initialize players
        self.player = []
        for i in range(number_of_players):
            self.player.append(Splendor_player("Player "+ str(i+1) ))
        print("initialized " + str(number_of_players) + " players")
            
        #initialize decks
        #tier1 deck
        self.t1deck = deck.Deck()
        self.t1deck.add_cards_totop(loadcards("asset\\level1.csv"))
        self.t1inplay = []
        #tier2 deck
        self.t2deck = deck.Deck()
        self.t2deck.add_cards_totop(loadcards("asset\\level2.csv"))
        self.t2inplay = []
        #tier3 deck
        self.t3deck = deck.Deck()
        self.t3deck.add_cards_totop(loadcards("asset\\level3.csv"))
        self.t3inplay = []

        #initialize token pool
        self.token_pool = Token_pool(7,7,7,7,7)

        #initialize nobles
        self.nobles = [None]*number_of_players
        for i in range(number_of_players):
            #randomize nobles
            pass

        #current_turn
        self.current_turn = 0
