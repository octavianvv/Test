import json

nume = input("care este numele persoanei?")

with open("angajati.json") as fisier:
    content = json.load(fisier)

if nume in content.keys():
    raspuns = input(f"{nume} exista in dictionar,actualizam varsta?da/nu")
    if raspuns == "da":
        varsta = input("care este varsta persoanei?")

        content[nume] = varsta
else:
    varsta = input("care este varsta persoanei?")
    content[nume] = varsta

with open("angajati.json", "w") as fisier:
    json.dump(content, fisier, indent=4)

"""
#TODO creare functii pt citire din fisier,scriere in fisier si modificare content
#de citit despre functiile loads si dumps   json.loads,json.dumps
"""
