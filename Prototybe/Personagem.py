from abc import ABC, abstractmethod
class Personagem(ABC):
    def __init__(self, nome, vida, magia, forca):
        self.nome = nome
        self.vida = vida
        self.magia = magia
        self.forca = forca

    def getInformacoes(self):
        return f"nome: {self.nome}, vida: {self.vida}, magia: {self.magia}, força {self.forca}"


    @abstractmethod
    def clone(self):
        pass