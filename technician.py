from technician_name_generator import generate_technician_names
import random

# Generate a global list of technician names
technicians = generate_technician_names(100)

class Technician:
    def __init__(self, tech_id):
        # Assign a random name from the technicians list
        self.tech_name = random.choice(technicians)
        # Remove the assigned name from the list to ensure uniqueness
        technicians.remove(self.tech_name)
        self.tech_id = tech_id  # ID do técnico
        self.busy = False  # Se o técnico está ocupado ou não
        self.current_call = None  # Chamado atual que o técnico está atendendo
        self.calls = []  # Lista de chamados que o técnico atendeu

    def __repr__(self):
        return f"Technician(ID={self.tech_id}, Name={self.tech_name}, Busy={self.busy})"

# Generate a directory of 100 technicians with unique random names and IDs
def generate_technician_directory(count=100):
    return [Technician(tech_id) for tech_id in range(1, count + 1)]