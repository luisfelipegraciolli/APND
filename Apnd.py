from typing import List

class APND():
    def __init__(self, alfabeto: set, alfabeto_pilha: set,estados: set, estado_inicial: str, estados_finais: set, transicoes: List[List[str]]):
        self.alfabeto = alfabeto
        self.alfabeto_pilha = alfabeto_pilha
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.transicoes = transicoes
        # Inicializa a pilha: se houver símbolo de fundo 'Z' no alfabeto da pilha,
        # coloca-o como marcador de fundo. Caso contrário, inicia vazia.
        if 'Z' in self.alfabeto_pilha:
            self.pilha: list = ['Z']
        else:
            self.pilha: list = []
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
        
        # Usa BFS para explorar todos os caminhos possíveis (não-determinismo)
        # Cada estado é representado por: (posição na cadeia, estado atual, pilha)
        from collections import deque
        
        fila = deque([(0, self.estado_inicial, self.pilha.copy())])
        aceitas = []
        
        while fila:
            pos, estado, pilha = fila.popleft()
            
            # Exibe o processamento
            simbolo_atual = cadeia[pos] if pos < len(cadeia) else 'ε'
            topo_pilha = pilha[-1] if pilha else 'vazio'
            print(f"[δ] Posição: {pos}, Estado: {estado}, Topo da pilha: {topo_pilha}, Símbolo: {simbolo_atual}")
            
            # Verifica se chegou ao final da cadeia e a pilha está vazia (aceitação por pilha vazia)
            if pos == len(cadeia) and pilha == []:
                aceitas.append((estado, pilha.copy()))
                print(f"✅ CAMINHO ACEITO (pilha vazia): Estado {estado}, Pilha: {pilha}")
                continue
            
            # Procura transições aplicáveis
            for transicao in self.transicoes:
                estado_origem = transicao[0]
                simbolo_entrada = transicao[1]
                topo = transicao[2]
                estado_destino = transicao[3]
                simbolos_saida = transicao[4]
                
                # Verifica se a transição é aplicável
                if estado_origem == estado and topo == topo_pilha:
                    # Transição com símbolo
                    if simbolo_entrada != self.epsilon and pos < len(cadeia) and cadeia[pos] == simbolo_entrada:
                        nova_pilha = pilha[:-1]  # Remove o topo
                        # Adiciona os símbolos de saída (se não for ε) na ordem inversa
                        if simbolos_saida != self.epsilon and simbolos_saida != '':
                            for simbolo in reversed(simbolos_saida):
                                nova_pilha.append(simbolo)

                        nova_pilha_copia = nova_pilha.copy()
                        fila.append((pos + 1, estado_destino, nova_pilha_copia))
                    
                    # Transição epsilon (sem consumir símbolo)
                    elif simbolo_entrada == self.epsilon:
                        nova_pilha = pilha[:-1]  # Remove o topo
                        # Adiciona os símbolos de saída (se não for ε) na ordem inversa
                        if simbolos_saida != self.epsilon and simbolos_saida != '':
                            for simbolo in reversed(simbolos_saida):
                                nova_pilha.append(simbolo)

                        nova_pilha_copia = nova_pilha.copy()
                        fila.append((pos, estado_destino, nova_pilha_copia))
        
        # Resultado final
        print("\n" + "="*60)
        if aceitas:
            print(f"✅ Cadeia ACEITA pelo autômato APND!")
            print(f"Número de caminhos de aceitação: {len(aceitas)}")
            return True
        else:
            print("❌ Cadeia REJEITADA pelo autômato APND!")
            return False
        
