import player_hand as pl

def gem_l2d(l):
    d = {}
    d['red'] = l[0]
    d['green'] = l[1]
    d['black'] = l[2]
    d['blue'] = l[3]
    d['white'] = l[4]
    return d

class Token_pool:
    def __init__(self,red=0,blue=0,green=0,black=0,white=0):
        self.red = 0
        self.blue = 0
        self.green = 0
        self.black = 0
        self.white = 0

    def add_tokens(self,red=0,blue=0,green=0,black=0,white=0):
        self.red+=red
        self.blue+=blue
        self.green+=green
        self.black+=black
        self.white+=white

    def remove_tokens(self,red=0,blue=0,green=0,black=0,white=0):
        self.red-=red
        self.blue-=blue
        self.green-=green
        self.black-=black
        self.white-=white

    def aslist(self):
        return [self.red,self.green,self.black,self.blue,self.white]

class Splendor_player(pl.Player):
    def __init__(self,name):
        super(Splendor_player,self).__init__(name)
        self.tokens = Token_pool()
        self.victorypoints = 0

    def passive_tokens(self):
        """returns the player's passive gem bonuses as list"""
        temp = [0]*5
        for card in self.hand.cards:
            temp[card.bonus_type_asid]+=1
        return temp

    def total_tokens(self):
        """returns the player's total gems as list"""
        t = self.tokens.aslist()
        p = self.passive_tokens()
        total = [0]*5
        for i in range(5):
            total[i] = t[i] + p[i]
        return total
            
        
    
        
