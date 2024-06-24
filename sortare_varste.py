from faker import Faker
from random import randint
generator=Faker("ro_Ro")
perechi=[(generator.name(),randint(10,25))for _ in range(100)]
perechi_ordonate=sorted(perechi,key=lambda pereche:pereche[1])
print(perechi_ordonate)
#incarcare pe github folosind comanda gitremoteaddorigin