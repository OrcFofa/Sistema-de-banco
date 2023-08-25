menu = """
======MENU======

[1]Deposito
[2]Saque
[3]Extrato
[0]Sair

================
"""

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    print(menu)
    opcao = int(input("Digite o numero da opção desejada: "))

    #função de deposito
    if opcao == 1:
        valor = float(input("Digite o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Deposito realizado com sucesso.")

        else:
            print("Não foi possivel realizar o deposito, numero invalido foi inserido")
            
    #Função de sacar
    elif opcao == 2:
        valor = float(input("Digite o valor do saque: "))

        #verifica se tem dinheiro pro saque
        passou_saldo = valor > saldo

        #verifica se esta abaixo de 500 (que foi o limite colocado)
        passou_limite = valor > limite

        #verifica se passou do numero de saques
        passou_saques = numero_saques >= LIMITE_SAQUES
        
        if passou_saldo:
            print("Operação não finalizada, sem saldo suficiente.")
        
        elif passou_limite:
            print("Operação não finalizada, passou do limite maximo pra saque.")

        elif passou_saques:
            print("Operação não finalizada, numero de saques ultrapassado.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso.")

        else:
            print("Operação não finalizada, valor inserido é invalido.")

    elif opcao == 3:
        print("\n¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ EXTRATO ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
        print("Não foram feitas movimentações." if not extrato else extrato) #usa um ternario pra ver se o extrato ta vazio ou não
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")

    elif opcao == 0:
        print("Muito obrigada por usar nosso sistema.")
        break
    
    else:
        print("Opção invalida, tente novamente.")