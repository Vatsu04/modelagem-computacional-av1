import simpy

class Environment(simpy.Environment):
    def __init__(self):
        super().__init__()
        self.now = 0  # Custom attribute to track time

    def get_now(self):
        """
        Retorna o tempo atual do ambiente simulado.
        """
        return self.now