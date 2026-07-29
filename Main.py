from Core import Core


def main():
    # Cria o cérebro da IA
    arg = Core()

    # Liga a IA
    arg.start()

    # Aqui ficará o loop principal futuramente
    # Enquanto a IA estiver ligada, ela ficará aguardando comandos.

    # Desliga a IA
    arg.stop()


if __name__ == "__main__":
    main()


    from Core import Core
from Memoria import Memory


def main():

    arg = Core()
    memoria = Memory()

    arg.start()
    memoria.start()

    memoria.save("nome", "Crhistyan")

    print(memoria.load("nome"))

    memoria.stop()
    arg.stop()


if __name__ == "__main__":
    main()

from Logger import Logger

logger = Logger()

logger.info("Sistema iniciado.")
logger.warning("Memória quase cheia.")
logger.error("Falha ao carregar módulo.")


from InputMenager import InputManager

input_manager = InputManager()

texto = input_manager.get_input()

print(texto)



from ComandProcessor import CommandProcessor


input_manager = InputManager()
processor = CommandProcessor()

texto = input_manager.get_input()

tipo = processor.process(texto)

print(tipo)