class Memory:

    def __init__(self):
        # Memória temporária da IA
        self.memory = {}

    def start(self):
        print("[MEMÓRIA] Módulo iniciado.")

    def stop(self):
        print("[MEMÓRIA] Módulo encerrado.")

    def save(self, key, value):
        """Salva uma informação na memória."""
        self.memory[key] = value

    def load(self, key):
        """Recupera uma informação da memória."""
        return self.memory.get(key)
