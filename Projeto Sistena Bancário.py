# Projeto Sistena Bancário - curso python

menu = """
    ---------------------------------   
           OPÇÕES BANCÁRIAS 
    ---------------------------------
             [1] Depositar
             [2] Sacar
             [3] Extrato
             [9] Sair
    ---------------------------------
    Opção Desejada: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":  # depositar
        valor = float(input("Valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! Valor informado é inválido.")

    elif opcao == "2":   # sacar 
        valor = float(input("Valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print("Operação não realizada! Saldo suficiente.")
        elif excedeu_limite:
            print(f"Operação não realizada! O valor do saque excede o limite de {limite:.2f} por transação.")
        elif excedeu_saques:
            print(f"Operação falhou! Você pode realizar até {LIMITE_SAQUES:.0f} saques por dia!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação não realizada! O valor informado é inválido.")

    elif opcao == "3":    # extrato
        print("\n------------ Extrato -------------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("---------------------------------")

    elif opcao == "9":   # sair
        break
    else:
        print("Operação inválida, por favor selecione a operação desejada.")
