#!/usr/bin/env python3
import random
import sys

articles=['a','the']
nouns=['cat','dragon','pyton','gun','grind','Archangelsk']
verbs=['catch','throw','try','left','make','do']
adverbs=['well','highly','annoyingly','fully']


max=5
if len(sys.argv)>1:
    try:
        if int(sys.argv[1])>0 and int(sys.argv[1])< 11:
            max=int(sys.argv[1])
    except ValueError as err:
        print(err)
    else:
        print('Invalid argument. Argument must be 0<x<11.')

for x in range(max):
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