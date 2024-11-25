from abc import abstractmethod

from numpy import double

from AprendPackage.modelos.Accao import Accao
from AprendPackage.modelos.Estado import Estado


class Aprendizagem:

    @abstractmethod
    def selecionar_accao(self, s) -> Accao:
        pass

    @abstractmethod
    def aprender(self, s: Estado, a: Accao, r: double, sn: Estado, an:Accao=None):
        pass