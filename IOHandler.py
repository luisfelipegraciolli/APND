from APND import APND

class IO:
    
    def ler_cadeia(self, file_name: str) -> str:
        with open(file_name, 'r', encoding='utf-8') as f:
            return f.read().strip()
        
    def ler_automato(self, file_name: str) -> APND:
        with open(file_name, 'r', encoding='utf-8') as f:
            linhas = [linha.strip() for linha in f if linha.strip() and not linha.startswith('#')]
        
        estados = (linhas[0].split(','))
        alfabeto = (linhas[1].split(','))
        estado_inicial = linhas[2].strip()
        estados_finais = (linhas[3].split(','))
        transicoes = []

        for linha in linhas[4:]:
            partes = linha.split(',')
            origem = partes[0].strip()
            destino = partes[1].strip()
            transicoes.append([s.strip() for s in origem.split(',')] + [destino])

        

        print("\n[INFO] Autômato carregado com sucesso:")
        print("Estados:", estados)
        print("Alfabeto:", alfabeto)
        print("Inicial:", estado_inicial)
        print("Finais:", estados)
        print("Transições:", transicoes)

        estados = set(estados)
        alfabeto = set(alfabeto)
        estado_inicial = linhas[2].strip()
        estados_finais = set(estados_finais)

        return APND(alfabeto, estados, estado_inicial, estados_finais, transicoes)
    