langsteWoord = ""
for woord in input("Geef 4 woorden, gescheiden door een streepje ( - ): ").split("-"):
    if len(woord) > len(langsteWoord):
        langsteWoord = woord
print("Het langste woord van de vier is:", langsteWoord)