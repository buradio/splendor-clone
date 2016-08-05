import deck

class CostData:
    def __init__(self,red_cost,green_cost,black_cost,blue_cost,white_cost):
        self.red_cost = red_cost
        self.green_cost = green_cost
        self.black_cost = black_cost
        self.blue_cost = blue_cost
        self.white_cost = white_cost
    def aslist(self):
        """returns list of costs ordered [red,green,black,blue,white]"""
        return [self.red_cost,self.green_cost,self.black_cost,self.blue_cost,self.white_cost]
    def asdict(self):
        """returns a dictionary with key "color" paired with cost e.g. "blue":blue_cost"""
        return {"red":red_cost,"green":green_cost,"blue":blue_cost,"black":black_cost,"white":white_cost}


        
class Splendor_card(deck.Card):
    def __init__(self,name,costdata,bonus_type,victory_points=0):
        super(Splendor_card,self).__init__(name)
        self.cost = costdata
        self.bonus_type = bonus_type
        self.victory_points = victory_points

    def bonus_type_asid(self):
        return ["red","green","black","blue","white"].index(self.bonus_type)
