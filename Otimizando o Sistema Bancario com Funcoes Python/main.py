import random

logado = False
usuarios = {}
LIMITE_SAQUE, LIMITE_QTD_SAQUES = 500, 3

def showLogin():
    print('''
[1] Entrar
[2] Cadastrar-se

[0] Sair
''')

def cadastrarUsuario(nome, data_nascimento, cpf, endereco):
    saldo = float(f"{random.uniform(300, 2500):.2f}")

    usuarios.update({
        cpf: {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "endereco": endereco,
            "CC": {
                "agencia": "0001",
                "n_conta": 1,
                "saldo": saldo,
                "extrato": "",
                "qtd_saques": 0
            }
        }
    })

    return usuarios

def showMenu(cpf):
    print(f'''
Agência: {usuarios[cpf]["CC"]["agencia"]} | Nº da Conta: {usuarios[cpf]["CC"]["n_conta"]}
Olá, {usuarios[cpf]["nome"]}. Saldo em conta: \033[92mR$ {usuarios[cpf]["CC"]["saldo"]}\033[0m

[1] Depósito
[2] Saque
[3] Extrato
[4] Nova Conta Corrente

[0] Logout
''')

def Deposito(saldo, extrato):
    deposito = float(input("Informe o valor do depósito: R$ "))

    while deposito <= 0:
        print("Valor inválido!")
        deposito = float(input("Informe o valor do depósito: R$ "))

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
        saque = float(input("Informe um valor para saque: R$ "))

        while (saque > LIMITE_SAQUE) or (saque > saldo) or (saque<=0):

            if (saque > saldo):
                print(f"Você informou um valor superior ao saldo para sacar. Seu saldo é R$ {saldo:.2f}")
            elif saque > LIMITE_SAQUE:
                print(f"Seu limite de saque é de R$ {LIMITE_SAQUE:.2f}. Tente novamente.")
            elif saque <= 0:
                print("Valor inválido!")

            saque = float(input("Informe um valor para saque: R$ "))

        qtd_saques += 1
        saldo -= saque
        print(f"\033[92mSaque de {saque:.2f} realizado com Sucesso!\033[0m")

        extrato += f"Saque: R$ {saque:.2f}\n"

        return saldo, extrato, qtd_saques

def Extrato(saldo,/,*,extrato):
    print(f"\033[90m===== EXTRATO BANCÁRIO =====\n{extrato if extrato != "" else "Não foram realizadas movimentações.\n"}\nSaldo: R$ {saldo:.2f}\033[0m")

def novaContaCorrente(cpf):
    usuarios[cpf]["CC"]["n_conta"] += 1

    return f"Foi criada uma nova Conta Corrente para o usuário {usuarios[cpf]["nome"]}."

while not logado:
    showLogin()
    option = int(input(">>> "))

    if option == 1:     # ENTRAR
        if usuarios == {}:
            print("Nenhum usuário cadastrado no sistema.")
        else:
            cpf = input("Informe seu CPF: ")

            while cpf not in usuarios:
                print("Nenhum usuário com este CPF foi encontrado.")
                cpf = input("Informe seu CPF: ")

            logado = True

    elif option == 2:   # CADASTRAR
        cpf = input("CPF: ")

        while cpf in usuarios:
            print("Este CPF já está cadastrado.")
            cpf = input("CPF: ")

        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
        endereco = input("Endereço (Rua, Nº, bairro, cidade/UF): ")

        cadastrarUsuario(nome, data_nascimento, cpf, endereco)

        print("Usuário cadastrado com sucesso! Entre para acessar sua conta.")

    elif option == 0:   # SAIR
        break
    else:
        print("Opção inválida!")
    
    while logado:
        showMenu(cpf)
        saldo = usuarios[cpf]["CC"]["saldo"]
        extrato = usuarios[cpf]["CC"]["extrato"]
        qtd_saques = usuarios[cpf]["CC"]["qtd_saques"]
        option = int(input(">>> "))

        if option == 1:   # DEPÓSITO
            usuarios[cpf]["CC"]["saldo"], usuarios[cpf]["CC"]["extrato"] = Deposito(saldo, extrato)

        elif option == 2: # SAQUE
            usuarios[cpf]["CC"]["saldo"], usuarios[cpf]["CC"]["extrato"], usuarios[cpf]["CC"]["qtd_saques"] = Saque(
                saldo=saldo, 
                extrato=extrato, 
                qtd_saques=qtd_saques, 
                LIMITE_SAQUE=LIMITE_SAQUE, 
                LIMITE_QTD_SAQUES=LIMITE_QTD_SAQUES
            )

        elif option == 3: # EXTRATO
            Extrato(saldo, extrato=extrato)

        elif option == 4: # NOVA CONTA CORRENTE
            print(novaContaCorrente(cpf))

        elif option == 0: # SAIR
            print("Fazendo Logout...")
            qtd_saques = 0
            logado = False
        else:
            print("Opção inválida!")