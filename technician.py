class technician:
    def __init__(self, name, id):
        self.tech_name = name # Nome do técnico
        self.tech_id = id # ID do técnico
        self.busy = False # Se o técnico está ocupado ou não
        self.current_call = None # Chamado atual que o técnico está atendendo
        self.calls = [] # Lista de chamados que o técnico atendeu


    