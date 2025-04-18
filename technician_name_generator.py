import random

def generate_technician_names(count=100):
    first_names = [
    "John", "Jane", "Alex", "Chris", "Taylor", "Jordan", "Morgan", "Casey", "Jamie", "Drew",
    "Emily", "Michael", "Sarah", "David", "Ashley", "Matthew", "Jessica", "Daniel", "Sophia", "Vergil",
    "Olivia", "Benjamin", "Emma", "Liam", "Ava", "Noah", "Isabella", "Lucas", "Mia", "Mason",
    "Amelia", "Dante", "Charlotte", "Elijah", "Harper", "Henry", "Evelyn", "Oliver", "Abigail", "James",
    "Gustavo", "Sabrina", "Guilherme", "Mauricio", "Daniel", "William", "Hannibal", "Will", "Michael", "Elizabeth", "Leon"
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
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        technicians.append(f"{first_name} {last_name}")
    
    return technicians
