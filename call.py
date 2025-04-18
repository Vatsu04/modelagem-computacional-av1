import env as env

class Call:

    call_id_counter = 0
    
    def __init__(self, env, call_type, call_wait):
        self.env = env
        Call.call_id_counter += 1 # ID do chamado
        self.call_id = Call.call_id_counter
        self.call_tech = self.define_tech() #Pega o nome do técnico de acordo com o ID do técnico
        self.call_time = env.now() # Tempo de criação do chamado
        self.call_type = call_type # Tipo de chamado (Prioridades: 1- Baixa, 2 - Média, 3 - Alta, 4 - Crítica)
        self.call_wait = call_wait # Tempo de de algum técnico para se colocar como disponível para atender o chamado
        self.start_time = env.now #Tempo do técnico para atender o chamado
        self.end_time = None # Horário de fechamento do chamado

    def close(self): 
        self.end_time = self.env.now

    def define_tech(self, id):
        return env.technicians[id].tech_name # Pega o nome do técnico de acordo com o ID do técnico
    

      