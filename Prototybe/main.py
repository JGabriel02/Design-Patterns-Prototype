from Guerreiro import Guerreiro
from Mago import Mago

print("==================================================")
personagem1 = Guerreiro("Olaf", 100, 20, 50)
personagem2 = Mago("Veigar", 80, 100, 30)
print(personagem1.getInformacoes())
print(personagem2.getInformacoes())
print("==================================================")
print("instanciando copías de 4 Guerreiros:")
template_guerreiro = Guerreiro("Sett", 100, 20, 100)
for i in range(1,5):
    clone_guerreiro = template_guerreiro.clone()
    print(f" {i} - {template_guerreiro.getInformacoes()}")
print("==================================================")
print("instanciando copías de 4 Magos")
personagem2.nome = "Ryze"
for i in range(1,5):
    clone_mago = personagem2.clone()
    print(f" {i} - {personagem2.getInformacoes()}")
print("==================================================")
print("Criando dois Personagens de cada classe:")
template_guerreiro1 = Guerreiro("Volibear", 300, 50, 50)
template_mago1 = Mago("Ahri", 60, 200, 100)
for i in range(1,3):
    clone_guerreiro1 = template_guerreiro1.clone()
    clone_mago1 = template_mago1.clone()
    print(f" {i} - {template_guerreiro1.getInformacoes()}")
    print(f" {i} - {template_mago1.getInformacoes()}")




