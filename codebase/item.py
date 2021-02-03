class Item(object):
    def __init__(self, name, cost, itype):
        self.name = name
        self.cost = cost
        self.itype = itype
    def __str__(self):
       return "%20s: %3d cfoot (%s)" % \
            (self.name, self.cost, self.itype)
    def getName(self):
        return self.name
    def getCost(self):
        return self.cost
    def getItemType(self):
        return self.itype
    def setCost(self, cost):
        self.cost = cost