
def menu():
    menu = """
    ╔════════════════════════════╗
    ║  Bem Vindo ao Lira Bank V2 ║
    ╠════════════════════════════╣
    ║ [d]  Depositar             ║
    ║ [s]  Sacar                 ║
    ║ [e]  Extrato               ║
    ║ [nc] Nova Conta            ║
    ║ [lc] Listar Contas         ║
    ║ [nu] Novo Usuario          ║
    ║ [q] Sair                   ║
    ╚════════════════════════════╝
    =>"""
    return input(menu)

def depositar (saldo,valor,extrato,/):
    if valor > 0:
        saldo += valor
        extrato += "Deposito: R${valor:.2f}\n"
        print("===================================")
        print("        Depósito Realizado         ")
        print("-----------------------------------")
        print(f"Valor depositado: R${valor:.2f}")
        print(f"Saldo atual: R${saldo:.2f}")
        print("===================================")
    else:
        print("Falha no deposito! O valor informado é inválido.")
    return saldo, extrato

def sacar(*,saldo,valor,extrato,limite,numero_saques,limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
            print("Saque cancelado! Você não tem saldo suficiente!")
    elif excedeu_limite:
            print("Saque cancelado! Você não tem limite disponível!")
    elif excedeu_saques:
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
    else:
        print("Operação falhou! O valor informado não é valido!")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    print("\n╔══════════════════════════════════════════════╗")
    print("║             Cadastro de Novo Usuário         ║")
    print("╠══════════════════════════════════════════════╣")
    cpf = input("║ CPF (somente números): \n║ =>")
    nome = input("║ Nome completo: \n║ => ")
    data_nascimento = input("║ Data de nascimento (dd-mm-aaaa): \n║ => ")
    endereco = input("║ Endereço (logradouro, nro - bairro - cidade/sigla estado): \n║ =>")
    print("╚══════════════════════════════════════════════╝")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("═══ Usuário criado com sucesso! ═══")




def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n═══ Usuário não encontrado, fluxo de criação de conta encerrado! ═══")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
     