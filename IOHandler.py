from APND import APND

class IO:
    
    def ler_cadeia(self, file_name: str) -> str:
        with open(file_name, 'r', encoding='utf-8') as f:
            return f.read().strip()
        
    def ler_automato(self, file_name: str) -> APND:
        with open(file_name, 'r', encoding='utf-8') as f:
            linhas = f.readlines()
        
        alfabeto = set(linhas[0].strip().split(','))
        estados = set(linhas[1].strip().split(','))
        estado_inicial = linhas[2].strip()
        estados_finais = set(linhas[3].strip().split(','))
        
        transicoes = []
        for linha in linhas[4:]:
            partes = linha.strip().split('->')
            estado_atual = partes[0].strip

        print("\n[INFO] Autômato carregado com sucesso:")
        print("Estados:", estados)
        print("Alfabeto:", alfabeto)
        print("Inicial:", estado_inicial)
        print("Finais:", estados)
        print("Transições:", transicoes)

        return APND(alfabeto, estados, estado_inicial, estados_finais, transicoes)
    