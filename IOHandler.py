from APND import APND

class IO:
    
    def ler_cadeia(self, file_name: str) -> str:
        with open(file_name, 'r', encoding='utf-8') as f:
            return f.read().strip()
        
    def ler_automato(self, file_name: str) -> APND:
        with open(file_name, 'r', encoding='utf-8') as f:
            linhas = [linha.strip() for linha in f if linha.strip() and not linha.startswith('#')]
        
        alfabeto = linhas.pop(0)
        alfabeto_pilha = linhas.pop(0)
        estados = linhas.pop(0)
        estado_inicial = linhas.pop(0)  
        estados_finais = linhas.pop(0)
        transicoes = []

        for linha in linhas:
            transicoes.append(linha.split(','))

        print("\n[INFO] Autômato carregado com sucesso:")
        print("Alfabeto:", alfabeto)
        print("Alfabeto da Pilha:", alfabeto_pilha)
        print("Estados:", estados)
        print("Inicial:", estado_inicial)
        print("Finais:", estados)
        print("Transições:")
        for transicao in transicoes:
            print(transicao)

        alfabeto = set(alfabeto)
        alfabeto_pilha = set(alfabeto_pilha)
        estados = set(estados)
        estado_inicial = linhas[2].strip()
        estados_finais = set(estados_finais)

        return APND(alfabeto, alfabeto_pilha, estados, estado_inicial, estados_finais, transicoes)
    