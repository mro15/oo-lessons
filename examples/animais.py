# Exemplo de classe Animal e heranca: classes Mamifero e Ave
class Animal:
    nome = None
    especie = None
    sexo = None
    local = None

    def andar(self, destino):
        print(f'andando para {destino}')
        self.local = destino

    def dormir(self):
        self.local = 'toca'
        print('dormindo')

    def respirar(self):
        print('respirando')

class Mamifero(Animal):
    pelo = None

    def amamentar(self):
        print("Amamentando")

class Ave(Animal):
    tamanho_asa = 0
    cor_penas = None
    ovos = 0

    def botar(self):
        self.ovos += 1

    def voar(self, local_voo):
        print('voando ...')
        self.local = local_voo


galinha = Ave()
galinha.tamanho_asa = 45
galinha.cor_penas = 'branca'
print('Atributos galinha: ', galinha.tamanho_asa, galinha.cor_penas, galinha.ovos)
galinha.botar()
print('Atributos galinha: ', galinha.tamanho_asa, galinha.cor_penas, galinha.ovos)
