import datetime

class Usuario:
    def __init__(self, data_de_nascimento, email, cpf, nome, endereco):
        self.email = email
        self.data_de_nascimento = data_de_nascimento
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco

class Conta:
    def __init__(self,usuario, numero_conta):
        self.agencia = "0001"
        self.numero_conta = numero_conta
        self.saldo = 0
        self.limite = 0
        self.numero_saques = 0
        self.usuario = usuario


class banco:
    def __init__(self):
        self.usuarios = {}
        self.contas = {}
        self.numero_conta_atual = 1
    
    def cadastrar_usuario(self, data_de_nascimento, email, cpf, nome, endereco):
        if cpf in self.usuarios:
            print("Não foi possivel cadastrar, pois esse cpf já está em uso")
            return False
        novo_usuario = Usuario(data_de_nascimento, email, cpf,nome, endereco)
        self.usuarios[cpf] = novo_usuario
        banco.criar_conta(novo_usuario)
        
        print("Usuario cadastrado com sucesso!\n")
        return True
    
    def criar_conta(self, usuario):
        criar_conta = Conta(usuario, self.numero_conta_atual)
        self.contas[self.numero_conta_atual] = criar_conta
        self.numero_conta_atual += 1
        print("Conta do usuário criada!")

    
    def buscar_usuario_por_cpf(self, cpf):
        usuario = self.usuarios.get(cpf, None)
        return usuario
    
    
    def buscar_conta_por_cpf(self, cpf):
        return self.contas.get(cpf, None)
    
    def buscar_conta_por_numero(self, numero):
        return self.contas.get(numero, None)
    
    def lista_dos_usuarios(self):
        print(f"------------------- Usuários --------------------\n")
        for indent in self.usuarios:
            user = banco.buscar_usuario_por_cpf(indent)
            for num in self.contas:
                conta = self.buscar_conta_por_numero(num)
                if conta.usuario.cpf == indent:
                    print(f"Nome: {user.nome}                    Numero da Conta: {conta.numero_conta}\n")

    def buscarContaUsuario(self, usuario):
          for num in self.contas:
                conta = self.buscar_conta_por_numero(num)
                if conta.usuario.cpf == usuario.cpf:
                    conta = banco.buscar_conta_por_numero(conta.numero_conta)
                    return conta
# Início do programa
banco = banco()

                                                    
def solicitar_dados_usuario(cpf):
    data_de_nascimento = input("Informe a sua data de nascimento:")
    email = input("Informe o seu email:")
    cpf = cpf
    nome =input("Informe o seu nome completo:")
    endereco = input("Informe o seu endereço completo:")
    return data_de_nascimento, email, cpf, nome, endereco 


def mensagemPersonalizada (funcao, valor):
    data = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"{funcao} valor {valor} - Data: {data}\n"


def menu(usuario):

    conta = banco.buscarContaUsuario(usuario)
    menu = """

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [cr]Criar conta
    [ls]Lista contas
    [cs]Criar usuario
    [q]\tSair
    => """
    

    saldo = conta.saldo
    limite = 0
    extrato = ""
    numero_saques = conta.numero_saques
    limite_saques = 3
                     

    while True:
        opcao = input(menu)
        
        if opcao == "d":
            valor = float(input("Informe o valor do depósito:"))

            if valor > 0:
                saldo += valor
                conta.saldo = saldo
                extrato += mensagemPersonalizada ("Deposito:",valor)
                print("Depósito feito com sucesso!!")
                
            else:
                print("Operação falhou! o valor informado não está correto ou inválido.")

        elif opcao == "s":
            valor = float(input("Informe o valor do saque:"))
            limite_saldo = valor > saldo
            limite_limite = valor > limite
            limite_saques_excedido = numero_saques >= limite_saques
            
            if limite_saldo:
                print("A operação falhou! O seu saldo é insuficiente.")

            elif limite_limite:
                print("A operação falhou! Você ultrapassou o saque limite.")    

            elif limite_saques_excedido:
                print("A operação falhou! Você já fez os 3 saques diários.")

            elif valor > 0:
                saldo -= valor
                extrato += mensagemPersonalizada ("Saque:", valor)
                numero_saques += 1
                print("Operção feita com sucesso!")
            else:
                print("Operação falhou! O valor informado é inválido.")
            
            

        elif opcao == "e":
            print("\n ---------------------- EXTRATO ----------------------")
            print(f"Agencia: {conta.agencia} Conta: {conta.numero_conta}\n")
            print(f"Nome: {usuario.nome}\n")
            if not extrato:
                print("Não foram realizadas movimentações.\n")
            else:
                for movimentacao in extrato.split('\n'):
                    print(movimentacao)

            print(f"\nSaldo: R$ {saldo:.2f}")
            print("--------------------------------------------------------")

        elif opcao == "cs":
            identificarUsuario()
            

        elif opcao == "ls":
             banco.lista_dos_usuarios()

        
        elif opcao == "cr":
            banco.criar_conta(usuario)

        elif opcao == "q":
            print("Agradecemos pela sua presença, até logo!")
            identificarUsuario()
        else:
            print("Operação invalida, por favor selecione novamente a operação desejada.")
        
        
def identificarUsuario():
    cpf = input("Informe o seu CPF (formato: xxx.xxx.xxx-xx):")
    usuario = banco.buscar_usuario_por_cpf(cpf)
    if usuario != None : 
        menu(usuario)
       
    else:
       data_de_nascimento, email, cpf, nome, endereco  = solicitar_dados_usuario(cpf)
       banco.cadastrar_usuario(data_de_nascimento, email, cpf, nome, endereco)
       usuario = banco.buscar_usuario_por_cpf(cpf)
       menu(usuario)

identificarUsuario()


            
    