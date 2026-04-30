from GeminiAI import GeminiAi
from pdf import gerar_curriculo_pdf

def main():
    print("=== Gerador de Currículo Personalizado ===\n")
    
    print("Cole a descrição da vaga abaixo (pressione Enter duas vezes para finalizar):\n")
    linhas = []
    while True:
        linha = input()
        if linha == "":
            break
        linhas.append(linha)
    
    requisitos = "\n".join(linhas)
    
    if not requisitos.strip():
        print("❌ Nenhuma descrição informada. Encerrando.")
        return

    print("\n🤖 Gerando objetivo profissional com IA...")
    ia = GeminiAi()
    novo_objetivo = ia.perguntaCurriculo(requisitos)
    
    print(f"\n📝 Objetivo gerado:\n{novo_objetivo}\n")
    
    gerar_curriculo_pdf(novo_objetivo)

if __name__ == "__main__":
    main()