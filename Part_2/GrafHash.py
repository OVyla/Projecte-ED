# -*- coding: utf-8 -*-
import copy
import math
import ElementData




class GrafHash:
    """
    OBJECTIU: Representar un graf dirigit o no dirigit amb nodes i arestes ponderades.
    RESPONSABILITAT: Proporcionar operacions per afegir, eliminar i manipular nodes i arestes,
                     així com explorar rutes i calcular pesos.
    """
    ###########################################################
    class Vertex:
        """
        OBJECTIU: Representar un node del graf.
        RESPONSABILITAT: Emmagatzemar la clau única i les dades associades a cada node.
        """
        __slots__ = ['_key', '_element_data']

        def __init__(self, key, element_data):
            """
            Inicialitza un node amb una clau i dades associades.
            - key: Identificador únic del node.
            - element_data: Instància d'ElementData que conté les dades del node.
            """
            self._key = key
            self._element_data = element_data

        def __repr__(self):
            """Retorna una representació formal del node."""
            return f"Vertex(key={self._key}, element_data={repr(self._element_data)})"

        def __eq__(self, other):
            """
            Compara dos nodes per la seva clau.
            """
            if not isinstance(other, GrafHash.Vertex):
                return NotImplemented
            return self._key == other._key

        def __hash__(self):
            """Permet que el node es pugui utilitzar com a clau en un diccionari."""
            return hash(self._key)
    
    ############################################################   
    __slots__ = ['__nodes', '__out', '__in', '__ponderat']

    def __init__(self, ln=[],lv=[],lp=[],digraf=True):
        """
        Inicialitza el graf.
        - ln: Llista de nodes inicials.
        - lv: Llista de valors associats als nodes.
        - lp: Llista de pesos de les arestes.
        - digraf: Indica si el graf és dirigit (True per defecte).
        """
        self.__nodes = {}
        self.__out = {}
        if digraf:
            self.__in={}
        self.__ponderat = True
    
    def es_digraf(self):
        """
        Retorna si el graf és dirigit o no.
        """
        return self.__in != None
        
    def insert_vertex(self, key, e: ElementData):
        """
        Afegeix un node al graf.
        - key: Identificador únic del node.
        - e: Dades associades al node (instància d'ElementData).
        """
        if not isinstance(e, ElementData.ElementData):
            raise TypeError
        v = self.Vertex(key, e)
        self.__nodes[key] = v
        self.__out[key] = {}
        if self.es_digraf():
            self.__in[key] = {}
        return v
    
    def get(self, key) -> ElementData:
        """
        Retorna el valor d'un node (objecte ElementData).
        """
        if key in self.__nodes:
            return self.__nodes[key]._element_data
        
    def insert_edge(self, n1, n2, p1=1):
        """
        Afegeix una aresta entre dos nodes.
        """
        self.__out[n1][n2] = p1
        self.__in[n2][n1] = p1
    
    def BFS(self, n1):
        """
        Realitza un recorregut en amplada (BFS) des d'un node inicial.
        Retorna un diccionari de nodes visitats amb el node previ com a valor.
        """
        if n1 not in self.__out:  # Comprovar si el node inicial existeix
            raise ValueError(f"El node {n1} no existeix al graf.")
        
        visitat = {n1: None}  # Diccionari de nodes visitats
        cua = [n1]  # Cua per BFS
        
        while cua:
            n = cua.pop(0)  # Extreure el primer node de la cua
            if n in self.__out:  # Comprovar si el node té veïns definits
                veins = list(self.__out[n].keys())
                for vei in veins:
                    if vei not in visitat:  # Si no s'ha visitat, afegir-lo
                        cua.append(vei)
                        visitat[vei] = n
        
        return visitat
        
        
    def camiMesCurt(self, n1, n2):
        """
        Troba el camí més curt entre dos nodes.
        Retorna la llista de nodes del camí més curt o None si no existeix.
        """
        visitat = self.BFS(n1)
        if n2 in visitat:
            n = visitat[n2]
            if n:
                path = [n2]
                while n != n1:
                    path.append(n)
                    n = visitat[n]
                path.append(n)
                path.reverse()
                return path
            else:
                return None
        else:
            return None
    
    def edges_out(self, x):
        """
        Retorna un iterador sobre els nodes sortints d'un node.
        """
        if x in self.__out:
            return iter(self.__out[x].keys())
        
    def edges_in(self, x):
        """
        Retorna un iterador sobre els nodes entrants d'un node.
        """
        if x in self.__nodes:
            return iter(self.__in[x].keys())
    
    def grauPesOut(self, x):
        """
        Retorna la suma dels pesos de les arestes sortints d'un node.
        """
        return sum(self.__out[x].values())
    
    def grauPesIn(self, x):
        """
        Retorna la suma dels pesos de les arestes entrants d'un node.
        """
        return sum(self.__in[x].values())
    
    def rank(self, node):
        """
        Retorna el rang d'un node com la suma dels pesos de les arestes entrants i sortints.
        """
        return self.grauPesIn(node) + self.grauPesOut(node)
    
    def next_videos(self, uuid):
        """
        Genera un iterador sobre els vídeos següents d'un node.
        """
        for nod_post, pes in self.__out[uuid].items():
            yield (nod_post, pes)
    
    def previous_videos(self, uuid):
        """
        Genera un iterador sobre els vídeos anteriors d'un node.
        """
        for nod_post, pes in self.__in[uuid].items():
            yield (nod_post, pes)
    
    def get_pes_aresta(self, uuid1, uuid2):
        """
        Retorna el pes de l'aresta entre dos nodes.
        """
        return self.__out[uuid1][uuid2]
    
    def augmentaPes(self, n1, n2):
        """
        Augmenta el pes de l'aresta entre dos nodes en 1.
        """
        self.__out[n1][n2] += 1
        self.__in[n2][n1] += 1
    
    def __repr__(self):
        """
        Retorna una representació formal del graf.
        """
        return f"GrafHash(nodes={len(self.__nodes)}, es_digraf={self.es_digraf()}, es_ponderat={self.__ponderat})"
    
    def __str__(self):
        """
        Retorna una representació en cadena del graf.
        """
        return f"GrafHash(nodes={len(self.__nodes)}, es_digraf={self.es_digraf()}, es_ponderat={self.__ponderat})"
    
    def __contains__(self, key):
        """
        Comprova si un node està en el graf.
        """
        return key in self.__nodes
    
    def _contains_file(self, file):
        """
        Comprova si un fitxer està contingut en el graf.
        """
        for uuid in self:  # Itera sobre els nodes
            if self.__nodes[uuid]._element_data.filename == file:  # Comprova si el fitxer coincideix
                return True
        return False
        
    def __len__(self):
        """
        Retorna el nombre de nodes en el graf.
        """
        return len(self.__nodes)
    
    def __iter__(self):
        """
        Permet la iteració sobre els nodes del graf.
        """
        return iter(self.__nodes.keys())
    
    def __getitem__(self, key):
        """
        Retorna les dades d'un node donat.
        """
        if key in self.__nodes:
            return self.__nodes[key]._element_data
    
    def __delitem__(self, key):
        """
        Elimina un node del graf.
        """
        if key in self.__nodes:  # Comprova si el node existeix
            del self.__nodes[key]  # Elimina el node del diccionari de nodes
            del self.__out[key]  # Elimina les arestes sortints associades
            if self.es_digraf():
                del self.__in[key]  # Elimina les arestes entrants associades si és un digraf
        else:
            raise KeyError(f"El node {key} no existeix en el graf.")
    
