from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

class GeminiAi:

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY não encontrada no .env")
        self.client = genai.Client(api_key=api_key)

    def pergunta_aleatoria(self, pergunta):
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=pergunta,
        )
        return response.text

    def perguntaCurriculo(self, requisitos):
        response = self.client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f'''Atue como um especialista em recrutamento e seleção tech. Vou aplicar para uma vaga de estágio e preciso que você crie um "Objetivo Profissional" para o meu currículo que seja perfeitamente alinhado com o anúncio da empresa.

Regras essenciais para o texto:

Tamanho: Deve ser extremamente conciso (máximo de 2 a 3 linhas e no máximo 35 palavras). Meu currículo tem um limite estrito de 1 página e o espaço é apertado.

Perfil: Sou estudante de Engenharia de Software e Ciência de Dados. Tenho foco e projetos práticos em desenvolvimento Backend e Mobile (Python, Kotlin, SQL, Java, Node.js).

Conteúdo: Conecte o meu perfil atual com as principais palavras-chave e dores da vaga. Mostre como minhas habilidades e meu foco acadêmico podem agregar valor imediato como estagiário nessa posição específica.

Tom: Profissional, direto ao ponto e sem clichês genéricos.

IMPORTANTE: Retorne APENAS o texto do objetivo, sem introduções, sem títulos, sem explicações, sem markdown. Somente o parágrafo final pronto para colar no currículo.

Descrição da vaga alvo: {requisitos}''',
    )
        return response.text.strip()