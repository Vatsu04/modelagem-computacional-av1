import env as Env
from datetime import datetime, timedelta
from generate_caller_names import generate_ticket_opener_names
import random


class Call:
    call_id_counter = 0  # Contador global para atribuir IDs únicos aos chamados
    caller_names = generate_ticket_opener_names(100)  

    def __init__(self, env, call_type, call_wait):
        """
        Inicializa um objeto Call (Chamado).
        :param env: O ambiente de simulação (Env).
        :param call_type: Tipo de chamado (Prioridades: 1- Baixa, 2 - Média, 3 - Alta, 4 - Crítica).
        :param call_wait: Tempo de espera para um técnico ficar disponível.
        """
        self.caller_name = random.choice(Call.caller_names)  # Nome do chamador gerado aleatoriamente
        self.env = env  # O ambiente de simulação
        Call.call_id_counter += 1  # Incrementa o contador de IDs
        self.call_id = Call.call_id_counter  # Atribui um ID único ao chamado
        self.call_tech = None  # Técnico ainda não atribuído ao chamado
        self.call_time = self.format_time(env.now)  # Tempo de criação do chamado
        self.call_type = call_type  # Tipo de prioridade do chamado
        self.call_wait = call_wait  # Tempo de espera até um técnico atender o chamado
        self.start_time = 0.00  # Tempo em que o técnico começa a atender o chamado
        self.end_time = 0.00 # Tempo em que o chamado é fechado

    @staticmethod
    def format_time(env_time):
        """
        Formata o tempo do ambiente para o formato HH:MM:SS.
        :param env_time: O tempo do ambiente (em segundos desde o início da simulação).
        """
        current_time = datetime.now()
        simulation_time = current_time + timedelta(seconds=env_time)
        return simulation_time.strftime("%H:%M:%S")

    def assign_tech(self, technician):
        """
        Atribui um técnico ao chamado.
        :param technician: O técnico disponível.
        """
        self.call_tech = technician.tech_name  # Atualiza o nome do técnico no chamado
        self.start_time = self.env.now  # Registra o tempo de início do atendimento

    def close(self):
        """
        Fecha o chamado e registra o horário de término do atendimento.
        """
        self.end_time = self.env.now  # Registra o horário de término do chamado

    def resolve(self, resolve_time):
        """
        Simula o tempo necessário para resolver o chamado.
        :param resolve_time: Tempo para resolver o chamado.
        """
        yield self.env.timeout(resolve_time)
        self.end_time = self.env.now  # Registra o horário de término do chamado