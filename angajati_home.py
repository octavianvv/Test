import json


def citeste():
    nume = input("care este numele persoanei? ")
    varsta = input("care este varsta? ")
    return (nume, varsta)


date_persoana = citeste()

with open("angajati.json", "r") as fisier:
    content = json.load(fisier)
    content[date_persoana[0]] = date_persoana[1]
with open("angajati.json", "w") as fisier:
    json.dump(content, fisier, indent=2)
    print(f"angajatul{date_persoana[0]}:a fost adaugat in lista")

