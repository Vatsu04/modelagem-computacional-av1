import numpy as np
import math
import Functions.simulation as Simulation
import Functions.technician as Technician
from Functions.env import Environment  # Import your custom Environment class
from datetime import timedelta
from Functions.name_generator import generate_ticket_opener_names, generate_technician_names, generate_ticket_title
from Functions.time_functions import format_time, realistic_call_interval, realistic_resolution_time



# Parâmetros da simulação
SIM_DURATION = 3600  # Duração da simulação (em segundos, equivalente a 1 hora)

# Gera o diretório de técnicos e chamadores
technicians = generate_technician_names(8)  # Simulando com 8 técnicos
callers = generate_ticket_opener_names(30)  # Simulando com 30 chamadores

# Inicializa o ambiente do SimPy
env = Environment()  # Using your custom Environment class
technician_pool = [Technician.Technician(env, tech) for tech in technicians]  # Cria um pool de técnicos
call_log = []  # Lista para registrar os chamados


# Processo para gerar chamados



# Inicia o gerador de chamados
env.process(Simulation.call_generator(env, call_log, technician_pool))

# Executa a simulação
env.run(until=SIM_DURATION)



# Análise pós-simulação
# Chamados resolvidos
resolved_calls = [call for call in call_log if call.start_time is not None and call.end_time is not None]

# Chamados não resolvidos
unresolved_calls = [call for call in call_log if call.unresolved]

# Tempos de resposta para os chamados resolvidos
response_times = [
    (call.end_time - call.start_time)
    for call in resolved_calls
    if call.end_time >= call.start_time
]

# Calcular a média de tempos de resposta
if response_times:
    average_response_time = np.mean(response_times)  # Média em segundos
    average_response_time = max(0, average_response_time)  # Garantir que a média seja positiva
    average_response_time_rounded = math.ceil(average_response_time)  # Arredonda para o próximo segundo
    average_response_time_formatted = str(timedelta(seconds=average_response_time_rounded))  # Formata como HH:MM:SS
else:
    average_response_time_formatted = "N/A"  # Caso não haja tempos válidos

# Imprimir os resultados formatados
print("\n--- RESULTADOS DA SIMULAÇÃO ---")
print(f"Tempo médio de resposta: {average_response_time_formatted}")
print(f"Total de chamados resolvidos: {len(resolved_calls)}")
print(f"Chamados não resolvidos: {len(unresolved_calls)}")