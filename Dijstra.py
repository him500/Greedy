from heapq import heappush,heappop,heapify
from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.V=v
        self.g=defaultdict(list)

    def addEdge(self,src,dest,weight):
        self.g[src].append([weight,dest])
        self.g[dest].append([weight,src])

    def put(self,heapmin,child,initd=0):
        for i in range(len(heapmin)):
            if heapmin[i][1]==child[1] and heapmin[i][0]>(child[0]+initd):
                heapmin[i][0]=child[0]+initd
                break;    

    def dijkstra(self,src):
        visited=[False]*self.V
        heapmin=[]
        for node in range(self.V):
            if node==src:
                heapmin.append([0,node])
            else:    
                heapmin.append([float("Inf"),node])

        for child in self.g[src]:
            self.put(heapmin,child)

        visited[src]=True
        heapify(heapmin)
        # print("this is heapmin ",heapmin)
        
        while not all(visited):
            # self.print_heap(heapmin)
            # print("loop"," ",visited)
            dump=[]
            dump.append(heappop(heapmin))
            # print(dump)
            # print("check",dump[-1][1])
            if visited[dump[-1][1]]==True:
                while (visited[dump[-1][1]]==True):
                    dump.append(heappop(heapmin))

            [srcdist,src]=dump[-1] #new src here

            while dump:
                elem=dump.pop()
                heappush(heapmin,elem)
            del dump

            for child in self.g[src]:
                if visited[child[1]]==False:
                    self.put(heapmin,child,srcdist)

            visited[src]=True
            heapify(heapmin)
        self.print_heap(heapmin)

    def print_heap(self,heapmin):
        p=[0]*self.V

        for i in range(len(heapmin)):
            p[heapmin[i][1]]=heapmin[i][0]
        print("vertex","distance")
        for i in range(len(p)):
            print(i," ",p[i])


graph = Graph(9) 
graph.addEdge(0, 1, 4) 
graph.addEdge(0, 7, 8) 
graph.addEdge(1, 2, 8) 
graph.addEdge(1, 7, 11) 
graph.addEdge(2, 3, 7) 
graph.addEdge(2, 8, 2) 
graph.addEdge(2, 5, 4) 
graph.addEdge(3, 4, 9) 
graph.addEdge(3, 5, 14) 
graph.addEdge(4, 5, 10) 
graph.addEdge(5, 6, 2) 
graph.addEdge(6, 7, 1) 
graph.addEdge(6, 8, 6) 
graph.addEdge(7, 8, 7) 
graph.dijkstra(0) 