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
    min_interval = 3  # Intervalo mínimo de 3 segundos
    interval = random.expovariate(1) * 10  # Média de 10 segundos
    return max(min_interval, interval)  # Garante o intervalo mínimo


def realistic_resolution_time(priority):
    """
    Gera um tempo de resolução realista baseado na prioridade do chamado.
    :param priority: A prioridade do chamado (Baixa, Média, Alta, Crítica).
    :return: Tempo de resolução em segundos.
    """
    if priority == "Baixa":
        mean, std_dev = 300, 60  # Média de 5 minutos com desvio padrão de 1 minuto
    elif priority == "Média":
        mean, std_dev = 240, 45  # Média de 4 minutos
    elif priority == "Alta":
        mean, std_dev = 180, 30  # Média de 3 minutos
    elif priority == "Crítica":
        mean, std_dev = 120, 20  # Média de 2 minutos
    else:
        mean, std_dev = 300, 60  # Default case
    return max(60, random.gauss(mean, std_dev))  # Garante que o tempo seja no mínimo 1 minuto


def technician_rest_time():
    """
    Retorna um tempo de descanso aleatório para o técnico entre os chamados.
    :return: Tempo de descanso em segundos.
    """
    return random.uniform(60, 300)  # Descanso de 1 a 5 minutos