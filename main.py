import os
from IOHandler import IO
from APND import APND
def main():
    io = IO()
    cadeia: str
    automato: APND = io.ler_automato("automato.txt")

    if os.path.exists("cadeia.txt"):
        cadeia = io.ler_cadeia("cadeia.txt")
    else:
        print("[WARN] Arquivo 'cadeia.txt' não encontrado. Usando ""aabb"" como cadeia padrão.")
        cadeia = "aabb"

    print("\n[INFO] Cadeia lida: ", cadeia)
    
    if not automato.check_alfabeto(cadeia):
        print("[ERRO] A cadeia contém símbolos que não pertencem ao alfabeto do autômato.")
        print("❌ Cadeia REJEITADA (Contém símbolos fora do alfabeto)")
        return

    resultado = automato.processa_cadeia(cadeia)

if __name__ == "__main__":
    main()