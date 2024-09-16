leeftijd = int(input("Hoe oud ben je?"))
paspoort = input("Heb je een paspoort? (ja/nee)")

if leeftijd >= 18 and paspoort == "ja":
    print("Jij mag stemmen!")
else:
    print("Jij mag niet stemmen!")
