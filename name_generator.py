import random


def generate_ticket_opener_names(count=100):
    # Define first names with associated genders
    first_names = [
        ("Alice", "Female"), ("Brian", "Male"), ("Clara", "Female"), ("Derek", "Male"), 
        ("Ella", "Female"), ("Felix", "Male"), ("Grace", "Female"), ("Hector", "Male"), 
        ("Ivy", "Female"), ("Jack", "Male"), ("Kara", "Female"), ("Leo", "Male"), 
        ("Mona", "Female"), ("Nathan", "Male"), ("Olive", "Female"), ("Peter", "Male"), ("Momo", "Female"), ("Sana", "Female"), ("Chaeyoung", "Female"),
        ("Quincy", "Male"), ("Rachel", "Female"), ("Steve", "Male"), ("Tina", "Female"), ("Nayeon", "Female")

  
    ]

    last_names = [
        "Taylor", "Bishop", "Chavez", "Mendoza", "Fisher", "Patel", "Reed", "Hicks", "Myers", "Ford",
        "Cruz", "Morales", "Stewart", "Diaz", "Rogers", "Reyes", "Edwards", "Carter", "Collins", "Murphy",
        "Bell", "Gutierrez", "Bailey", "Cooper", "Richardson", "Howard", "Ward", "Cox", "Torres", "Peterson",
        "Gray", "Ramsey", "Sanders", "Price", "Bennett", "Wood", "Barnes", "Ross", "Henderson", "Coleman",
        "Jenkins", "Perry", "Powell", "Long", "Patterson", "Hughes", "Flores", "Washington", "Butler", "Simmons",
        "Foster", "Gonzales", "Bryant", "Alexander", "Russell", "Griffin", "Hayes", "Chapman", "Webb", "West",
        "Pereira", "Moreira", "Teixeira", "Almeida", "Silva", "Oliveira", "Souza", "Ferreira", "Pinto", "Lima",
        "Rocha", "Carvalho", "Barbosa", "Rezende", "Montenegro", "Batista", "Vasquez", "Campos", "Ramos", "Vieira"
    ]
    openers = []

    for _ in range(count):
        first_name, gender = random.choice(first_names)
        last_name = random.choice(last_names)
        full_name = f"{first_name} {last_name}"
        openers.append((full_name, gender))  # Return the full name and gender as a tuple
    
    return openers

def generate_technician_names(count=100):
    # Define first names with associated genders
    first_names = [
        ("John", "Male"), ("Jane", "Female"), ("Alex", "Male"), ("Chris", "Male"), 
        ("Taylor", "Female"), ("Morgan", "Male"), ("Casey", "Female"), ("Jamie", "Female"),
        ("Emily", "Female"), ("Michael", "Male"), ("Sarah", "Female"), ("David", "Male"), ("Rian", "Male"),
        ("Ashley", "Female"), ("Gustavo", "Male"), ("Lucas", "Male"), ("Guilherme", "Male"), ("Sabrina", "Female"), ("Caue", "Male"), ("Yone", "Female"),
        ("Hannibal", "Male"), ("Samuel", "Male"), ("Clarice", "Female"), ("Will", "Female"), ("Geraldo", "Male"), ("Eduardo", "Male"), ("Anna", "Female"), 
        ("Lia", "Female"), ("Dahyun", "Female"), ("Tzuyu", "Female"), ("Mina", "Female"), ("Jeongyeon", "Female"), ("Fernanda", "Female")
    ]

    last_names = [
    "Smith", "Johnson", "Brown", "Williams", "Jones", "Garcia", "Miller", "Davis", "Martinez", "Hernandez",
    "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee",
    "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker",
    "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green", "Adams", 
    "Tascheri", "Suares", "Afton", "Lecter", "Graham", "Brito", "Coutinho", "do Valle", "Kennedy", "Teske", "Alves", "Lima", "Melo", "Pereira", "Moreira", "Teixeira", "Almeida", "Silva", "Oliveira", "Souza",
    "Ferreira", "Pinto", "Lima", "Rocha", "Carvalho", "Barbosa", "Rezende", "Montenegro", "Batista", "Vasquez", "Campos", "Ramos", "Vieira"
]

    technicians = []

    for _ in range(count):
        first_name, gender = random.choice(first_names)
        last_name = random.choice(last_names)
        full_name = f"{first_name} {last_name}"
        technicians.append((full_name, gender))  # Return the full name and gender as a tuple
    
    return technicians


import random

def generate_ticket_title():
    # Problemas recorrentes em empresas
    categories = [
        "Reiniciar senha", "Problema de conexão com a internet", "Lentidão no sistema",
        "Mouse não funciona", "Teclado com defeito", "Impressora sem papel", 
        "Erro ao abrir programa", "Sistema operacional travando", "Atualização pendente",
        "Problema na VPN", "E-mail corporativo inacessível", "Monitor não liga", 
        "Configuração de software", "Solicitação de acesso a pastas", "Tela azul da morte",
        "Erro de autenticação", "Problema com certificado digital", "Microfone não funciona",
        "Câmera não é detectada", "Erro de rede local", "Computador não liga", 
        "Driver desatualizado", "Solicitação de instalação de software", "Problema com backup",
        "Erro no sistema de ponto eletrônico", "Conexão instável no Wi-Fi",
        "Solicitação de troca de equipamento", "Problema com licenciamento de software",
        "Solicitação de suporte remoto", "Erro de sincronização com o servidor",
        "Som não está funcionando", "Erro ao imprimir documentos", "Falta de espaço no disco",
        "Problema com o firewall", "Conexão lenta na videoconferência", 
        "Erro ao salvar arquivos", "Solicitação de permissão de administrador",
        "Mouse com duplo clique automático", "Teclado com teclas travadas",
        "Problema com atualização de antivírus"
    ]

    # Escolhe e retorna um título aleatório da lista
    return random.choice(categories)
