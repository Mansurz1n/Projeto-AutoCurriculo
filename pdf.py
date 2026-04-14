from docx import Document
from docx2pdf import convert
import os

def gerar_curriculo_pdf(texto_novo_objetivo):
    # O nome exato do arquivo que você fez upload
    arquivo_base = "Currículo Gabriel Mansur.docx"
    
    # 1. Abre o seu currículo em Word
    print("Abrindo o template do currículo...")
    doc = Document(arquivo_base)

    # A frase exata que está no seu currículo agora e será substituída
    texto_antigo = "Trabalhar como Estagiário na área de TI."
    
    # 2. Procura pela frase antiga e substitui pelo texto da IA
    substituiu = False
    for paragrafo in doc.paragraphs:
        if texto_antigo in paragrafo.text:
            paragrafo.text = paragrafo.text.replace(texto_antigo, texto_novo_objetivo)
            substituiu = True
            break # Como achamos o objetivo, não precisa olhar o resto do documento

    if not substituiu:
        print("Aviso: A frase original do objetivo não foi encontrada no documento!")
        return

    # 3. Salva um novo arquivo Word temporário
    word_temporario = "Curriculo_Temporario.docx"
    doc.save(word_temporario)

    # 4. Converte esse novo Word para PDF
    pdf_final = "Curriculo_Gabriel_Mansur_Atualizado.pdf"
    print("Convertendo para PDF. Isso pode levar alguns segundos...")
    convert(word_temporario, pdf_final)

    # 5. Apaga o Word temporário para deixar a pasta limpa
    os.remove(word_temporario)
    print(f"\n✅ Sucesso! Arquivo '{pdf_final}' criado e pronto para envio.")

# ==========================================
# Testando a função isoladamente (antes de plugar a IA)
# ==========================================
if __name__ == "__main__":
    # Um texto de teste simulando a resposta do Gemini
    texto_gemini = "Estudante de Engenharia de Software e Ciência de Dados com foco prático em Backend e Mobile. Busco aplicar meus conhecimentos em Python, Kotlin e SQL para otimizar os processos da empresa."
    
    gerar_curriculo_pdf(texto_gemini)