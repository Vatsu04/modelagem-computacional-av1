import random


def generate_ticket_opener_names(count=100):
    # Define first names with associated genders
    first_names = [
        ("Alice", "Female"), ("Brian", "Male"), ("Clara", "Female"), ("Derek", "Male"), 
        ("Ella", "Female"), ("Felix", "Male"), ("Grace", "Female"), ("Hector", "Male"), 
        ("Ivy", "Female"), ("Jack", "Male"), ("Kara", "Female"), ("Leo", "Male"), 
        ("Mona", "Female"), ("Nathan", "Male"), ("Olive", "Female"), ("Peter", "Male"), 
        ("Quincy", "Male"), ("Rachel", "Female"), ("Steve", "Male"), ("Tina", "Female"),
  
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
        ("Emily", "Female"), ("Michael", "Male"), ("Sarah", "Female"), ("David", "Male"),
        ("Ashley", "Female"), ("Gustavo", "Male"), ("Lucas", "Male"), ("Guilherme", "Male"), ("Sabrina", "Female"),
        ("Hannibal", "Male")
    ]

    last_names = [
    "Smith", "Johnson", "Brown", "Williams", "Jones", "Garcia", "Miller", "Davis", "Martinez", "Hernandez",
    "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee",
    "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker",
    "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green", "Adams", 
    "Tascheri", "Suares", "Afton", "Lecter", "Graham", "Brito", "Coutinho", "do Valle", "Kennedy"
]

    technicians = []

    for _ in range(count):
        first_name, gender = random.choice(first_names)
        last_name = random.choice(last_names)
        full_name = f"{first_name} {last_name}"
        technicians.append((full_name, gender))  # Return the full name and gender as a tuple
    
    return technicians