from technician_name_generator import generate_technician_names


technicians = generate_technician_names(100)

class Technician:
    technician_id_counter = 0  # Contador global para atribuir IDs únicos aos técnicos

    def __init__(self, env, technician):
        """
        Inicializa um técnico.
        :param env: O ambiente de simulação do SimPy.
        :param technician: Os dados do técnico (nome, ID, etc.).
        """
        Technician.technician_id_counter += 1  # Incrementa o contador de IDs
        self.technician_id = Technician.technician_id_counter  # Atribui um ID único ao técnico
        self.env = env  # O ambiente de simulação
        self.technician = technician  # Dados do técnico (use 'technician.tech_name' para acessar o nome)
        self.busy = False  # Indica se o técnico está ocupado ou não
        self.current_call = None  # Chamado atual que o técnico está atendendo

    def work_on_call(self, call, resolve_time):
        """
        Simula o trabalho do técnico em um chamado.
        :param call: O objeto do chamado.
        :param resolve_time: Tempo necessário para resolver o chamado.
        """
        self.busy = True
        self.current_call = call
        print(f"{self.env.now}: Técnico {self.technician.tech_name} começou a trabalhar no chamado {call.call_id}")
        yield self.env.timeout(resolve_time)  # Aguarda o tempo necessário para resolver o chamado
        self.busy = False
        self.current_call = None
        print(f"{self.env.now}: Técnico {self.technician.tech_name} finalizou o chamado {call.call_id}")