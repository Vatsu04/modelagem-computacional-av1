import random
import Functions.call as call
from Functions.name_generator import generate_ticket_title
from Functions.time_functions import format_time, realistic_call_interval, realistic_resolution_time


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

        new_call = call.Call(env, call_id, priority, generate_ticket_title())  # Cria novo chamado
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
                    # Verifica se o prazo expirou
            if env.now >= call.deadline:
                
                call.mark_unresolved()
                print(f"{format_time(env.now)}- Chamado {call.call_id} expirou e não foi resolvido.")
                return  # Sai da função após marcar como não resolvido

            # Aguarda 5 segundos antes de tentar atribuir novamente
            yield env.timeout(5)
        
            return  
