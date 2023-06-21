#class needs to have a capital first leter- if the class is multiple words you still need _
class Autommbile():
    #define a constructor
    #the constructor defines what happens when we create an automobule
    def __init__(self, make, model, vin, engine_size, owner):
        #assign parameter values
        self.make = make
        self.model = model
        self.vin = vin
        self.engine_size = engine_size
        self.ower = owner
        #the self means for one specific atomobile
        
