while True:
    try:
        teller = int(input("Geef de teller: "))
        noemer = int(input("Geef de noemer: "))

        print(f"Het resultaat is {teller/noemer:.2f}")
    except ZeroDivisionError:
        print(f"Je mag niet delen door 0...")
    except ValueError:
        print(f"Je moet een geheel getal invullen")
    except:
        print(f"Fout!")
    else:
        break
    finally:
        print("Dat was leuk!")
