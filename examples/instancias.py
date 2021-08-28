from pessoa import Pessoa, PessoaConstruida, Musico
from carro import Carro, Caminhonete

# Instancia de alice e bob, classe Pessoa
alice = Pessoa()
bob = Pessoa()

# Instancia de uno e gol, classe carro
uno = Carro()
gol = Carro()

# atribuindo valores ao objeto uno
uno.modelo = 'uno'
uno.cor = 'vermelho'
uno.ano_fabricacao = 2000
uno.proprietario = 'Bob'

# acesssar os valores do objeto uno
print('Acessando o atributo modelo do objeto uno: ', uno.modelo)
print('Acessando o atributo cor do objeto uno: ', uno.cor)

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
obj = PessoaConstruida('Lucia', 10, 1.60)
print('Nome da pessoa construida: ', obj.nome)
print('Idade da pessoa construida: ', obj.idade)
print('Altura da pessoa construida: ', obj.altura)



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

