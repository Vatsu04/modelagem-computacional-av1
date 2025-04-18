import simpy
import random
import numpy as np
import matplotlib.pyplot as plt
import call as Call
import technician as Technician
import env as Env



# Parâmetros da simulação
SIM_DURATION = 100  # Duração da simulação em unidades de tempo (ex.: minutos)
CALL_ARRIVAL_RATE = 2  # Taxa média de chegada de chamados por unidade de tempo

# Gera o diretório de técnicos
technicians = Technician.generate_technician_directory(10)  # Simulando com 10 técnicos

# Inicializa o ambiente do SimPy
env = simpy.Environment()
technician_pool = [Technician.Technician(env, tech) for tech in technicians]  # Cria um pool de técnicos

# Lista para registrar os chamados
call_log = []


# Processo para gerar chamados
def call_generator(env, call_log, technician_pool):
    call_id = 0
    while True:
        # Gera o tempo de chegada do próximo chamado usando uma distribuição exponencial
        yield env.timeout(random.expovariate(CALL_ARRIVAL_RATE))
        call_id += 1
        priority = random.randint(1, 4)  # Define uma prioridade aleatória para o chamado
        new_call = Technician.Call(env, call_id, priority)  # Use a classe Call do módulo Technician
        call_log.append(new_call)  # Adiciona o chamado ao log
        print(f"{env.now}: Novo chamado criado com ID {call_id} e prioridade {priority}")
        env.process(assign_call(env, new_call, technician_pool))  # Processa a atribuição do chamado


# Processo para atribuir chamados aos técnicos disponíveis
def assign_call(env, call, technician_pool):
    # Verifica se há técnicos disponíveis
    available_tech = next((tech for tech in technician_pool if not tech.busy), None)
    if available_tech:
        resolve_time = random.randint(5, 15)  # Tempo aleatório para resolver o chamado
        env.process(available_tech.work_on_call(call, resolve_time))  # Técnico trabalha no chamado
        yield env.process(call.resolve(resolve_time))  # Simula a resolução do chamado
        print(f"{env.now}: Chamado {call.call_id} resolvido.")
    else:
        print(f"{env.now}: Chamado {call.call_id} aguardando técnico disponível.")


# Inicia o gerador de chamados
env.process(call_generator(env, call_log, technician_pool))

# Executa a simulação
env.run(until=SIM_DURATION)

# Análise pós-simulação
resolved_calls = [call for call in call_log if call.end_time is not None]
average_response_time = np.mean([call.end_time - call.start_time for call in resolved_calls])

print("\n--- RESULTADOS DA SIMULAÇÃO ---")
print(f"Tempo médio de resposta: {average_response_time:.2f} unidades de tempo")
print(f"Total de chamados resolvidos: {len(resolved_calls)}")
print(f"Chamados não resolvidos: {len(call_log) - len(resolved_calls)}")