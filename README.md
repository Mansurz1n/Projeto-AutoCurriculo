# 📄 AutoCurrículo

Gerador automático de currículo personalizado com IA. Cole a descrição de uma vaga e o projeto usa o **Google Gemini** para reescrever o objetivo profissional do seu currículo, exportando o resultado em PDF pronto para envio.

---

## ✨ Como funciona

1. Você cola a descrição da vaga no terminal
2. O Gemini gera um objetivo profissional alinhado à vaga
3. O script substitui o objetivo no template `.docx`
4. O arquivo é convertido e salvo como `.pdf`

---

## 🗂️ Estrutura do projeto

```
Projeto-AutoCurriculo/
│
├── main.py                        # Ponto de entrada da aplicação
├── GeminiAI.py                    # Integração com a API do Google Gemini
├── pdf.py                         # Manipulação do .docx e conversão para PDF
│
├── Curriculo_Gabriel_Mansur.docx  # Template base do currículo
│
├── .env                           # Chave da API (não versionar)
├── .gitignore
└── README.md
```

---

## ⚙️ Requisitos

- Python 3.10+
- Microsoft Word instalado (necessário para o `docx2pdf` no Windows)

### Instalar dependências

```bash
pip install google-genai python-docx docx2pdf python-dotenv
```

---

## 🔑 Configuração

Crie um arquivo `.env` na raiz do projeto com sua chave da API do Gemini:

```
GEMINI_API_KEY=sua_chave_aqui
```

> Você pode obter uma chave em: https://ai.google.dev/gemini-api/docs/api-key

---

## ▶️ Como usar

```bash
python main.py
```

Cole a descrição da vaga quando solicitado e pressione **Enter duas vezes** para confirmar. O arquivo `Curriculo_Gabriel_Mansur_Atualizado.pdf` será gerado na mesma pasta.

---

## 🛠️ Tecnologias

- [Google Gemini API](https://ai.google.dev/) — geração de texto com IA
- [python-docx](https://python-docx.readthedocs.io/) — manipulação de arquivos Word
- [docx2pdf](https://github.com/AlJohri/docx2pdf) — conversão Word → PDF
- [python-dotenv](https://github.com/theskumar/python-dotenv) — gerenciamento de variáveis de ambiente

---

## ⚠️ Observações

- O `docx2pdf` funciona **apenas no Windows** com Microsoft Word instalado
- Nunca suba o arquivo `.env` para o repositório — ele já está no `.gitignore`
- O template `.docx` precisa conter exatamente o texto `"Atuar como Estagiário na area de TI."` para a substituição funcionar

---

## 👤 Autor

**Gabriel Mansur**  
[github.com/Mansurz1n](https://github.com/Mansurz1n)
