# 1 criação da classe carro

# class Carro:
#     modelo=''
#     cor=''
#     ano=''

#     volvo=Carro()
#     volvo.modelo="EX30"
#     volvo.cor="Cloud Blue"
#     volvo.ano="2024"

# 2 criação da classe restaurante
# class Restaurante:
#     nome=''
#     categoria=''
#     ativo=''
#     cardapio=''
#     acessibilidade=''

# restaurante_hadassa=Restaurante()
# restaurante_hadassa="Hadassa"
# restaurante_hadassa="Pizzaria"
# restaurante_hadassa=False
# restaurante_hadassa="Pizza"
# restaurante_hadassa="Rampa, elevador, braille"

# 3 e 4 adicionando um construtor na classe restaurante
class Restaurante:
    restaurantes=[]
    def __init__(self, nome, categoria, cardapio, acessibilidade):
        self.nome=nome
        self.categoria=categoria
        self.ativo=False
        self.cardapio=cardapio
        self.acessibilidade=acessibilidade

        Restaurante.restaurantes.append(self)
        

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo} |  {self.cardapio} | {self.acessibilidade}'
    
# construção do objeto (instancia)
restaurante_nathi=Restaurante('Hadassa', 'Pizzaria', 'pizza', 'sim')

print(restaurante_nathi)

# 5 criação da classe cliente com construtor

class Cliente:
    clientes=[]
    def __init__(self, nome, idade, altura, sexo):
        self.nome=nome
        self.idade=idade
        self.altura=altura
        self.sexo=sexo

        Cliente.clientes.append(self)

jubiscleison=Cliente('Jubiscleison', '20', '1,80', 'Masculino')
ceverina=Cliente('Ceverina', '20', '1,50', 'Feminino')
jubiscreusa=Cliente('Jubiscreusa', '20', '1,56', 'Feminino')

print(vars(jubiscleison))
print(vars(ceverina))
print(vars(jubiscreusa))

    
    




















