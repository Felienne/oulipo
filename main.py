import random

# before using this code, run:
# pip3 install -U spacy
# python3 -m spacy download nl_core_news_sm


import spacy
nlp = spacy.load("nl_core_news_sm")
import nl_core_news_sm
nlp = nl_core_news_sm.load()



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

def random_woord_van_type(boek, word_type):
    random_regel = random.choice(boek)
    doc = nlp(random_regel)
    for w in doc:
        if w.pos_ == word_type:
            return w.text

    return '.'


boek = lees_boek_in('romeo-en-julia.txt')

for i in range(5):
    zin = ''
    for j in range(10):
        woord = random_woord(boek)
        zin += woord + ' '
    print(zin + random_woord_van_type(boek, 'PUNCT'))



# mogelijke uitvoer:
# [('Dit', 'PRON'), ('is', 'AUX'), ('een', 'DET'), ('zin', 'NOUN'), ('.', 'PUNCT')]
