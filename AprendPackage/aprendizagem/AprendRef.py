from abc import abstractmethod

from numpy import double

from AprendPackage.modelos.Accao import Accao
from AprendPackage.modelos.Estado import Estado
from AprendPackage.selecao_accao.SelAccao import SelAccao
from AprendPackage.memoria.MemoriaAprend import MemoriaAprend


class AprendRef:

    def __init__(self, mem_aprend: MemoriaAprend, sel_accao: SelAccao, alfa: double, gama: double):
        self.mem_aprend = mem_aprend
        self.sel_accao = sel_accao
        self.alfa = alfa
        self.gama = gama


    @abstractmethod
    def aprender(self, s:Estado, a:Accao, r:double, sn:Estado, an:Accao = None):
        pass