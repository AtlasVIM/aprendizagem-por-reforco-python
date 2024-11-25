from numpy import double

from AprendPackage.selecao_accao.SelAccao import SelAccao
from AprendPackage.aprendizagem.QLearning import QLearning
from AprendPackage.memoria.MemoriaAprend import MemoriaAprend
from AprendPackage.modelos.Accao import Accao
from AprendPackage.modelos.Estado import Estado
from AprendPackage.modelos.ModeloTR import ModeloTR


class DynaQ(QLearning):


    def __init__(self, mem_aprend: MemoriaAprend, sel_accao: SelAccao, alfa: double, gama: double, num_sim: int):
        super().__init__(mem_aprend, sel_accao, alfa, gama)
        self.num_sim = num_sim
        self.modelo = ModeloTR()

    def aprender(self, s:Estado, a:Accao, r:double, sn:Estado, an:Accao=None):
        super().aprender(s,a,r,sn)
        self.modelo.atualizar(s,a,r,sn)
        self.simular()

    def simular(self):
        for i in range(self.num_sim):
            s,a,r,sn = self.modelo.amostrar()
            super().aprender(s,a,r,sn)
