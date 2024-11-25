import random

from AprendPackage.modelos.Experiencia import Experiencia


class MemoriaExperiencia:
    def __init__(self, dim_max:int):
        self.dim_max = dim_max
        self.memoria = []


    def actualizar(self, e:Experiencia):

        if len(self.memoria) == self.dim_max:
            self.memoria.remove(self.memoria[0])
        self.memoria.append(e)


    def amostrar(self, n:int):
        n_amostras = min(n, len(self.memoria))
        return random.sample(self.memoria, n_amostras)

