string = input("Voer een string in: ")

print("Deze string omgekeerd: ")
for i in range(len(string), 0, -1):
    print(string[i])

string = input("Voer een string in:")

string_reversed = ""
for letter in string:
    string_reversed = letter + string_reversed

print(f"Deze string omgekeerd: {string_reversed}")


getal1 = int(input("Getal 1: "))
getal2 = int(input("Getal 2: "))
getal3 = int(input("Getal 3: "))

getallen = [getal1, getal2, getal3]
getallen.sort()

print("Het middelste getal is:", getallen[1])


import math

x1 = int(input("X-positie coordinaat 1: "))
y1 = int(input("Y-positie coordinaat 1: "))
x2 = int(input("X-positie coordinaat 2: "))
y2 = int(input("Y-positie coordinaat 2: "))

left_sum = x2-x1
right_sum = y2-y1

res = (left_sum**2) + (right_sum**2)
sqrt = math.sqrt(res)
afstand = round(sqrt, 4)

print(f"Afstand tussen de coors ({x1, y1}) en ({x2, y2}) is: {afstand}")

# Alternatief
afstand = ((x2-x1)**2 + (y2-y1)**2)**.5

print(f"[TJM] Afstand tussen de coors ({x1, y1}) en ({x2, y2}) is: {afstand:.4f}")

invoer = input("Geef een getal: ")
resultaat = 1
while invoer != 'stop':
    resultaat = resultaat * int(invoer)
    invoer = input("Geef een getal: ")

print("Het product:", resultaat)


def isPositiefEnKleinerDan(x, y):
    if x > 0 and x < y:
        return True
    else:
        return False


# Alternateif
def isPositiefEnKleinerDan(x, y):
    return 0 < x < y

print(isPositiefEnKleinerDan(-19, 100))

