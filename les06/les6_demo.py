woord = 'ingeerfde'
for letter in woord:
    print(letter, end='=')

print()

for i in range(len(woord)):
    print(woord[i], end='-')

teams = [('Laura', 'Lorenzo', 'Philippe'), ('Gijs', 'Tijmen', 'Lukas')]

print(teams[1][2][3])

for team in teams:
    for student in team:
        for letter in student:
            print(letter, end='.')
        print()
    print('-' * 80)

woord = 'hallo'
for i in range(len(woord)):
    print(woord[i], end='-')

print("\nNu met while:")

i = 0
while i < len(woord):
    print(woord[i], end='-')
    i += 1

# # Irritante applicatie
# while True:
#     # input("Zeg 's wat: ")


print("\n")


def acronym(woorden):
    lijst = woorden.split(' ')  # ['Tijmen', 'Joppe', 'Muller']

    afko = str()
    for woord in lijst:
        afko = afko + woord[0]

    afko = afko.upper()
    return afko


print(acronym('Tijmen Joppe Muller'))  # 'TJM'
print(acronym('central processing unit'))  # 'CPU'


def pixels(lst):
    nr_not_dark = 0
    for row in lst:
        for col_index in range(len(row)):
            if row[col_index] != 0:
                nr_not_dark += 1
    return nr_not_dark


lst = [[0, 54, 0], [54, 54, 0], [54, 54, 0], [76, 76, 0]]  # 7

print(pixels(lst))
