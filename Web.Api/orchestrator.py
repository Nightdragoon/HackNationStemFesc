import google.generativeai as genai

class Orchestrator:
    def __init__(self, api_key):
        # Configurar API
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash")

        # Agentes
        self.agents = [
            {"name": "Brandon", "role": "Analisis cientifico matematico"},
            {"name": "Rodrigo", "role": "Sociologo"},
            {"name": "Esve", "role": "Analisis cientifico fisico"},
            {"name": "Emmannuel", "role": "Analisis cientifico general"}
            
        ]

        # Historial de conversación
        self.history = []

    def generate_reply(self, agent, previous_message):
        """
        Genera una respuesta coherente según el último mensaje
        y el contexto de la conversación.
        """
        prompt = (
            f"Eres {agent['name']}, {agent['role']}.\n"
            f"Estás participando en un debate profesional sobre tecnología.\n"
            f"Tu respuesta debe ser breve (4 a 6 oraciones), reflexiva y natural.\n"
            f"Responde específicamente al siguiente comentario anterior:\n\n"
            f"'{previous_message}'\n\n"
            f"Historial reciente de la conversación:\n{chr(10).join(self.history[-5:])}\n\n"
            f"Escribe tu respuesta como si realmente participaras en el diálogo."
        )

        response = self.model.generate_content(prompt)
        return response.text.strip()

    def run_discussion(self, topic):
        """Inicia una conversación entre los agentes sobre el tema dado."""
        print(f"\n🧠 Conversación sobre: {topic}\n")

        # 1️⃣ Primer agente introduce el tema
        first_agent = self.agents[0]
        intro_prompt = (
            f"Eres {first_agent['name']}, {first_agent['role']}.\n"
            f"Introduce el tema '{topic}' explicando brevemente su relevancia hoy en día "
            f"en 4 a 6 oraciones, con tono reflexivo y profesional."
        )

        response = self.model.generate_content(intro_prompt)
        first_reply = response.text.strip()
        self.history.append(f"{first_agent['name']}: {first_reply}")
        print(f"{first_agent['name']}: {first_reply}\n")

        # 2️⃣ Rondas de debate
        for round_num in range(2):
            for i, agent in enumerate(self.agents[1:] if round_num == 0 else self.agents):
                previous_message = self.history[-1]
                reply = self.generate_reply(agent, previous_message)
                line = f"{agent['name']}: {reply}"
                print(line + "\n")
                self.history.append(line)

        print("🧩 Fin de la discusión.\n")
