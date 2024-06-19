# deschidere fisier
variabila = open("test.txt", "a+")#a=append r=read w=write
# citire continut fisier
content = variabila.read()
# citire produs de la tastatura
nume_produs = input("nume produs: ")
# modificam variabila content,adaugand un nou produs
variabila.write(f"\n{nume_produs}")
# inchidem fisierul
variabila.close()

#sa incarc pe github shopping_cart.py