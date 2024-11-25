from numpy import double

from AprendPackage.memoria import MemoriaAprend
from AprendPackage.aprendizagem.AprendRef import AprendRef
from AprendPackage.modelos.Accao import Accao
from AprendPackage.modelos.Estado import Estado
from AprendPackage.selecao_accao.SelAccao import SelAccao
from AprendPackage.aprendizagem.Aprendizagem import Aprendizagem

class MecAprendRef(Aprendizagem):
    def __init__(self, accoes, aprend_ref:AprendRef, sel_accao:SelAccao, mem_aprend:MemoriaAprend):
        self.accoes = accoes
        self.aprend_ref = aprend_ref
        self.sel_accao = sel_accao
        self.mem_aprend = mem_aprend


    def selecionar_accao(self, s:Estado) -> Accao:
        return self.sel_accao.selecionar_accao(s)


    def aprender(self, s: Estado, a: Accao, r:double, sn: Estado, an=None):
        self.aprend_ref.aprender(s,a,r,sn,an)

