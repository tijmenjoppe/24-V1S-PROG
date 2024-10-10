def kwadraten_som(grondgetallen):
    """
    Sommeer de kwadraten van de positieve getallen
    in de lijst `grondgetallen`.

    grondgetallen (list): een lijst van integers
    """
    som = 0
    for getal in grondgetallen:
        if getal > 0:
            som = som + getal ** 2

    return som


print(kwadraten_som([6]))           # 36
print(kwadraten_som([-6]))          #  0
print(kwadraten_som([4, 3, -5]))    # 25
print(kwadraten_som([0]))           #  0
print(kwadraten_som([]))            #  0

