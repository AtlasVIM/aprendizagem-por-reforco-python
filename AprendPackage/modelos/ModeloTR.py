import random


class ModeloTR:
    def __init__(self):
        self.T = {}
        self.R = {}

    def atualizar(self,s,a,r,sn):
        self.T[(s,a)] = sn #Modelo Determinista
        self.R[(s,a)] = r

    def amostrar(self):
        s,a = random.choice(list(self.T.keys()))
        sn = self.T[(s,a)]
        r = self.R[(s,a)]
        return s,a,r,sn

