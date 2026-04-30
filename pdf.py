from docx import Document
from docx2pdf import convert
import os

# Pasta onde o pdf.py está
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def gerar_curriculo_pdf(texto_novo_objetivo):
    arquivo_base =  os.path.join(BASE_DIR, "Curriculo_Gabriel_Mansur.docx")
    
    print("Abrindo o template do currículo...")
    doc = Document(arquivo_base)

    texto_antigo = "Atuar como Estagiário na area de TI."
    
    substituiu = False
    for paragrafo in doc.paragraphs:
        if texto_antigo in paragrafo.text:
            paragrafo.text = paragrafo.text.replace(texto_antigo, texto_novo_objetivo)
            substituiu = True
            break

    if not substituiu:
        print("⚠️ Aviso: frase original do objetivo não encontrada no documento!")
        return

    word_temporario = os.path.join(BASE_DIR, "Curriculo_Temporario.docx")
    pdf_final = os.path.join(BASE_DIR, "Curriculo_Gabriel_Mansur_Atualizado.pdf")

    doc.save(word_temporario)

    print("Convertendo para PDF...")
    convert(word_temporario, pdf_final)

    os.remove(word_temporario)
    print(f"\n✅ Sucesso! Arquivo '{pdf_final}' criado e pronto para envio.")