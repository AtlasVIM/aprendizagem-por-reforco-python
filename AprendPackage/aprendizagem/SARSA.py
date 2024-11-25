from numpy import double

from AprendPackage.modelos.Accao import Accao
from AprendPackage.aprendizagem.AprendRef import AprendRef
from AprendPackage.modelos.Estado import Estado
from AprendPackage.memoria.MemoriaAprend import MemoriaAprend
from AprendPackage.selecao_accao.SelAccao import SelAccao


class SARSA(AprendRef):
    def __init__(self, mem_aprend: MemoriaAprend, sel_accao: SelAccao, alfa: double, gama: double):
        super().__init__(mem_aprend, sel_accao, alfa, gama)

    def aprender(self, s:Estado, a:Accao, r:double, sn:Estado, an:Accao = None):
        an = self.sel_accao.selecionar_accao(sn)
        qsa = self.mem_aprend.Q(s,a)
        qsnan = self.mem_aprend.Q(sn,an)
        q = qsa + self.alfa * (r + self.gama * qsnan -qsa)
        print(q, "SARSA Q", qsnan, "SARSA QSNAN", (sn.x,sn.y), " NEXT STATE")
        self.mem_aprend.actualizar(s,a,q)
