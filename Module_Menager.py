class ModuleManager:


    def __init__(self):

        self.modules = {}



    # =====================================
    # Registro de módulos
    # =====================================

    def register(self, name, module):

        self.modules[name] = module



    # =====================================
    # Buscar módulo
    # =====================================

    def get(self, name):

        return self.modules.get(name)



    # =====================================
    # Inicializar todos os módulos
    # =====================================

    def start_all(self):

        for name, module in self.modules.items():


            if hasattr(module, "start"):

                module.start()



    # =====================================
    # Encerrar todos os módulos
    # =====================================

    def stop_all(self):

        for name, module in self.modules.items():


            if hasattr(module, "stop"):

                module.stop()