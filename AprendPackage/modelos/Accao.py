
class Accao:
    def __init__(self, accao):
        self.accao = accao

    def __eq__(self, other):
        return self.accao == other.accao

    def __hash__(self):
        return hash(self.accao)