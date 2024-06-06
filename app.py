# 3 importar o arquivo que contém a classe restaurante
from modelos.restaurante4 import Restaurante

# 4 criar m objeto(instâmcia dde restaurante)
restaurante_praca=Restaurante('praça','gourmet')
restaurante_mexico=Restaurante('mexican food','mexicana')
restaurante_japones=Restaurante('japa','japonesa')

# alterar estado de um restaurante
restaurante_japones.alternar_estado()

# criando avaliaçõs para o restaurante praça
restaurante_praca.receber_avaliacao('Albino',8)
restaurante_praca.receber_avaliacao('Berenice',10)

# 2 criando a chamada da função de entrada
def main():
    # 5 inserir uma ação dentro do main
    Restaurante.listar_restaurantes()
    

if __name__=='__main__':
    main()