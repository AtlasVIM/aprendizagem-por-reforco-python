from numpy import double

from AprendPackage.aprendizagem.QLearning import QLearning
from AprendPackage.memoria import MemoriaAprend
from AprendPackage.memoria.MemoriaExperiencia import MemoriaExperiencia
from AprendPackage.modelos.Estado import Estado
from AprendPackage.modelos.Accao import Accao
from AprendPackage.modelos.Experiencia import Experiencia
from AprendPackage.selecao_accao.SelAccao import SelAccao


class QME(QLearning):
    def __init__(self, mem_aprend: MemoriaAprend, sel_accao:SelAccao, alfa:double, gama:double, num_sim:int, dim_max:int):
        super().__init__(mem_aprend,sel_accao,alfa,gama)
        self.num_sim = num_sim
        self.memoria_experiencia = MemoriaExperiencia(dim_max)


    def aprender(self, s:Estado, a:Accao, r:double, sn:Estado, an:Accao = None):
        super().aprender(s,a,r,sn)
        e = Experiencia(s,a,r,sn)
        self.memoria_experiencia.actualizar(e)
        self.simular()


    def simular(self):
        amostras = self.memoria_experiencia.amostrar(self.num_sim)
        for experiencia in amostras:
            super().aprender(experiencia.s,experiencia.a,experiencia.r,experiencia.sn)