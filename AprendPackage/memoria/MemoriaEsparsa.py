from numpy import double

from AprendPackage.modelos.Accao import Accao
from AprendPackage.modelos.Estado import Estado
from AprendPackage.memoria.MemoriaAprend import MemoriaAprend
from AprendPackage.memoria.MemoriaAssociativa import MemoriaAssociativa


class MemoriaEsparsa(MemoriaAprend):

    def __init__(self, valor_omissao=0.0):
        self.valor_omissao = valor_omissao
        self.memoria = MemoriaAssociativa().memoria

    def Q(self, s: Estado, a: Accao):
        return self.memoria.get((s, a), self.valor_omissao)

    def actualizar(self, s: Estado, a: Accao, q: double):
        self.memoria[(s, a)] = q
