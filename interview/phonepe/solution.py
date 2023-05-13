from abc import ABC, abstractmethod
from collections import defaultdict
class OperationInterface(ABC):
    
    @abstractmethod
    def startTracking(self, id, tags):
        pass
        
    @abstractmethod
    def stopTracking(self, id):
        pass
    
    @abstractmethod
    def getCounts(self, tags):
        pass
        
class Entity:
    def __init__(self, id, tag):
        self.id = id
        self.tag = tag
        self.isBeingTracked = False
        
class PendencySystem(OperationInterface):
    def __init__(self):
        self.entityList = []
        self.tagEntityMap = defaultdict(list)
        
    def createEntity(self, id, tag):
        entity = Entity(id, tag)
        self.entityList.append(entity)
        self.tagEntityMap[tag].append(entity)
        return entity
    
    def startTracking(self, id, tags):
        for tag in tags:
            if tag in self.tagEntityMap:
                entityList = self.tagEntityMap[tag]
                entityIds = [e.id for e in entityList]
                if id not in entityIds:
                    entity = self.createEntity(id, tag)
                    entity.isBeingTracked = True
            else:
                entity = self.createEntity(id, tag)
                entity.isBeingTracked = True
                        
    def stopTracking(self, id):
        for entity in self.entityList:
            if entity.id == id and entity.isBeingTracked:
                entity.isBeingTracked = False
                
    def getCounts(self, tags):
        tagCountMap = defaultdict(int)
        for tag in tags:
            if tag in self.tagEntityMap:
                entityList = self.tagEntityMap[tag]
                for entity in entityList:
                    if entity.isBeingTracked:
                        tagCountMap[tag] += 1
        # print tagCountMap
        maxCount = 0
        maxTag = ''
        for tag in tagCountMap:
            if tagCountMap[tag] > maxCount:
                maxCount = tagCountMap[tag]
                maxTag = tag
        res = 0
        for tag in tagCountMap:
            if tag != maxTag:
                res = maxCount - tagCountMap[tag]
        print (res if res else maxCount)
        
ps = PendencySystem()
ps.startTracking(1112, ["UPI", "Karnataka", "Bangalore"])
ps.startTracking(2451, ["UPI", "Karnataka", "Mysore"])
ps.startTracking(3421, ["UPI", "Rajasthan", "Jaipur"])
ps.startTracking(1221, ["Wallet", "Karnataka", "Bangalore"])

ps.getCounts(["UPI"])
ps.getCounts(["UPI", "Karnataka"])
ps.getCounts(["UPI", "Karnataka", "Bangalore"])

ps.getCounts(["Bangalore"])

ps.startTracking(4221, ["Wallet", "Karnataka", "Bangalore"])
ps.stopTracking(1112)
ps.stopTracking(2451)

ps.getCounts(["UPI"])
ps.getCounts(["Wallet"])
ps.getCounts(["UPI", "Karnataka", "Bangalore"])
