from numpy import double


from AprendPackage.modelos import Accao
from AprendPackage.modelos.Estado import Estado


class ModeloAgente:

    def __init__(self, mec_aprend):
        self.mec_aprend = mec_aprend


    def executar(self):
        pass

    def selecionar_accao(self, s:Estado) -> Accao:
        return self.mec_aprend.selecionar_accao(s)

    def aprender(self, s: Estado, a: Accao, r: double, sn: Estado, an=None):
        self.mec_aprend.aprender(s, a, r, sn, an)

    def treinar(self):
        pass