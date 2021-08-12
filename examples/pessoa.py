
class Pessoa:
    nome = None
    idade = None
    altura = None
    endereco = None
    localizacao = None

    def andar(self, destino):
        self.localizacao = destino

    def dormir(self, destino_quarto):
        print('Indo dormir...')
        self.localizacao = destino_quarto

    def comer(self, destino_cozinha):
        print('Indo para a cozinha...')
        self.localizacao = destino_cozinha

class PessoaConstruida:

    nome = None
    idade = None
    altura = None

    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura