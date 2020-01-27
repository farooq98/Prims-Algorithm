#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class DGraph:
    def __init__(self, vertex):
        self.v = vertex
        self.adjacentMatrix = [[0 for i in range(self.v)] for j in range(self.v)]

    def AddEdges(self, src, dest, cost):
        if src == dest:
            print("Source and destination are same")
        else:
            self.adjacentMatrix[src][dest] = cost
            self.adjacentMatrix[dest][src] = cost

    def getNeighbours(self, source):
        lst = []
        for i in range(len(self.adjacentMatrix[source])):
            if self.adjacentMatrix[source][i] > 0:
                lst.append(i)
        return lst
    
    def weight(self,src,dest):
        return self.adjacentMatrix[src][dest]
    
    def prims(self,source):
        
        #dct2 = {}
        #for i in range(len(self.adjacentMatrix)):
        #    temp = {}
        #    x = self.getNeighbours(i)
        #    for j in x:
        #        temp[j] = self.adjacentMatrix[i][j]
        #    dct2[i] = temp
        #print(dct2)
        
        visited = []
        dct = {i:9999999 for i in range(len(self.adjacentMatrix))}
        dct[source] = 0
        #print(dct)
        answer = {}
        
        temp = {i:dct[i] for i in dct}
        
        #for i in range(len(self.adjacentMatrix)):
        
        while temp:    
            min = 9999999
            minNode = None
            for i in temp:
                if temp[i] < min:
                    min = temp[i]
                    minNode = i
            #print("MinNode:",minNode)
            temp.pop(minNode)
            #print("Temp: ",temp)
            
            
            
            #minNode = None
            #for node in dct:
            #    if minNode is None:
            #        minNode = node
            #    elif dct[node] < dct[minNode]:
            #        minNode = node    
            
            if minNode not in visited:
                visited.append(minNode)
                
                x = self.getNeighbours(minNode)
                for j in x:
                    #print(self.weight(minNode,j) , dct[j])
                    #print(self.weight(minNode,j) < dct[j])
                    if self.weight(minNode,j) < dct[j] and (j not in visited):
                        dct[j] = self.weight(minNode,j)
                        temp[j] = self.weight(minNode,j)
                #answer = {j: dct[j]} 
                #dct.pop(minNode)        
            
                    
                #print("Dct:",dct)
        print("Cost: ",sum(dct.values()))
            
        print(visited)

g = DGraph(9)
g.AddEdges(0, 1, 4)
g.AddEdges(0, 7, 8)
g.AddEdges(1, 2, 8)
g.AddEdges(1, 7, 11)
g.AddEdges(7, 8, 7)
g.AddEdges(7, 6, 1)
g.AddEdges(2, 8, 2)
g.AddEdges(2, 5, 4)
g.AddEdges(2, 3, 7)
g.AddEdges(8, 6, 6)
g.AddEdges(6, 5, 2)
g.AddEdges(5, 4, 10)
g.AddEdges(5, 3, 14)
g.AddEdges(3, 4, 9)
g.prims(0)

