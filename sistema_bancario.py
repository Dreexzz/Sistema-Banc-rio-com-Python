menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 4500
limite = 4500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
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
            extrato += f"Saque R$ {valor:.2f}\n"
            numero_saques += 1
            print("Operção feita com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")
        
        

    elif opcao == "e":
        print("\n ---------------------- EXTRATO ----------------------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("--------------------------------------------------------")
    
    elif opcao == "q":
        print("Agradecemos pela sua presença, até logo!")
        break
    
    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")
