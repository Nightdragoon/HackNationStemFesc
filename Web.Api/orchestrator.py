import google.generativeai as genai
from sqlalchemy import Engine , Select , Insert
class Orchestrator:
    def __init__(self, api_key , engine , Base , guid):
        # Configurar API
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash")
        self.engine = engine
        self.Base = Base
        self.guid = guid

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
            f"Tu respuesta debe ser breve (4 a 6 oraciones) o menos de 300 caracteres, reflexiva y natural.\n"
            f"Responde específicamente al siguiente comentario anterior:\n\n"
            f"'{previous_message}'\n\n"
            f"Historial reciente de la conversación:\n{chr(10).join(self.history[-5:])}\n\n"
            f"Escribe tu respuesta como si realmente participaras en el diálogo. say everything in english"
        )

        response = self.model.generate_content(prompt)
        return response.text.strip()

    def run_discussion(self, topic):
        """Inicia una conversación entre los agentes sobre el tema dado."""

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
        smnt_first = Insert(self.Base.classes.conversacion).values(nombreAgente=first_agent['name'], mensajeAgente=first_reply,
                                                             idConversacion=self.guid)
        with self.engine.connect() as connection:
            connection.execute(smnt_first)
            connection.commit()

        # 2️⃣ Rondas de debate
        for round_num in range(2):
            for i, agent in enumerate(self.agents[1:] if round_num == 0 else self.agents):
                previous_message = self.history[-1]
                reply = self.generate_reply(agent, previous_message)
                line = f"{agent['name']}: {reply}"
                self.history.append(line)
                smnt = Insert(self.Base.classes.conversacion).values(nombreAgente = agent['name'] , mensajeAgente = reply , idConversacion = self.guid)
                with self.engine.connect() as connection:
                    connection.execute(smnt)
                    connection.commit()

        print("🧩 Fin de la discusión.\n")
