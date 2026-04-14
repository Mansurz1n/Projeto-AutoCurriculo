from google import genai

class GeminiAi:

    def __init__(self):
        pass


    def pergunta_aleatoria(self,pergunta):
        client = genai.Client()

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=pergunta,
        )

        return response.text
        