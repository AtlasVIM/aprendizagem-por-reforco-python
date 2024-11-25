from numpy import double

from AprendPackage.modelos import Accao
from AprendPackage.modelos.Estado import Estado


class Experiencia:
    def __init__(self, s:Estado, a:Accao, r:double, sn:Estado):
        self.s = s
        self.a = a
        self.r = r
        self.sn = sn

