s = ''
woord = 'hogeschool utrecht'

for i in range(11, len(woord)):
    print(i)
    s = s + woord[i]
    s += woord[i]

print(s)


naam = 'Kalis'
geslacht = 'm'
gebjaar = 2008
getrouwd = False

aanhef = ''
if 2024 - gebjaar >= 18:
    if geslacht == 'v':
        if getrouwd:
            aanhef = 'señora '
        else:
            aanhef = 'señorita '
    else:
        aanhef = 'señor '

    aanhef = aanhef + naam

print(aanhef)
