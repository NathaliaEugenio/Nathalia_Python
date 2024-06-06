# 1 classe Restaurante
class Restaurante:
    nome=''
    categoria=''
    ativo=False

# 2 objetos
restaurante_praca=Restaurante()
restaurante_praca.nome='Praça'
restaurante_praca.categoria='Gourmet'

restaurante_pizza=Restaurante()

restaurantes=[restaurante_praca, restaurante_pizza]

#print(dir(restaurante_praca))
#print('')
#print(vars(restaurante_praca))

# questão 1
restaurante_praca.categoria='Italiana'
'''
def atribuir_categoria():
    nome_do_restaurante=input('Digite o nome do restaurante que você deseja alterar a categoria: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_do_restaurante==restaurante.nome:
            restaurante_encontrado=True
            categoria_do_restaurante=input('Digite a nova categoria do restaurante: ')
            restaurante.categoria=categoria_do_restaurante
            mensagem=f'A categoria do Restaurante {nome_do_restaurante} foi alterada para {categoria_do_restaurante} com sucesso!'
            print(mensagem)
            print('')

        if not restaurante_encontrado:
            print(f'O restaurante {nome_do_restaurante} não foi encontrado!')
            print('')

atribuir_categoria()
'''
# questão 2
nome_restaurante=restaurante_praca.nome

# questão 3
if restaurante_praca.ativo:
    print('O restaurante está ativado')
    print('')
else:
    print('O restaurante está desativado')
    print('')

# questão 4
categoria=Restaurante.categoria

# questão 5
restaurante_praca.nome='Bistrô'

# questão 6
restaurante_pizza.nome='Pizza Place'
restaurante_pizza.categoria='Fast Food'

# questão 7
if restaurante_pizza.categoria=='Fast Food':
    print('A categoria da instância restaurante_pizza é Fast Food')
    print('')
else:
    print('A categoria da instância restaurante_pizza não é Fast Food')
    print('')

# questão 8
restaurante_pizza.ativo=True

# questão 9
print(restaurante_praca.nome)
print('')
print(restaurante_praca.categoria)
print('')