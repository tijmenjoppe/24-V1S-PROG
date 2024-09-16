def bak_pannekoek(melk, ei, bloem):
    """ Bereken aantal pannenkoeken op basis van melk (in ml), eieren (in stuks) en bloem (in gram). """
    aantal_melk = melk // 800
    aantal_ei = ei
    aantal_bloem = bloem // 400

    aantal_pannekoeken = min(aantal_melk, aantal_ei, aantal_bloem) * 10

    return aantal_pannekoeken


print("Aantal pannekoeken:", bak_pannekoek(3000, 10, 5000) / 4)


def rng(lst):
    return max(lst) - min(lst)


print(rng([1, 2, 3, 4]))
print(rng([3, 4, 2, 1]))
print(rng([10, 20, 30, 40]))
print(rng([-1, -2, -3, -4]))
print(rng([-14, -342, 1 - 3, 9 ** 3]))
