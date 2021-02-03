class Item(object):
    def __init__(self, scenario, consq, exp, cfoot):
        self.scenario = scenario
        self.consq = consq
        self.exp = exp
        self.cfoot = cfoot
   
    def getScenario(self):
        return self.scenario
    def getConsq(self):
        return self.consq
    def getExp(self):
        return self.exp
    def getCarbonFoot(self):
        return self.cfoot