# Demo if-statement(s) vs. dictionary
def zoek_student(nummer):
    if nummer == 1835957:
        return 'Dominik'
    elif nummer == 1842828:
        return 'Damon'
    elif nummer == 1828968:
        return 'Dirk'

    return 'onbekend'


print('Student', 1835957, 'is', zoek_student(1835957))

studenten = {1835957: 'Dominik', 1842828: 'Damon', 1828968: 'Dirk'}

print('Student', 1835957, 'is', studenten[1835957])

print('items:', studenten.items())
print('keys:', studenten.keys())
print('values:', studenten.values())

for (key, value) in studenten.items():
    print(key, "=", value)

artikel = """
nederlandse militairen die volgende maand meedoen aan een navo-oefening in noorwegen moeten hun eigen winterkleding
regelen defensie had de kleding voor hen moeten kopen maar slaagde daar niet op tijd in dit bevestigt een
woordvoerder na berichtgeving door de telegraaf wat er precies is misgegaan in de aanbesteding waardoor de
winterkleding niet op tijd kon worden geleverd kan de woordvoerder niet zeggen de militairen hoeven de kleding niet
voor te schieten benadrukt de woordvoerder ze kunnen een voorschot krijgen van 1000 euro wat genoeg moet zijn om
alles wat nodig is aan te schaffen de temperaturen in het gebied waar de oefening wordt gehouden kan dalen tot meer
dan 20 graden onder nul zo'n duizend militairen doen aan de missie mee"""


def wordcount(text: str):
    woorden_lijst = text.split()

    # elk uniek woord als key, aantal voorkomens als value
    woordteller = dict()

    for woord in woorden_lijst:
        if woord in woordteller:
            woordteller[woord] = woordteller[woord] + 1
        else:
            woordteller[woord] = 1

    return woordteller


artikel_tel = wordcount(artikel)

# for (woord, aantal) in artikel_tel.items():
#     print(f"'{woord}' komt {aantal} keer voor")

phonebook = {
    ('Anna', 'Karenina'): '(123) 456-78-90',
    ('Yu', 'Tsun'): '(901) 234-56-78',
    ('Hans', 'Castorp'): '(321) 908-76-54'}

def lookup(lookup_dict):
    while True:
        vnaam = input("Wat is de voornaam? ").capitalize()
        anaam = input("Wat is de achternaam? ").capitalize()
        naam = (vnaam, anaam)

        if naam in lookup_dict:
            print("Nummer:", lookup_dict[naam])
        else:
            print('Onbekend')

        # for k, v in lookup_dict.items():
        #     if k == naam:
        #         print("Nummer: ", v)


# lookup(phonebook)

import json
import pprint

pp = pprint.PrettyPrinter(indent=4)

with open("studenten.json") as json_bestand:
    data = json.load(json_bestand)

# print(data['studenten'][0])

pp.pprint(data['studenten'][0])

for student in data['studenten']:
    print(f'{student["voornaam"]} heeft voor PROG een {student["cijfers"]["PROG"]}')