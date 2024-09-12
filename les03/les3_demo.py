som = 0
for getal in range(2, 9, 2):
    # som = som + getal
    som += getal

print('som:', som)


naam = input("Geben Sie seine Nahm bitte: ")
leeftijd = int(input("Geben Sie bitte Ihrer leeftijd: "))
if leeftijd >= 18:
    print(f"{naam}, du mochst wahlen")
else:
    print("Du moechst nicht wahlen leiter")


if leeftijd >= 65:
    print("Je bent bejaard")
elif 65 > leeftijd >= 18:
    print("Je bent volwassen")
elif 18 > leeftijd >= 12:
    print("Je bent een puber")
elif 12 > leeftijd >= 4:
    print("Je bent een kleuter")
else:
    print("Je bent een baby")


if leeftijd >= 65:
    print("Je bent bejaard")
elif leeftijd >= 18:
    print("Je bent volwassen")
elif leeftijd >= 12:
    print("Je bent een puber")
elif leeftijd >= 4:
    print("Je bent een kleuter")
else:
    print("Je bent een baby")


lengte = float(input("Wat is je lengte (in meter)? "))
gewicht = float(input("Wat is je gewicht (in kg)? "))

bmi = gewicht / lengte ** 2

print(f"Je BMI is {round(bmi, 2)}")

if bmi < 18.5:
    print("Je hebt ondergewicht...")
elif bmi < 25:
    print("Je hebt een normaal gewicht...")
else:  # bmi >= 25
    print("Je hebt overgewicht...")


for letter in ('a', 'b', 'x'):
    print(letter)


for cijfer in range(0, 11, 1):  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # ^ iets = 0
    # ^ iets = 1
    # ^ iets = 2
    print("iets =", cijfer)

print("klaar!")


word = input("Geef een woord: ")

for character in word:
    print(character, end='\r\n')
