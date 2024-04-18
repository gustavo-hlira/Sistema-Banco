menu = """
╔═══════════════════════════╗
║     Bem Vindo ao Lira Bank║
╠═══════════════════════════╣
║ [1] Depositar             ║
║ [2] Sacar                 ║
║ [3] Extrato               ║
║ [0] Sair                  ║
╚═══════════════════════════╝
=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)
    if opcao == "1":
        print("Deposito")
        valor = float(input("Digite o valor a ser depositado:R$ "))
        
        if valor > 0 :
            saldo += valor
            extrato += f"Deposito: R${valor:.2f}\n"
            print("===================================")
            print("        Depósito Realizado         ")
            print("-----------------------------------")
            print(f"Valor depositado: R${valor:.2f}")
            print(f"Saldo atual: R${saldo:.2f}")
            print("===================================")
            input("Pressione Enter para continuar...")
        
        else:
            print("Falha no deposito! O valor informado é inválido.")
            input("Pressione Enter para continuar...")

    elif opcao == "2":
        print("Saque")
        valor = float(input("Digite o valor do saque:R$ "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques > LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Saque cancelado! Você não tem saldo suficiente!")
        elif excedeu_limite:
            print("Saque cancelado! Você não tem limite disponível!")
        elif excedeu_saque:
            print("Você excedeu o numero de saques do dia")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
            print("===================================")
            print("         Saque Realizado           ")
            print("-----------------------------------")
            print(f"Valor sacado: R${valor:.2f}")
            print(f"Saldo atual: R${saldo:.2f}")
            print("===================================")
            input("Pressione Enter para continuar...")

        else:
            print("Operação falhou! O valor informado não é valido!")



    elif opcao == "3":
        
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações.")


        else:
            print("Descrição         | Valor")
            print("-----------------------------------------")
            for movimento in extrato.split("\n"):
                if movimento: 
                    tipo, valor = movimento.split(": ")
                    print(f"{tipo:<17} | R$ {valor:>10}")
        print("\nSaldo atual:", f"R$ {saldo:.2f}")
        print("==========================================")
        input("Pressione Enter para continuar...")
        
    elif opcao == "0":
        break
    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")


        