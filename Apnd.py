from typing import List

class APND():
    def __init__(self, alfabeto: set, estados: set, estado_inicial: str, estados_finais: set, transicoes: List[List[str]]) -> None:
        self.alfabeto = alfabeto
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.transicoes = transicoes
        self.pilha: list = ['z0']  # Inicializa a pilha com o símbolo de fundo



    def push(self, char: str) -> None:
        pass

    def pop():
        pass