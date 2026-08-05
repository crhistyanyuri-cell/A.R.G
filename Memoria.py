import json
import os


class Memory:

    def __init__(self):

        self.folder = "Data"

        self.file = os.path.join(
            self.folder,
            "memory.json"
        )

        self.memory = {}

        self.create_folder()

        self.load_memory()


    def start(self):

        print("[MEMÓRIA] Módulo iniciado.")


    def stop(self):

        print("[MEMÓRIA] Módulo encerrado.")


    def create_folder(self):

        if not os.path.exists(self.folder):

            os.makedirs(self.folder)


    def save(self, key, value):

        self.memory[key] = value

        self.save_memory()


    def load(self, key):

        return self.memory.get(key)


    def delete(self, key):

        if key in self.memory:

            del self.memory[key]

            self.save_memory()


    def get_all(self):

        return self.memory


    def load_memory(self):

        if os.path.exists(self.file):

            try:

                with open(
                    self.file,
                    "r",
                    encoding="utf-8"
                ) as arquivo:

                    self.memory = json.load(
                        arquivo
                    )

            except json.JSONDecodeError:

                self.memory = {}


    def save_memory(self):

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as arquivo:

            json.dump(
                self.memory,
                arquivo,
                indent=4,
                ensure_ascii=False
            )