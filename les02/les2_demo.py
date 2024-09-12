import random

getal = int(input("Geef een getal: "))

dobbelsteen = random.randrange(1)

print(f"Ik koos {dobbelsteen}")
print(f"Jij koos {getal}")

print(type(getal))
print(type(dobbelsteen))

print(getal == dobbelsteen)
