import fsm
class InhabitantHandler:
    inhabitants = []

    def GetInhabitants(self):
        return self.inhabitants

#Gets all inhabitants at a given state
    def GetInhabitantsAt(self, state):
        temp = []
        for i in range(len(self.inhabitants)):
            if(type(self.inhabitants[i].state) == type(state)):
                temp.append(self.inhabitants[i])
        return temp
    
handler = InhabitantHandler()
