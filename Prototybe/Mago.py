import copy
from Personagem import Personagem
class Mago(Personagem):
    def __init__(self, nome, vida, magia, forca):
        super().__init__(nome, vida, magia, forca)
        self.classe = "Mago"

    def getInformacoes(self):
        return f"classe: {self.classe}, nome: {self.nome}, vida: {self.vida}, magia: {self.magia}, força {self.forca}"

    def clone(self):
        return copy.deepcopy(self)

