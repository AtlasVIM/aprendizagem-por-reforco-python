import time
import numpy as np
import glfw
from OpenGL.GL import *
from OpenGL.raw.GLU import gluOrtho2D

from AprendPackage.agentes.AgenteQuatroDirecoes import AgenteQuatroDirecoes
from AprendPackage.ambientes.Labirinto import Labirinto


class TesteLabirinto:
    def __init__(self, lado_grelha, estado_inicial, estado_final, paredes, accoes, sel_accao, mec, episodios, passos):
        self.labirinto =  Labirinto(
            lado_grelha=lado_grelha,
            estado_inicial=estado_inicial,
            estado_final=estado_final,
            paredes=paredes
        )

        self.sel_accao = sel_accao


        self.estado_inicial = estado_inicial
        self.estado_final = estado_final
        self.episodios = episodios
        self.passos = passos

        self.agente = AgenteQuatroDirecoes(mec,self.labirinto, accoes, estado_inicial)
        self.tamanho_janela = 1000
        self.celula = self.tamanho_janela / self.labirinto.lado_grelha
        self.passos_dados = 0
        self.episodios_dados = 0


        glfw.init()
        self.janela = glfw.create_window(self.tamanho_janela,
                                         self.tamanho_janela,
                                         "Teste Labirinto",
                                         None,
                                         None)
        glfw.make_context_current(self.janela)
        glClearColor(1.0, 1.0, 1.0, 1.0)
        glMatrixMode(GL_PROJECTION)
        gluOrtho2D(0, self.tamanho_janela, 0, self.tamanho_janela)



    def vizualizar(self):

        try:
            while not glfw.window_should_close(self.janela):

                self.treinar_e_atualizar()
        finally:
            glfw.terminate()


    def renderizar(self):
        glClear(GL_COLOR_BUFFER_BIT)
        self.desenhar_labirinto()
        self.desenhar_agente()
        glfw.swap_buffers(self.janela)

    def treinar_e_atualizar(self):


            for e in range(self.episodios):
                self.episodios_dados = e+1
                print(" ========= EPISODIO ", self.episodios_dados, " =========")
                self.agente.posicao = self.estado_inicial
                for p in range(self.passos):
                    self.passos_dados = p+1
                    print(" ========= PASSO NUMERO ", self.passos_dados, " =========")
                    self.agente.treinar()
                    self.renderizar()
                    glfw.poll_events()
                    time.sleep(0.05)
                    if (self.agente.posicao.x, self.agente.posicao.y) == (self.estado_final.x,self.estado_final.y):
                        print("OBJETIVO ENCONTRADO")
                        break
            glfw.set_window_should_close(self.janela, True)

    def desenhar_labirinto(self):

        for i in range(self.labirinto.lado_grelha):
            for j in range(self.labirinto.lado_grelha):
                x, y = j * self.celula, (self.labirinto.lado_grelha - i - 1) * self.celula

                if self.labirinto.grelha[i,j] == -1:
                    glColor3f(0.0, 0.0, 0.0)
                elif [i,j] == [self.labirinto.estado_final.y,self.labirinto.estado_final.x]:
                    glColor3f(1.0, 0.84, 0.0)
                else:
                    glColor3f(1.0, 1.0, 1.0)

                glBegin(GL_QUADS)
                glVertex2f(x, y)
                glVertex2f(x + self.celula, y)
                glVertex2f(x + self.celula, y + self.celula)
                glVertex2f(x, y + self.celula)
                glEnd()





    def desenhar_agente(self):
        x_agente, y_agente = self.agente.posicao.x, self.agente.posicao.y
        x_agente *= self.celula
        y_agente = (self.labirinto.lado_grelha - y_agente - 1) * self.celula
        x_centro = x_agente + self.celula // 2
        y_centro = y_agente + self.celula // 2

        glColor3f(1.0, 0.0, 1.0)
        glBegin(GL_POLYGON)
        for angle in np.linspace(0, 2.5 * np.pi, 30):
            glVertex2f(x_centro + 10 * np.cos(angle), y_centro + 10 * np.sin(angle))
        glEnd()
