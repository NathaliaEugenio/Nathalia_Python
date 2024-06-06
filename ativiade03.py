# Exercício 1 "criando a classe pessoa"
class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def __str__(self):
        return f"{self.nome} | {self.idade} | {self.profissao}"
    
    def aniversario(self):
        self.idade += 1


    def saudacao(self):
        print("Olá Nathalia! Seja bem-vinda. Que sua paixão por explorar os segredos da vida continue a inspirar e encantar. Estamos ansiosos para ver as descobertas incríveis que você fará!" + self.nome) 


nathalia = Pessoa("Nathalia", 20, "Bióloga")
print(nathalia)

nathalia.aniversario()
print(nathalia)

print(nathalia.saudacao())

# Exercício 2
class ContaBancaria:
    conta=[]
    def __init__(self, titular, saldo):
        self.titular=titular
        self.saldo=saldo
        self.ativo=False
        
        ContaBancaria.conta.append(self)

# Exercício 3
    def __str__(self):
        return f'{self.titular} | {self.saldo}'

conta1=ContaBancaria('Nathalia','R$1000')
conta2=ContaBancaria('Vitor', 'R$100.000,00')
print(conta1)
print(conta2)

# Exercício 4
@classmethod
def ativar_conta(self):
    self.ativo=True

conta3=ContaBancaria('Jubiscleusa', 5.00)
print(f'Antes de ativar: Conta ativa? {conta3.ativo}')
ContaBancaria.ativar_conta(conta3)
print(f'Depois de ativar: Conta ativa? {conta3.ativo}')

# Exercício 5
class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self.titular=titular
        self.saldo=saldo
        self.ativo=False

@property
def titular(self):
    return self.titular

@property
def saldo(self):
    return self.saldo

@property
def ativo(self):
    return self.ativo


# Exercício 6
conta4=ContaBancariaPythonica('Josefino', 1500.03)
print(f'Titular da conta 4 é: {conta4.titular}')

# Exercício 7
class Clientebanco:
    def __init__(self, nome, idade, profissao, endereco, telefone):
        self.nome=nome
        self.idade=idade
        self.profissao=profissao
        self.endereco=endereco
        self.telefone=telefone

cliente1=Clientebanco('João',30,'médico','Rua A','3696 6969')
cliente2=Clientebanco('Cleison',23,'jornalista','Rua B','3696 6969')
cliente3=Clientebanco('bernadete',40,'agricultora','Rua C','3696 6969')

# Exercício 8
@classmethod
def criar_conta(cls,titular,saldo_inicial):
    conta=Clientebanco(titular, saldo_inicial)
    return conta










    
