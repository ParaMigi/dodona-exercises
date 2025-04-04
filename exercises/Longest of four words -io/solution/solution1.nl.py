woord1, woord2, woord3, woord4 = input("Geef 4 woorden, gescheiden door een streepje ( - ): ").split("-")
langsteWoord = woord1
if len(woord2) > len(langsteWoord):
    langsteWoord = woord2
if len(woord3) > len(langsteWoord):
    langsteWoord = woord3
if len(woord4) > len(langsteWoord):
    langsteWoord = woord4
print("Het langste woord van de vier is:", langsteWoord)