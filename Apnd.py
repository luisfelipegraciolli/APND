from typing import List

class APND():
    def __init__(self, alfabeto: set, alfabeto_pilha: set,estados: set, estado_inicial: str, estados_finais: set, transicoes: List[List[str]]):
        self.alfabeto = alfabeto
        self.alfabeto_pilha = alfabeto_pilha
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.transicoes = transicoes
        self.pilha: list = ['z0']  # Inicializa a pilha com o símbolo de fundo
        self.epsilon = 'ε'

    def check_alfabeto(self, cadeia: str) -> bool:
        """Verifica se todos os símbolos da cadeia pertencem ao alfabeto."""
        return set(cadeia).issubset(self.alfabeto)
    
    def check_cadeia(self, cadeia: str) -> bool:
        """Verifica se a cadeia está vazia."""
        return len(cadeia) == 0
    
    def processa_cadeia(self, cadeia: str):
        """Processa a cadeia usando o autômato APND."""
        print("\n[INFO] Iniciando o processamento da cadeia...")
        pass
        
