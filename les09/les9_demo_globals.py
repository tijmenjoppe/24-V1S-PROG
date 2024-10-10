import pprint

n = 3
factor = 10

def verdubbel(getal):
    global factor
    factor = 2

    print("Locals in verdubbel")
    pprint.pprint(locals())
    print()

    print("Globals in verdubbel")
    pprint.pprint(globals())
    print()

    return factor * getal

print(verdubbel(n))

pprint.PrettyPrinter(indent=4)

print("Locals in __main__")
pprint.pprint(locals())
print()

print("Globals in __main__")
pprint.pprint(globals())
print()
