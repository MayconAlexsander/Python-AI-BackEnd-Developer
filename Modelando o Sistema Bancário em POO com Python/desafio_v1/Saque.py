from desafio_v1 import Transacao

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        transacao_realizada = conta.sacar(self.valor)

        if transacao_realizada:
            conta.historico.addTransacao(self)