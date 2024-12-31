# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 15:39:10 2019

@author: gemma
"""
import copy
import math
import ElementData




class GrafHash:
    ###########################################################
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
    
    ############################################################   
    __slots__ = ['__nodes', '__out', '__in', '__ponderat']

    def __init__(self, ln=[],lv=[],lp=[],digraf=True):
        """Crea graf (no dirigit per defecte, digraf si dirigit es True.
        """
        self.__nodes = {}
        self.__out = {}
        if digraf:
            self.__in={}
        self.__ponderat = True
    
    def es_digraf(self):
        return self.__in != None
        
    def insert_vertex(self, key, e: ElementData):
        if not isinstance(e, ElementData.ElementData):
            raise TypeError
        v = self.Vertex(key, e)
        self.__nodes[key] = v
        self.__out[key] = {}
        if self.es_digraf():
            self.__in[key] = {}
        return v
    
    def get(self, key) -> ElementData:
        if key in self.__nodes:
            return self.__nodes[key]._element_data
        
    def __contains__(self, key):
        return key in self.__nodes
    
    def _contains_file(self, file):
        for uuid in self:
            if self.__nodes[uuid]._element_data.filename == file:
                return True
        return False
        
    def __len__(self):
        return len(self.__nodes)
    
    def __iter__(self):
        return iter(self.__nodes.keys())
    
    def __getitem__(self, key):
        if key in self.__nodes:
            return self.__nodes[key]._element_data
    
    def __delitem__(self, key):
        if key in self.__nodes:
            del self.__nodes[key]
            del self.__out[key]
            if self.es_digraf():
                del self.__in[key]
        else:
            raise KeyError(f"El node {key} no existeix en el graf.")
    
    def __repr__(self):
        return f"GrafHash(nodes={len(self.__nodes)}, es_digraf={self.es_digraf()}, es_ponderat={self.__ponderat})"

    def insert_edge(self, n1, n2, p1=1):
        self.__out[n1][n2] = p1
        self.__in[n2][n1] = p1
    
    def BFS(self, n1):
        visitat = {n1:None}
        cua = [n1]
        while cua:
            n = cua.pop(0)
            for vei in self.__out[n].keys():
                if vei not in visitat:
                    cua.append(vei)
                    visitat[vei] = n
        return visitat
    
    def camiMesCurt(self, n1, n2):
        visitat = self.BFS(n1)
        n = visitat[n2]
        path = [n2]
        while n != n1:
            path.append(n)
            n = visitat[n]
        path.append(n)
        path.reverse()
        return path
    
    def edges_out(self, x):
        if x in self.__out:
            return iter(self.__out[x].keys())
        
    def edges_in(self, x):
        if x in self.__nodes:
            return iter(self.__in[x].keys())
    
    def grauPesOut(self, x):
        return sum(self.__out[x].values())
    
    def grauPesIn(self, x):
        return sum(self.__in[x].values())
    
    def rank(self, node):
        return self.grauPesIn(node) + self.grauPesOut(node)
    
    def next_videos(self, uuid):
        for nod_post, pes in self.__out[uuid].items():
            yield (nod_post, pes)
    
    def previous_videos(self, uuid):
        for nod_post, pes in self.__in[uuid].items():
            yield (nod_post, pes)
    
    def get_pes_aresta(self, uuid1, uuid2):
        return self.__out[uuid1][uuid2]
    
    def augmentaPes(self, n1, n2):
        self.__out[n1][n2] += 1
        self.__in[n2][n1] += 1
    
    def __str__(self):
        cad="===============GRAF===================\n"
     
        for it in self.__out.items():
            cad1="__________________________________________________________________________________\n"
            cad1=cad1+str(it[0])+" : "
            for valor in it[1].items():
                cad1=cad1+str(str(valor[0])+"("+ str(valor[1])+")"+" , " )
                            
            cad = cad + cad1 + "\n"
        
        return cad
    
