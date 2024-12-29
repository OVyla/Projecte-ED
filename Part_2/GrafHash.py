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
    __slots__ = ['_nodes', '_out', '_in', '_ponderat']

    def __init__(self, ln=[],lv=[],lp=[],digraf=True):
        """Crea graf (no dirigit per defecte, digraf si dirigit es True.
        """
        self._nodes = {}
        self._out = {}
        if digraf:
            self._in={}
        self._ponderat = True
    
    def es_digraf(self):
        return self._in != None
        
    def insert_vertex(self, key, e: ElementData):
        if not isinstance(e, ElementData.ElementData):
            raise TypeError
        v = self.Vertex(key, e)
        self._nodes[key] = v
        self._out[key] = {}
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
    
    def _contains_file(self, file):
        for uuid in self:
            if self._nodes[uuid]._element_data.filename == file:
                return True
        return False
        
    def __len__(self):
        return len(self._nodes)
    
    def __iter__(self):
        return iter(self._nodes.keys())
    
    def __getitem__(self, key):
        if key in self._nodes:
            return self._nodes[key]._element_data
    
    def __delitem__(self, key):
        if key in self._nodes:
            del self._nodes[key]
            del self._out[key]
            if self.es_digraf():
                del self._in[key]
        else:
            raise KeyError(f"El node {key} no existeix en el graf.")
    
    def __repr__(self):
        return f"GrafHash(nodes={len(self._nodes)}, es_digraf={self.es_digraf()}, es_ponderat={self._ponderat})"

    def insert_edge(self, n1, n2, p1=1):
        self._out[n1][n2] = p1
        self._in[n2][n1] = p1
    
    def BFS(self, n1):
        visitat = {n1:None}
        cua = [n1]
        while cua:
            n = cua.pop(0)
            for vei in self._out[n].keys():
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
        if x in self._out:
            return iter(self._out[x].keys())
        
    def edges_in(self, x):
        if x in self._nodes:
            return iter(self._in[x].keys())
    
    def grauPesOut(self, x):
        return sum(self._out[x].values())
    
    def grauPesIn(self, x):
        return sum(self._in[x].values())
    
    def rank(self, node):
        return self.grauPesIn(node) + self.grauPesOut(node)
    
    def next_videos(self, uuid):
        for nod_post, pes in self._out[uuid].items():
            yield (nod_post, pes)
    
    def previous_videos(self, uuid):
        for nod_post, pes in self._in[uuid].items():
            yield (nod_post, pes)
    
    def get_pes_aresta(self, uuid1, uuid2):
        return self._out[uuid1][uuid2]
    
    def augmentaPes(self, n1, n2):
        self._out[n1][n2] += 1
        self._in[n2][n1] += 1
    
    def __str__(self):
        cad="===============GRAF===================\n"
     
        for it in self._out.items():
            cad1="__________________________________________________________________________________\n"
            cad1=cad1+str(it[0])+" : "
            for valor in it[1].items():
                cad1=cad1+str(str(valor[0])+"("+ str(valor[1])+")"+" , " )
                            
            cad = cad + cad1 + "\n"
        
        return cad
    
