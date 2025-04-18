import env

def now():
    """
    Retorna o tempo atual do ambiente simulado.
    """
    return env.now

class Call:
    def __init__(self, env, call_id, call_type, call_wait):
        self.env = env
        self.call_id = call_id
        self.call_time = now() # Tempo de criação do chamado
        self.call_type = call_type # Tipo de chamado (Prioridades: 1- Baixa, 2 - Média, 3 - Alta, 4 - Crítica)
        self.call_wait = call_wait # Tempo de de algum técnico para se colocar como disponível para atender o chamado
        self.start_time = env.now #Tempo do técnico para atender o chamado
        self.end_time = None # Horário de fechamento do chamado

    def close(self):
        self.end_time = self.env.now

