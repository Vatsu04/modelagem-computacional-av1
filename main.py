import random
import numpy as np
import call as Call
import technician as Technician
from env import Environment  # Import your custom Environment class
from name_generator import generate_ticket_opener_names, generate_technician_names

# Parâmetros da simulação
SIM_DURATION = 100  # Duração da simulação (em unidades de tempo, ex.: minutos)
CALL_ARRIVAL_RATE = 2  # Taxa média de chegada de chamados (chamados por unidade de tempo)

# Gera o diretório de técnicos
technicians = generate_technician_names(10)  # Simulando com 10 técnicos
callers = generate_ticket_opener_names(10)  # Simulando com 10 chamadores


# Inicializa o ambiente do SimPy
env = Environment()  # Using your custom Environment class
technician_pool = [Technician.Technician(env, tech) for tech in technicians]  # Cria um pool de técnicos
caller_pool = [Call.Call(env, caller, random.randint(1, 10)) for caller in callers]  # Cria um pool de chamadores
# Lista para registrar os chamados
call_log = []


# Função para formatar o tempo no formato HH:MM:SS
def format_time(env_time):
    from datetime import datetime, timedelta
    start_time = datetime.now().replace(second=0, microsecond=0)  # Ponto de início da simulação
    simulation_time = start_time + timedelta(seconds=env_time)
    return simulation_time.strftime("%H:%M:%S")


# Processo para gerar chamados
def call_generator(env, call_log, technician_pool):
    call_id = 0
    while True:
        # Gera o tempo de chegada do próximo chamado usando uma distribuição exponencial
        yield env.timeout(random.expovariate(CALL_ARRIVAL_RATE))
        call_id += 1
        priority = random.randint(1, 4)  # Define uma prioridade aleatória para o chamado
        if(priority ==1):
            priority = "Baixa"
        elif(priority ==2):
            priority = "Média"
        elif(priority ==3):
            priority = "Alta"
        else:
            priority = "Crítica"
        new_call = Call.Call(env, call_id, priority)  # Usa a classe Call do módulo Call
        call_log.append(new_call)  # Adiciona o chamado ao log
        print(f"{format_time(env.now)}- Novo chamado criado com ID {call_id} e prioridade {priority}")
        env.process(assign_call(env, new_call, technician_pool))  # Processa a atribuição do chamado


# Processo para atribuir chamados aos técnicos disponíveis
def assign_call(env, call, technician_pool):
    # Verifica se há técnicos disponíveis
    available_tech = next((tech for tech in technician_pool if not tech.busy), None)
    if available_tech:
        call.assign_tech(available_tech)  # Atualiza o chamado com o técnico disponível
        resolve_time = random.randint(5, 15)  # Tempo aleatório para resolver o chamado
        env.process(available_tech.work_on_call(call, resolve_time))  # Técnico trabalha no chamado
        yield env.process(call.resolve(resolve_time))  # Simula a resolução do chamado
        
        # Escolhe o termo correto com base no gênero do técnico
        tecnico_ou_tecnica = "Técnica" if available_tech.gender == "Female" else "Técnico"
        print(f"{format_time(env.now)}- Chamado {call.call_id} resolvido por {tecnico_ou_tecnica} {call.call_tech}.")
    else:
        print(f"{format_time(env.now)}- Chamado {call.call_id} aguardando técnico disponível.")


# Inicia o gerador de chamados
env.process(call_generator(env, call_log, technician_pool))

# Executa a simulação
env.run(until=SIM_DURATION)

# Análise pós-simulação
resolved_calls = [call for call in call_log if call.end_time is not None]
average_response_time = np.mean(
    [(call.end_time - call.start_time) for call in resolved_calls]
)

from datetime import timedelta

# Converte o tempo médio (em segundos) para o formato HH:MM:SS
average_response_time_formatted = str(timedelta(seconds=average_response_time))
print("\n--- RESULTADOS DA SIMULAÇÃO ---")
print(f"Tempo médio de resposta: {average_response_time_formatted}")
print(f"Total de chamados resolvidos: {len(resolved_calls)}")
print(f"Chamados não resolvidos: {len(call_log) - len(resolved_calls)}")