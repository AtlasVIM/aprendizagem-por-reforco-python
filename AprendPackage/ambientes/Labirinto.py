import numpy as np

from AprendPackage.ambientes.ModeloAmbiente import ModeloAmbiente


from AprendPackage.modelos.Estado import Estado


class Labirinto(ModeloAmbiente):


    def __init__(self, lado_grelha:int, estado_inicial:Estado, estado_final:Estado, paredes:[Estado]):
        super().__init__()
        self.lado_grelha = lado_grelha
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final
        self.paredes = paredes
        self.grelha = self.criar_labirinto()

    def posicao_valida(self, posicao):
        x,y = posicao.x,posicao.y

        return 0 <= x <= self.lado_grelha-1 and 0 <= y <= self.lado_grelha-1 and self.grelha[y,x] != -1

    def criar_labirinto(self):

        grelha = np.zeros((self.lado_grelha, self.lado_grelha))

        for parede in self.paredes:
            y,x = parede.y,parede.x
            grelha[x,y] = -1

        x,y = self.estado_final.x,self.estado_final.y
        grelha[y,x] = 1

        return grelha

