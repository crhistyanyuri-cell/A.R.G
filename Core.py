class Core:

    def __init__(self):

        # Informações da IA
        self.name = "A.R.G."
        self.version = "0.1.0"

        # Estado da IA
        self.running = False

    def start(self):

        self.running = True

        print("=" * 40)
        print(f"{self.name} v{self.version}")
        print("Sistema iniciado com sucesso.")
        print("=" * 40)

    def stop(self):

        self.running = False

        print("=" * 40)
        print("Sistema encerrado.")
        print("=" * 40)