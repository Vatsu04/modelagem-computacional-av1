
from datetime import datetime, timedelta


class Technician:
    technician_id_counter = 0  # Contador global para atribuir IDs únicos aos técnicos
    

    def __init__(self, env, technician_data):
        """
        Inicializa um técnico.
        :param env: O ambiente de simulação do SimPy.
        :param technician_data: Dados do técnico (nome e gênero).
        """
        Technician.technician_id_counter += 1  # Incrementa o contador de IDs
        self.tech_name, self.gender = technician_data  # Nome e gênero do técnico
        self.technician_id = Technician.technician_id_counter  # Atribui um ID único ao técnico
        self.env = env  # O ambiente de simulação
        self.busy = False  # Indica se o técnico está ocupado ou não
        self.current_call = None  # Chamado atual que o técnico está atendendo
        self.start_time = datetime.now()  # Registra o tempo de início

    @staticmethod
    def format_time(env_time):
        """
        Formata o tempo do ambiente para o formato HH:MM:SS.
        :param env_time: O tempo do ambiente (em minutos ou segundos).
        """
        current_time = datetime.now()
        simulation_time = current_time + timedelta(seconds=env_time)
        return simulation_time.strftime("%H:%M:%S")

    def work_on_call(self, call, resolve_time):
        """
        Simula o trabalho do técnico em um chamado.
        :param call: O objeto do chamado.
        :param resolve_time: Tempo necessário para resolver o chamado.
        """
        self.busy = True
        self.current_call = call
        tecnico_ou_tecnica = "Técnica" if self.gender == "Female" else "Técnico"
        print(f"{self.format_time(self.env.now)}- {tecnico_ou_tecnica} {self.tech_name} começou a trabalhar no chamado {call.call_id}")
        yield self.env.timeout(resolve_time)  # Aguarda o tempo necessário para resolver o chamado
        print(f"{self.format_time(self.env.now)}- {tecnico_ou_tecnica} {self.tech_name} finalizou o chamado {call.call_id}")
        self.busy = False  # Marca o técnico como disponível novamente