from numpy import double
from AprendPackage.aprendizagem.AprendRef import AprendRef
from AprendPackage.memoria.MemoriaAprend import MemoriaAprend
from AprendPackage.selecao_accao.SelAccao import SelAccao
from AprendPackage.modelos.Accao import Accao
from AprendPackage.modelos.Estado import Estado


class QLearning(AprendRef):

    def __init__(self, mem_aprend: MemoriaAprend, sel_accao: SelAccao, alfa: double, gama: double):
        super().__init__(mem_aprend, sel_accao, alfa, gama)


    def aprender(self, s:Estado, a:Accao, r:double, sn:Estado, an:Accao=None):
        an = self.sel_accao.max_accao(sn)
        qsa = self.mem_aprend.Q(s,a)
        qsnan = self.mem_aprend.Q(sn,an)
        q = qsa + self.alfa * (r + self.gama * qsnan -qsa)
        ##print("| STATE ", s.estado, "| ACTION ", a.accao, "| REWARD ", r, "| NEXT STATE ", sn.estado, "| Q ", q, " | NEXT Q", qsnan)
        self.mem_aprend.actualizar(s,a,q)







