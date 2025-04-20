import random
from datetime import datetime, timedelta

# Captura a hora atual como base
CURRENT_TIME = datetime.now().replace(second=0, microsecond=0)

def format_time(env_time):
    """
    Formata o tempo do ambiente para o formato HH:MM:SS.
    :param env_time: O tempo do ambiente (em segundos desde o início da simulação).
    """
    simulation_time = CURRENT_TIME + timedelta(seconds=env_time)
    return simulation_time.strftime("%H:%M:%S")


def dynamic_call_arrival_rate(env_time):
    """
    Ajusta a taxa de chegada dos chamados dependendo do tempo de simulação.
    :param env_time: O tempo do ambiente (em minutos ou segundos).
    """
    if 0 <= env_time % 1440 < 480:  # Madrugada (00:00 - 08:00)
        return 0.2  # Menos chamados (intervalos maiores)
    elif 480 <= env_time % 1440 < 960:  # Manhã (08:00 - 16:00)
        return 2  # Alta demanda (intervalos menores)
    else:  # Tarde/Noite (16:00 - 00:00)
        return 0.8  # Demanda moderada (intervalos intermediários)


def realistic_call_interval():
    """
    Gera um intervalo de tempo realista entre a chegada de chamados.
    Combina distribuições exponenciais com um intervalo mínimo.
    """
    min_interval = 50  # Intervalo mínimo de 50 segundos
    interval = random.expovariate(1 / 60)  # Média de 1 minuto
    return max(min_interval, interval)  # Garante o intervalo mínimo


def realistic_resolution_time(priority):
    """
    Gera um tempo de resolução realista baseado na prioridade do chamado.
    :param priority: A prioridade do chamado (Baixa, Média, Alta, Crítica).
    :return: Tempo de resolução em segundos.
    """
    if priority == "Baixa":
        mean, std_dev = 240, 45  # Média de 4 minutos
    elif priority == "Média":
        mean, std_dev = 180, 30  # Média de 3 minutos
    elif priority == "Alta":
        mean, std_dev = 120, 20  # Média de 2 minutos
    elif priority == "Crítica":
        mean, std_dev = 90, 15   # Média de 1,5 minuto
    else:
        mean, std_dev = 240, 45  # Default case
    return max(60, random.gauss(mean, std_dev))  # Garante que o tempo seja no mínimo 1 minuto


def technician_rest_time():
    """
    Retorna um tempo de descanso aleatório para o técnico entre os chamados.
    :return: Tempo de descanso em segundos.
    """
    rest_time = random.uniform(60, 180)  # Descanso de 1 a 3 minutos
    print(f"Debug: Tempo de descanso definido como {rest_time:.2f} segundos.")
    return rest_time