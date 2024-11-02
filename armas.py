from abc import ABC, abstractmethod, ABCMeta
from golpes import *

class Arma(ABC):
    destruicao: float

    def __init__(self, d):
        self.destruicao = d

    def agredir(self, j):
        j.energia -= 5

    def __str__(self):
        return f'Poder de destruição: {self.destruicao}'

class Faca(Arma):
    lamina: int

    def __init__(self):
        self.lamina = 10
        self.destruicao = 15

    def agredir(self, j):
        if (self.lamina > 0):
            j.energia -= self.destruicao
            self.lamina -= 1
        else:
            super().agredir(j)
        
class Soco_Ingles(Faca, Soco):
    def agredir(self, j):
        super().agredir(j)
        self.golpear(j)

class Disparavel(metaclass=ABCMeta):
    def __init__(self):
        pass
    
    @abstractmethod
    def disparar(self, j):
        pass

    @abstractmethod
    def recarregar(self):
        pass

class Revolver(Arma, Disparavel):
    cartuchos: int

    def __init__(self):
        self.destruicao = 20
        self.cartuchos = 6

    def recarregar(self):
        self.cartuchos = 6

    def disparar(self, j):
        if self.cartuchos > 0:
            self.cartuchos -= 1
            j.energia -= self.destruicao
        else:
            self.recarregar()

class Lanca_Chamas(Arma, Disparavel):
    gas: float

    def __init__(self):
        self.gas = 100.0
        self.destruicao = 30

    def recarregar(self):
        self.gas = 100.0

    def disparar(self, j):
        if self.gas > 0:
            self.gas -= 5.5
            j.energia -= self.destruicao
        else:
            self.recarregar()