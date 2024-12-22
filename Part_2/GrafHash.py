# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 15:39:10 2019

@author: gemma
"""
import copy
import math
import ElementData




class GrafHash:

    class Vertex:

        __slots__ = ['_key', '_element_data']

        def __init__(self, key, element_data):
            self._key = key
            self._element_data = element_data

        def __repr__(self):
            return f"Vertex(key={self._key}, element_data={repr(self._element_data)})"

        def __eq__(self, other):
            if not isinstance(other, GrafHash.Vertex):
                return NotImplemented
            return self._key == other._key

        def __hash__(self):
            return hash(self._key)
    
################################Definicio Class _Vertex       
    __slots__ = ['_nodes', '_out', '_in', '_ponderat']

    def __init__(self, ln=[],lv=[],lp=[],digraf=False):
        """Crea graf (no dirigit per defecte, digraf si dirigit es True.
        """
        self._nodes = {}
        self._out = { }
        self._in={} if digraf else self._out
        #nodes={}
        for n in ln:
            v=self.insert_vertex(n)
            #nodes[n]=v
        if lp==[]:
            self._ponderat=False
            for v in lv:
                self.insert_edge(v[0],v[1])
        else:
            self._ponderat=True
            for vA,pA in zip(lv,lp):
                self.insert_edge(vA[0],vA[1],pA)
    
    def es_digraf(self):
        return self._out!=self._in
    
    def getOut(self):
        return self._out
        
    def insert_vertex(self, key, e: ElementData):
        v= self.Vertex(key, e)
        self._nodes[key] = v
        self._out[key] = { }
        if self.es_digraf():
            self._in[key] = {}
        return v
    
    def get(self, key) -> ElementData:
        if key in self._nodes:
            return self._nodes[key]._element_data
        else:
            return None
        
    def __contains__(self, key):
        return key in self._nodes
    
    def __len__(self):
        return len(self._nodes)
    
    def __iter__(self):
        return iter(self._nodes.values())
    
    def __getitem__(self, key):
        return self._nodes[key]
    
    def __delitem__(self, key):
        if key in self._nodes:
            del self._nodes[key]
            del self._out[key]
            if self.es_digraf():
                del self._in[key]
        else:
            raise KeyError(f"El node {key} no existeix en el graf.")
    
    def __repr__(self):
        return f"GrafHash(nodes={self._nodes}, es_digraf={self.es_digraf()}, es_ponderat={self._ponderat()})"

    def insert_edge(self, n1, n2, p1=1):
        
        self._out[n1][n2] = p1
        self._in[n2][n1] = p1
        
    def grauOut(self, x):
        return len(self._out[x])

    def grauIn(self, x):
        return len(self._in[x])
    
    def vertices(self):
        """Return una iteracio de tots els vertexs del graf."""
        return self._nodes.__iter__( )

    def edges(self,x):
        """Return una iteracio de tots els nodes veins de sortida de x al graf."""
        #return self._out[x].items()
        return iter(self._out[x].__iter__())
    
    def camins(self, n1,n2):
        
        if n1 in self._out and n2 in self._in:
            if len(self._out[n1])> 0 and len(self._in[n2])> 0:
                visited = { }
                paths = []
                lpathsRes = []
                self.totsCaminsFins(n1, n2, visited, paths, lpathsRes)       
        return lpathsRes
        
    
    def totsCaminsFins(self,n1,n2,visited,paths,lpathsRes):
        visited[n1] = True
        paths.append(n1)
        
        if n1 == n2:
            #paths.append(n1)
            print(paths)
            lpathsRes.append(copy.deepcopy(paths))
        else:
            for vei in self._out[n1]:
                if vei not in visited:
                    self.totsCaminsFins(vei, n2, visited, paths, lpathsRes) 
        paths.pop()
        del visited[n1]

    def DFS(self, nInicial):
        visitat = {nInicial:None}
        recorregut = [nInicial]
        if nInicial in self._nodes:
            if len(self._out[nInicial]) != 0:
                self.DFSRec(nInicial, visitat, recorregut)
        return visitat, recorregut
            
            
    def DFSRec(self, n1, visitat, recorregut):
        for vei in self._out[n1]:
            if vei not in visitat:
                recorregut.append(vei)
                visitat[vei] = n1
                self.DFSRec(vei, visitat, recorregut)
    
    def BFS(self, n1):
        visitat = {n1:None}
        cua = [n1]
        while cua:
            n = cua.pop(0)
            for vei in self._out[n]:
                if vei not in visitat:
                    cua.append(vei)
                    visitat[vei] = n
        return visitat
    
    def minDistance(self, dist, visitat):
        min = math.inf
        min_index = None
        for node,distancia in dist.items():
            if distancia < min and node not in visitat:
                min = distancia
                min_index = node
        return min_index

    def dijkstra(self, n):
        if n not in self._nodes:
            raise ValueError(f"El nodo {n} no existe en el grafo.")

        dist = {}  
        anterior = {}  
        visitat = [] 

        for vertex in self._nodes:
            dist[vertex] = math.inf  
            anterior[vertex] = None  
        dist[n] = 0

        for i in range(len(self._nodes)):
            u = self.minDistance(dist, visitat)
            if u is None:  
                break
            visitat.append(u) 

            for vertex in self._out[u]:  
                if vertex not in visitat:  
                    nueva_dist = dist[u] + self._out[u][vertex]  
                    if nueva_dist < dist[vertex]:  
                        dist[vertex] = nueva_dist
                        anterior[vertex] = u  

        anterior.pop(n, None)

        return dist, anterior
        
    def dijkstraModif(self,n1,n2):
        dist, anterior = self.dijkstra(n1)
        cami = []
        actual = n2

        while actual is not None:
            cami.insert(0, actual)  
            actual = anterior[actual]

        
        if cami[0] != n1:
            return None  

        return cami

    def camiMesCurt(self, n1, n2):
        dist, anterior = self.dijkstra(n1)

        cami = []
        actual = n2
        while actual is not None: 
            cami.insert(0, actual)
            actual = anterior.get(actual)  

        if cami[0] != n1:
            raise ValueError(f"No hi ha cami entre {n1} i {n2}")

        return cami
    
    
    
    def __str__(self):
        cad="===============GRAF===================\n"
     
        for it in self._out.items():
            cad1="__________________________________________________________________________________\n"
            cad1=cad1+str(it[0])+" : "
            for valor in it[1].items():
                cad1=cad1+str(str(valor[0])+"("+ str(valor[1])+")"+" , " )
                            
            cad = cad + cad1 + "\n"
        
        return cad
    
