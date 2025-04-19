import random

def generate_ticket_opener_names(count=100):
    first_names = [
        "Alice", "Brian", "Clara", "Derek", "Ella", "Felix", "Grace", "Hector", "Ivy", "Jack",
        "Kara", "Leo", "Mona", "Nathan", "Olive", "Peter", "Quincy", "Rachel", "Steve", "Tina",
        "Ulysses", "Vera", "Wes", "Xena", "Yara", "Zane", "Hugo", "Nina", "Oscar", "Paula",
        "Quinn", "Rita", "Sam", "Tasha", "Uma", "Victor", "Wendy", "Xavier", "Yvonne", "Zach",
        "Anita", "Bruce", "Cecilia", "Dennis", "Erin", "Freddie", "Giovanna", "Harold", "Isabel", "Jason",
        "Karen", "Lorenzo", "Melanie", "Norah", "Otto", "Phoebe", "Quentin", "Rafael", "Sophie", "Trevor",
        "Ursula", "Vincent", "Willow", "Ximena", "Yuri", "Zoey", "Fabio", "Claudio", "Marina", "Luisa",
        "Artur", "Juliana", "Carlos", "Nicolas", "Bárbara", "Fernanda", "Renata", "Adriano", "Sergio", "Camila"
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
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        openers.append(f"{first_name} {last_name}")
    
    return openers