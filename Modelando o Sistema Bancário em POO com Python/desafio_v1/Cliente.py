class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizarTransacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def addConta(self, conta):
        self.contas.append(conta)