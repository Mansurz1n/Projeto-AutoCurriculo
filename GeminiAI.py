from google import genai

class GeminiAi:

    def __init__(self):
        self.client = genai.Client()

        pass


    def pergunta_aleatoria(self,pergunta):
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=pergunta,
        )

        return response.text
    
    def perguntaCurriculo(self,requisitos):
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents='''Atue como um especialista em recrutamento e seleção tech. Vou aplicar para uma vaga de estágio e preciso que você crie um "Objetivo Profissional" para o meu currículo que seja perfeitamente alinhado com o anúncio da empresa.

Regras essenciais para o texto:



Tamanho: Deve ser extremamente conciso (máximo de 2 a 3 linhas e no máximo 35 palavras). Meu currículo tem um limite estrito de 1 página e o espaço é apertado.

Perfil: Sou estudante de Engenharia de Software e Ciência de Dados. Tenho foco e projetos práticos em desenvolvimento Backend e Mobile (Python, Kotlin, SQL, Java, Node.js).

Conteúdo: Conecte o meu perfil atual com as principais palavras-chave e dores da vaga. Mostre como minhas habilidades e meu foco acadêmico podem agregar valor imediato como estagiário nessa posição específica.

Tom: Profissional, direto ao ponto e sem clichês genéricos.

Descrição da vaga alvo:{requisitos}''',
        )
        return response.text
    
