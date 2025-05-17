# POO - Programação Orientada a Objetos


class Ford:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

Shelby = Ford("Mustang", "Shelby GT350", 2019)
Gol = Ford("Volkswagen", "Gol", 2012)

print(Shelby.modelo)
print(Gol.modelo)
