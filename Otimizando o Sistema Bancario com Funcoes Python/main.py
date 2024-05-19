user, extrato = "USUÁRIO", ""
deposito, qtd_saques, saldo = 0, 0, 800
LIMITE_SAQUE, LIMITE_QTD_SAQUES = 500, 3

msg_deposito = "Informe o valor do depósito: R$ "
msg_saque = "Informe um valor para saque: R$ "

def Deposito(deposito, saldo, extrato):
    deposito = float(input(msg_deposito))

    while deposito <= 0:
        print("Valor inválido!")
        deposito = float(input(msg_deposito))

    saldo += deposito
    print(f"\033[92mDepósito de {deposito:.2f} realizado com Sucesso!\033[0m")

    extrato += f"Depósito: R$ {deposito:.2f}\n"

    return saldo, extrato

def Saque(saldo, extrato, qtd_saques, LIMITE_SAQUE, LIMITE_QTD_SAQUES):
    if qtd_saques >= LIMITE_QTD_SAQUES:
        print("\033[91mVocê atingiu a quantidade máxima de saques diários.\033[0m")
        return saldo, extrato, qtd_saques
    elif saldo <= 0:
        print("\033[91mVocê não possui saldo suficiente para realizar essa operação.\033[0m")
        return saldo, extrato, qtd_saques
    else:
        saque = float(input(msg_saque))

        while (saque > LIMITE_SAQUE) or (saque > saldo) or (saque<=0):

            if (saque > saldo):
                print(f"Você informou um valor superior ao saldo para sacar. Seu saldo é R$ {saldo:.2f}")
                saque = float(input(msg_saque))
            elif saque > LIMITE_SAQUE:
                print(f"Seu limite de saque é de R$ {LIMITE_SAQUE:.2f}. Tente novamente.")
                saque = float(input(msg_saque))
            elif saque <= 0:
                print("Valor inválido!")
                saque = float(input(msg_saque))

        qtd_saques += 1
        saldo -= saque
        print(f"\033[92mSaque de {saque:.2f} realizado com Sucesso!\033[0m")

        extrato += f"Saque: R$ {saque:.2f}\n"

        return saldo, extrato, qtd_saques

def Extrato(saldo,/,*,extrato):
    print(f"\033[90m===== EXTRATO BANCÁRIO =====\n{extrato}\nSaldo: R$ {saldo:.2f}\033[0m")

while True:
    menu = f'''
Olá, {user}. Saldo em conta: \033[92mR$ {saldo:.2f}\033[0m

[1] Depósito
[2] Saque
[3] Extrato

[0] Sair
'''
    print(menu)

    option = int(input())

    if option == 1:   # DEPÓSITO
        saldo, extrato = Deposito(deposito, saldo, extrato)

    elif option == 2: # SAQUE
        saldo, extrato, qtd_saques = Saque(
            saldo=saldo, 
            extrato=extrato, 
            qtd_saques=qtd_saques, 
            LIMITE_SAQUE=LIMITE_SAQUE, 
            LIMITE_QTD_SAQUES=LIMITE_QTD_SAQUES
        )

    elif option == 3: # EXTRATO
        Extrato(saldo, extrato=extrato)

    elif option == 0: # SAIR
        print("Fazendo Logout...")
        break
    else:
        print("Opção inválida!")