import random

import numpy as np
from numpy import double

from AprendPackage.modelos import Estado
from AprendPackage.memoria.MemoriaAprend import MemoriaAprend
from AprendPackage.selecao_accao.SelAccao import SelAccao


class EGreedy(SelAccao):

    def __init__(self, mem_aprend: MemoriaAprend, accoes, epsilon: double):
        super().__init__(mem_aprend)
        self.accoes = accoes
        self.epsilon = epsilon

    def max_accao(self, s: Estado):
        random.shuffle(self.accoes)

        idx_otimo = 0
        for idx, a in enumerate(self.accoes):
            if self.mem_aprend.Q(s,a) > self.mem_aprend.Q(s,self.accoes[idx_otimo]):
                idx_otimo = idx
        return self.accoes[idx_otimo]

    def aproveitar(self, s: Estado):
        return self.max_accao(s)

    def explorar(self):
        return random.choice(self.accoes)

    def selecionar_accao(self, s: Estado):
        if random.random() > self.epsilon:
            accao = self.aproveitar(s)
        else:
            accao = self.explorar()

        print("ACCAO ESCOLHIDA ", accao.accao)
        return accao

