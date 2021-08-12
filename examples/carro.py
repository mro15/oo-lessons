
class Carro:
    modelo = None
    cor = None
    ano_fabricacao = None
    proprietario = None
    velocidade = 0

    def ligar(self):
        print('Carro ligado!')

    def desligar(self):
        print('Carro desligado.')

    def acelerar(self, velocidade):
        print('Acelerando ...')
        self.velocidade = self.velocidade + velocidade

class Caminhonete(Carro):
    tamanho = None
    localizacao = None

    def lavar(self):
        print('Indo ao lava car ...')
        self.localizacao = 'lava car'