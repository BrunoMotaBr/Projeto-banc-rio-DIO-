menu = """
===== Bem vindo ao DIOBank =====
          [D] Deposito
          [E] Extrato
          [S] Saque
          [Q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).upper()

    if opcao == "D":
        print("Deposito")
        deposito = float(input("Qual valor do deposito: "))
        extrato += f"  Deposito: R${deposito:.2f} \n"
        saldo += deposito
        print(f"Deposito realizado novo saldo: {saldo:.2f}")


    elif opcao == "E":
        print("----- Extrato -----")
        if extrato != "":
            print(f"{extrato}")
            print(f"  Saldo: R${saldo:.2f}")
        else:
            print("Não ouve nenhuma movimentação em conta.")
        print("-------------------")

    elif opcao == "S":
        print("Saque")
        saque = float(input("Qual valor do saque: "))
        if numero_saques >= LIMITE_SAQUES:
            print("Você exedeu o limite diario de saques.")
        elif saque > limite or saque > saldo:
            resposta = "Não é possivel realizar esse saque pois exede o limite." if saque > limite else "Não é possivel realizar esse saque pois o valor é maior que o disponivel em conta."
            print(resposta)
        elif saque > 0:
            numero_saques += 1
            saldo -= saque
            extrato += f"  Saque: R${saque:.2f} \n"
            print(f"Saque realizado novo saldo: {saldo:.2f}")
        else: 
            print("Não é possivel SACAR VALORES NEGATIVOS.")

    elif opcao == "Q":
        print("Saindo...")
        break

    else:
        print("Opção invalida")