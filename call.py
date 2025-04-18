import env as Env
from datetime import datetime

class Call:
    call_id_counter = 0  # Contador global para atribuir IDs únicos aos chamados

    def __init__(self, env, call_type, call_wait):
        """
        Inicializa um objeto Call (Chamado).
        :param env: O ambiente de simulação (Env).
        :param call_type: Tipo de chamado (Prioridades: 1- Baixa, 2 - Média, 3 - Alta, 4 - Crítica).
        :param call_wait: Tempo de espera para um técnico ficar disponível.
        """
        self.env = env  # O ambiente de simulação
        Call.call_id_counter += 1  # Incrementa o contador de IDs
        self.call_id = Call.call_id_counter  # Atribui um ID único ao chamado
        self.call_tech = None  # Técnico ainda não atribuído ao chamado
        self.call_time = self.get_current_time()  # Tempo de criação do chamado
        self.call_type = call_type  # Tipo de prioridade do chamado
        self.call_wait = call_wait  # Tempo de espera até um técnico atender o chamado
        self.start_time = None  # Tempo em que o técnico começa a atender o chamado
        self.end_time = None  # Tempo em que o chamado é fechado

    def assign_tech(self, tech_id):
        """
        Atribui um técnico ao chamado.
        :param tech_id: O ID do técnico disponível.
        """
        self.call_tech = Env.technicians[tech_id].tech_name  # Atribui o nome do técnico ao chamado
        self.start_time = self.env.now  # Registra o tempo de início do atendimento

    def close(self):
        """
        Fecha o chamado e registra o horário de término do atendimento.
        """
        self.end_time = self.env.now  # Registra o horário de término do chamado

    @staticmethod
    def get_current_time():
        """
        Retorna o horário atual formatado como uma string no formato HH:MM:SS.
        """
        now = datetime.now()
        return now.strftime("%H:%M:%S")