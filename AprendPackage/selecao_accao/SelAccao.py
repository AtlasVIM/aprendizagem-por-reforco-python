from abc import abstractmethod

from AprendPackage.modelos import Estado
from AprendPackage.modelos.Accao import Accao
from AprendPackage.memoria.MemoriaAprend import MemoriaAprend


class SelAccao():
    def __init__(self, mem_aprend: MemoriaAprend):
        self.mem_aprend = mem_aprend

    @abstractmethod
    def selecionar_accao(self, s: Estado) -> Accao:
        pass

    @abstractmethod
    def max_accao(self, s: Estado) -> Accao:
        pass