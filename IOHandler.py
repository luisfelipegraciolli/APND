from APND import APND

class IO:
    
    def ler_cadeia(self, file_name: str) -> str:
        with open(file_name, 'r', encoding='utf-8') as f:
            return f.read().strip()
        
    def ler_automato(self, file_name: str) -> APND:
        with open(file_name, 'r', encoding='utf-8') as f:
            linhas = [linha.strip() for linha in f if linha.strip() and not linha.strip().startswith('#')]

        if len(linhas) < 5:
            raise ValueError('Arquivo de autômato mal formatado: faltando seções')

        # Cabeçalhos
        alfabeto_line = linhas.pop(0)
        alfabeto_pilha_line = linhas.pop(0)
        estados_line = linhas.pop(0)
        estado_inicial_line = linhas.pop(0)
        estados_finais_line = linhas.pop(0)

        # Tokens
        alfabeto = [s.strip() for s in alfabeto_line.split(',') if s.strip()]
        alfabeto_pilha = [s.strip() for s in alfabeto_pilha_line.split(',') if s.strip()]
        estados = [s.strip() for s in estados_line.split(',') if s.strip()]
        estado_inicial = estado_inicial_line.strip()
        estados_finais = [s.strip() for s in estados_finais_line.split(',') if s.strip()]

        transicoes = []
        for linha in linhas:
            parts = [p.strip() for p in linha.split(',')]
            if parts:
                transicoes.append(parts)

        print("\n[INFO] Autômato carregado com sucesso:")
        print("Alfabeto:", alfabeto)
        print("Alfabeto da Pilha:", alfabeto_pilha)
        print("Estados:", estados)
        print("Inicial:", estado_inicial)
        print("Finais:", estados_finais)
        print("Transições:")
        for transicao in transicoes:
            print(transicao)

        # Converte para os formatos esperados
        alfabeto = set(alfabeto)
        alfabeto_pilha = set(alfabeto_pilha)
        estados = set(estados)
        estados_finais = set(estados_finais)

        return APND(alfabeto, alfabeto_pilha, estados, estado_inicial, estados_finais, transicoes)
    