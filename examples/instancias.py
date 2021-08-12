from pessoa import Pessoa, PessoaConstruida, Musico
from carro import Carro, Caminhonete

# Instancia de alice e bob, classe Pessoa
alice = Pessoa()
bob = Pessoa()

# Instancia de uno e gol, classe carro
uno = Carro()
gol = Carro()

# Atribuicao de valores aos atributos de alice
alice.nome = 'Alice'
alice.idade = 25
alice.localizacao = 'Harve'
alice.altura = 1.73

# Acessando os valores dos atributos de alice
print('Nome da pessoa: ', alice.nome)
print('Idade da pessoa: ', alice.idade)
print('Altura da pessoa: ', alice.altura)
print('Localizacao da pessoa: ', alice.localizacao)

# Chamando o metodo andar para o objeto alice
alice.andar('casa')
print('Localizacao atual de alice: ', alice.localizacao)

# Instancia de lucia, da classe PessoaConstruida
lucia = PessoaConstruida('Lucia', 10, 1.60)
print('Nome da pessoa construida: ', lucia.nome)
print('Idade da pessoa construida: ', lucia.idade)
print('Altura da pessoa construida: ', lucia.altura)

# Instancia da classe Caminhonete que herda da classe Carro
caminhonete = Caminhonete()
caminhonete.cor = 'preta'
caminhonete.tamanho = 2
caminhonete.localizacao = 'casa'
caminhonete.ano_fabricacao = 2018

print('Cor da caminhonete: ', caminhonete.cor)
print('Tamanho da caminhonete: ', caminhonete.tamanho)
print('Localizacao da caminhonete: ', caminhonete.localizacao)
print('Ano de fabricacao da caminhonete: ', caminhonete.ano_fabricacao)

caminhonete.lavar()
caminhonete.acelerar(30)

# Instancia da classe Musico, que herda da classe Pessoa
musico = Musico('violao')
musico.nome = 'Marcela'

musico.tocar()
musico.andar('estudio')
print('Localizacao: ', musico.localizacao)

