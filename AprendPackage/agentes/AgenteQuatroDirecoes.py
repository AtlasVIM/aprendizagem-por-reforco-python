import numpy as np
from numpy import double

from AprendPackage.agentes.ModeloAgente import ModeloAgente
from AprendPackage.ambientes.Labirinto import Labirinto
from AprendPackage.aprendizagem import MecAprendRef
from AprendPackage.modelos import Accao
from AprendPackage.modelos.Estado import Estado


class AgenteQuatroDirecoes(ModeloAgente):
    def __init__(self, mec_aprend:MecAprendRef,labirinto:Labirinto, accoes, posicao):
        super().__init__(mec_aprend)
        self.labirinto = labirinto
        self.accoes = accoes
        self.posicao = posicao


    def selecionar_accao(self, s:Estado) -> Accao:
        return super().selecionar_accao(self.posicao)

    def aprender(self, s: Estado, a: Accao, r: double, sn: Estado, an=None):
        self.mec_aprend.aprender(s,a,r,sn,an)

    def prox_estado(self,a:Accao):
        return Estado(self.posicao.x+a.x, self.posicao.y+a.y)


    def treinar(self):
                a = self.selecionar_accao(self.posicao)
                sn = self.prox_estado(a)

                r = np.double(-0.1)
                if self.labirinto.grelha[sn.y][sn.x] == -1:
                    r = np.double(-10)
                    print("LABIRINTH REWARD: ", -100)
                elif self.labirinto.grelha[sn.y][sn.x] == 1:
                    r = np.double(1000)
                    print("LABIRINTH REWARD: ", 1000)

                self.aprender(self.posicao,a,r,sn)
                print((self.posicao.x,self.posicao.y), " ESTADO ATUAL", (sn.x,sn.y), " PROX ESTADO", self.mec_aprend.mem_aprend.Q(self.posicao,a))

                if self.labirinto.posicao_valida(sn):
                    self.posicao = sn


