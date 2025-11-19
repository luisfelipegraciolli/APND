import os
from IOHandler import IO
from APND import APND
def main():
    io = IO()
    cadeia: str
    automato: APND = io.ler_automato("automato.txt")
    nome_arquivo_cadeia = "cadeia.txt"

    if os.path.exists(nome_arquivo_cadeia):
        cadeia = io.ler_cadeia(nome_arquivo_cadeia)
        print("[INFO] Cadeia lida do arquivo " + nome_arquivo_cadeia)
        
    else:
        print("[WARN] Arquivo 'cadeia.txt' não encontrado. Usando ""aabb"" como cadeia padrão.")
        cadeia = "aabb"

    print("\n[INFO] Cadeia carregada: ", cadeia)
    
    if not automato.check_alfabeto(cadeia):
        print("[ERRO] A cadeia contém símbolos que não pertencem ao alfabeto do autômato.")
        print("❌ Cadeia REJEITADA (Contém símbolos fora do alfabeto)")
        return

    automato.processa_cadeia(cadeia)

if __name__ == "__main__":
    main()