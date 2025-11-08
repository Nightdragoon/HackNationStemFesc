from orchestrator import Orchestrator

if __name__ == "__main__":
    api_key = "AIzaSyDIk-w2E3o8Hk49_hPQCYQH_jlRbn-Du5U"  # Coloca aquí tu clave
    orchestrator = Orchestrator(api_key)

    topic = input("Ingresa un tema o texto base: ")
    orchestrator.run_discussion(topic)
