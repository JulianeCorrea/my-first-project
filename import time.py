import time

class Tamagotchi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.felicidade = 50
        self.energia = 50

    def alimentar(self):
        if self.fome > 0:
            self.fome -= 10
            self.felicidade += 5
            print(f"{self.nome} foi alimentado!")
        else:
            print(f"{self.nome} não está com fome.")

    def brincar(self):
        if self.energia > 0:
            self.felicidade += 10
            self.energia -= 15
            print(f"{self.nome} brincou e está mais feliz!")
        else:
            print(f"{self.nome} está cansado demais para brincar.")

    def dormir(self):
        if self.energia < 100:
            self.energia += 20
            print(f"{self.nome} dormiu e recuperou energia.")
        else:
            print(f"{self.nome} já está com a energia cheia.")

    def status(self):
        print(f"Status de {self.nome}:")
        print(f"Fome: {self.fome}")
        print(f"Felicidade: {self.felicidade}")
        print(f"Energia: {self.energia}")

    def passar_tempo(self):
        self.fome += 5
        self.felicidade -= 5
        self.energia -= 5

# Loop Principal
nome = input("Dê um nome ao seu Tamagotchi: ")
tamagotchi = Tamagotchi(nome)

while True:
    tamagotchi.status()
    print("\nO que você quer fazer?")
    print("1. Alimentar")
    print("2. Brincar")
    print("3. Dormir")
    print("4. Sair")
    
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        tamagotchi.alimentar()
    elif escolha == "2":
        tamagotchi.brincar()
    elif escolha == "3":
        tamagotchi.dormir()
    elif escolha == "4":
        print("Até logo!")
        break
    else:
        print("Escolha inválida.")
    
    time.sleep(1)
    tamagotchi.passar_tempo()
    print("\n" + "-" * 30 + "\n")