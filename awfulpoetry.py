#!/usr/bin/env python3
import random

articles=['a','the']
nouns=['cat','dragon','pyton','gun','grind','Archangelsk']
verbs=['catch','throw','try','left','make','do']
adverbs=['well','highly','annoyingly','fully']

for x in range(5):
    choice=random.randint(0,1)
    if choice==0:
        print(articles[random.randint(0,len(articles)-1)],
              ' ',nouns[random.randint(0,len(nouns)-1)],
              ' ',verbs[random.randint(0,len(verbs)-1)],
              ' ',adverbs[random.randint(0,len(adverbs)-1)])
    else:
        print(articles[random.randint(0,len(articles)-1)],
              ' ',nouns[random.randint(0,len(nouns)-1)],
              ' ',verbs[random.randint(0,len(verbs)-1)],)