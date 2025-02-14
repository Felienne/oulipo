import random


def lees_boek_in(bestandsnaam):
    file = open(bestandsnaam, "r")
    content = file.readlines()
    file.close()
    return content


def random_woord(boek):
    random_regel = random.choice(boek)
    while len(random_regel) < 10:
        random_regel = random.choice(boek)

    woordenlijst = random_regel.split(' ')
    woordenlijst = [x for x in woordenlijst if '\n' not in x]
    return random.choice(woordenlijst)


boek = lees_boek_in('romeo-en-julia.txt')

for i in range(5):
    zin = ''
    for j in range(10):
        woord = random_woord(boek)
        zin += woord + ' '
    print(zin)


