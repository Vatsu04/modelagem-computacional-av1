import random
import numpy as np
import call as Call
import math
import technician as Technician
from env import Environment  # Import your custom Environment class
from datetime import timedelta
from name_generator import generate_ticket_opener_names, generate_technician_names, generate_ticket_title
from time_functions import format_time, realistic_call_interval, realistic_resolution_time

# Parâmetros da simulação
SIM_DURATION = 3600  # Duração da simulação (em segundos, equivalente a 1 hora)

# Gera o diretório de técnicos e chamadores
technicians = generate_technician_names(5)  # Simulando com 10 técnicos
callers = generate_ticket_opener_names(10)  # Simulando com 100 chamadores

# Inicializa o ambiente do SimPy
env = Environment()  # Using your custom Environment class
technician_pool = [Technician.Technician(env, tech) for tech in technicians]  # Cria um pool de técnicos
call_log = []  # Lista para registrar os chamados


# Processo para gerar chamados
def call_generator(env, call_log, technician_pool):
    call_id = 0
    while True:
        # Gera o tempo de chegada do próximo chamado com intervalo realista
        yield env.timeout(realistic_call_interval())
        call_id += 1
        priority_level = random.choices(
        population=[1, 2, 3, 4],  # Baixa, Média, Alta, Crítica
        weights=[4, 3, 2, 1],     # Mais chances de gerar prioridade baixa
        k=1
        )[0]
        priority = ["Baixa", "Média", "Alta", "Crítica"][priority_level - 1]  # Define uma prioridade aleatória para o chamado

        new_call = Call.Call(env, call_id, priority, generate_ticket_title() )  # Cria novo chamado
        call_log.append(new_call)  # Adiciona o chamado ao log
        
        print(f"{format_time(env.now)}- Novo chamado '{new_call.call_title}' criado com ID {call_id} e prioridade {priority} por {new_call.caller_name}.")
        
        # Processa a atribuição do chamado
        env.process(assign_call(env, new_call, technician_pool))


# Processo para atribuir chamados aos técnicos disponíveis
def assign_call(env, call, technician_pool):
    while True:  # Loop contínuo para tentar atribuir o chamado
        # Verifica se há técnicos disponíveis
        available_tech = next((tech for tech in technician_pool if not tech.busy), None)
        if available_tech:
            call.assign_tech(available_tech)  # Atualiza o chamado com o técnico disponível
            resolve_time = realistic_resolution_time(call.call_type)  # Tempo de resolução
            env.process(available_tech.work_on_call(call, resolve_time))  # Técnico trabalha no chamado
            yield env.process(call.resolve(resolve_time))  # Simula a resolução do chamado
            return  # Sai da função após atribuir o técnico

        # Verifica se o prazo expirou
        if env.now >= call.deadline:
            call.mark_unresolved()
            print(f"{format_time(env.now)}- Chamado {call.call_id} expirou e não foi resolvido.")
            return  # Sai da função após marcar como não resolvido

        # Aguarda 5 segundos antes de tentar atribuir novamente
        yield env.timeout(5)
    


# Inicia o gerador de chamados
env.process(call_generator(env, call_log, technician_pool))

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