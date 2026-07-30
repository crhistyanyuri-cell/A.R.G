import json
import os


class Memory:

    def __init__(self):

        self.file = "memory.json"

        self.memory = {}

        self.load_memory()


    def start(self):

        print("[MEMÓRIA] Módulo iniciado.")


    def stop(self):

        print("[MEMÓRIA] Módulo encerrado.")


    def save(self, key, value):

        """Salva uma informação na memória."""

        self.memory[key] = value

        self.save_memory()


    def load(self, key):

        """Recupera uma informação da memória."""

        return self.memory.get(key)


    def load_memory(self):

        """Carrega a memória salva no arquivo."""

        if os.path.exists(self.file):

            with open(self.file, "r", encoding="utf-8") as arquivo:

                self.memory = json.load(arquivo)


    def save_memory(self):

        """Salva a memória no arquivo."""

        with open(self.file, "w", encoding="utf-8") as arquivo:

            json.dump(
                self.memory,
                arquivo,
                indent=4,
                ensure_ascii=False
            )
