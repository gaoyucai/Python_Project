# Author:GaoYuCai
import heapq
class PrioityQueue:
    def __init__(self):
        self._queue=[]
        self._index=0
    def push(self,item,prioity):
        heapq.heappush(self._queue,(-prioity,self._index,item))
        self._index+=1
    def pop(self):
        return heapq.heappop(self._queue)[-1]
class Item:
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return "Item{!r})".format(self.name)
q=PrioityQueue()
q.push(Item("foo"),1)
q.push(Item("bar"),5)
q.push(Item("spam"),4)
q.push(Item("grok"),1)
print(q.pop())