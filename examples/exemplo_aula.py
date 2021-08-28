# Exemplo de classe

class ExemploClasse:
    # atributos
    numero = None
    nome = None


# instancia da classe ExemploClasse
aula = ExemploClasse()

print("Objeto aula ", aula, "\n\n")
print("Antes da atribuicao")
print(aula.numero)
print(aula.nome)

aula.numero = 7
aula.nome = 'orientacao a obj'

print("Depois da atribuicao")
print(aula.numero)
print(aula.nome)
