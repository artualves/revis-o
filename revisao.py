from abc import ABC, abstractmethod, ABCMeta
from typing import List
from armas import *
from golpes import *

class Jogador():
    energia: float
    armas: List[Arma]

    def __init__(self):
        self.energia = 150
        self.armas : List[Arma] = []

    def atirar(self, d: Disparavel, j):
        d.disparar(j)

    def bater(self, j, g: Golpe = None, a: Arma = None):
        if g == None and a != None:
            a.agredir(j)
        elif a == None and g != None:
            g.golpear(j)
    
    def municiar(self, d: Disparavel):
        d.recarregar()

    def __str__(self):
        return f'Energia: {self.energia}'