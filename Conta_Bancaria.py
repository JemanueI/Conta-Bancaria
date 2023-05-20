menu = """
[1] Deposito
[2] Saque
[3] Extrato
[4] Sair
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0 
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print("Operacao realizada com sucesso!")

        else:
            print("Operação não realizada!")

    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite =  valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operacao nao realizada!")

        elif excedeu_limite:
            print("Operacao nao realizada!")

        elif excedeu_saques:
            print("Operacao nao realizada!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1 
            print("Operacao realizada com sucesso!")

        else:
            print("Operacao nao realizada!")
    
    elif opcao == "3":
        print("\n=========> EXTRATO <=========")
        print("Não houve transações" if not extrato else extrato)
        print(f"\nSaldo: {saldo:.2f}")
        print("=============================")
    
    elif opcao == "4":
        break

    else:
        print("Operacao nao realizada, tente novamente!")