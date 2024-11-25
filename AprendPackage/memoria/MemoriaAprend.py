from abc import abstractmethod

from numpy import double

from AprendPackage.modelos.Accao import Accao
from AprendPackage.modelos.Estado import Estado


class MemoriaAprend:

    @abstractmethod
    def actualizar(self, s:Estado, a:Accao, q:double):
        pass

    @abstractmethod
    def Q(self, s:Estado, a:Accao) -> double:
        pass

