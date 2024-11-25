import tkinter

import numpy as np

from AprendPackage.aprendizagem.DynaQ import DynaQ
from AprendPackage.aprendizagem.MecAprendRef import MecAprendRef
from AprendPackage.aprendizagem.QLearning import QLearning
from AprendPackage.aprendizagem.QME import QME
from AprendPackage.aprendizagem.SARSA import SARSA
from AprendPackage.memoria.MemoriaAprend import MemoriaAprend
from AprendPackage.memoria.MemoriaEsparsa import MemoriaEsparsa
from AprendPackage.modelos.Accao import Accao
from AprendPackage.modelos.Estado import Estado
from AprendPackage.modelos.accoes_movimento.AccaoBaixo import AccaoBaixo
from AprendPackage.modelos.accoes_movimento.AccaoCima import AccaoCima
from AprendPackage.modelos.accoes_movimento.AccaoDireita import AccaoDireita
from AprendPackage.modelos.accoes_movimento.AccaoEsquerda import AccaoEsquerda
from AprendPackage.selecao_accao.EGreedy import EGreedy
from AprendPackage.selecao_accao.EGreedyWithDecay import EGreedyWithDecay
from AprendPackage.testes.TesteLabirinto import TesteLabirinto

## Teste Labirinto

alfa = np.double(0.1)
gama = np.double(0.5)
# epsilon para egreedy com decaimento
epsilon = np.double(0.4)
#epsilon = np.double(0.1)
num_sim = 100
dim_max = 100

lado_grelha = 11
estado_inicial = Estado(5,0)
estado_final = Estado(6,10)
paredes = [Estado(0,0),
           Estado(0,1),
           Estado(0, 2),
           Estado(0,3),
           Estado(0,4),
           Estado(0,6),
           Estado(0,7),
           Estado(0,8),
           Estado(0,9),
           Estado(0,10),
           Estado(1, 0),
           Estado(2, 0),
           Estado(3, 0),
           Estado(4, 0),
           Estado(5, 0),
           Estado(6, 0),
           Estado(7, 0),
           Estado(8, 0),
           Estado(9, 0),
           Estado(10, 0),
           Estado(10, 1),
           Estado(10, 2),
           Estado(10, 3),
           Estado(10, 4),
           Estado(10, 5),
           Estado(10, 6),
           Estado(10, 7),
           Estado(10, 8),
           Estado(10, 9),
           Estado(0, 10),
           Estado(1, 10),
           Estado(2, 10),
           Estado(3, 10),
           Estado(4, 10),
           Estado(5, 10),
           Estado(6, 10),
           Estado(7, 10),
           Estado(8, 10),
           Estado(9, 10),
           Estado(10, 10),
           Estado(1, 4),
           Estado(1, 6),
           Estado(2, 2),
           Estado(2, 3),
           Estado(2, 4),
           Estado(2, 6),
           Estado(2, 8),
           Estado(3, 3),
           Estado(3, 8),
           Estado(4, 2),
           Estado(4, 3),
           Estado(4, 4),
           Estado(4, 5),
           Estado(4, 7),
           Estado(4, 8),
           Estado(4, 9),
           Estado(5, 2),
           Estado(6, 2),
           Estado(6, 3),
           Estado(6, 5),
           Estado(6, 6),
           Estado(6, 7),
           Estado(6, 9),
           Estado(7, 7),
           Estado(8, 1),
           Estado(8, 3),
           Estado(8, 4),
           Estado(8, 5),
           Estado(8, 5),
           Estado(8, 7),
           Estado(8, 8),
           Estado(9, 4),
           Estado(9, 7),
           ]

accoes = [AccaoEsquerda(), AccaoDireita(), AccaoCima(), AccaoBaixo()]

mem_aprend = MemoriaEsparsa()
#sel_accao = EGreedy(mem_aprend, accoes, epsilon)
sel_accao = EGreedyWithDecay(mem_aprend,accoes,epsilon)


#aprendizagem = DynaQ(mem_aprend, sel_accao, alfa, gama,num_sim)
aprendizagem = QME(mem_aprend, sel_accao, alfa, gama, num_sim, dim_max)

## Para estes algoritmos funcionarem é preciso alterar os parametros alfa, gama e epsilon
#aprendizagem = SARSA(mem_aprend,sel_accao,alfa,gama)
#aprendizagem = QLearning(mem_aprend,sel_accao,alfa,gama)

mec = MecAprendRef(accoes, aprendizagem, sel_accao, mem_aprend)

teste = TesteLabirinto(
    lado_grelha,
    estado_inicial,
    estado_final,
    paredes=paredes,
    accoes=accoes,
    sel_accao=sel_accao,
    mec=mec,
    episodios=50,
    passos=100
                       )

teste.vizualizar()

