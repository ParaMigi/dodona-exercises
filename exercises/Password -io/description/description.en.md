# <b>Assignment</b>
Schrijf een programma dat een gebruiker om het wachtwoord vraagt totdat die het juist heeft en steeds aangeeft hoeveel foute pogingen de gebruiker al heeft gedaan. Het juiste wachtwoord is <code>InformaticaWetenschappen!</code>.

<br>
<br>

# <b>Examples</b>

<details markdown="1"><summary>Example 1</summary>
### Input
```console?lang=python
AtsmaIsCool!
MichielsIsGeweldig!
DerckIsFantastisch!
Wiskunde
Biologie
Chemie
STEM
InformaticaWetenschappen!
```

### Output
```console?lang=python
Wrong password - attempt 1 - try again
Wrong password - attempt 2 - try again
Wrong password - attempt 3 - try again
Wrong password - attempt 4 - try again
Wrong password - attempt 5 - try again
Wrong password - attempt 6 - try again
Wrong password - attempt 7 - try again
Correct password
```
</details>

<details markdown="1"><summary>Example 2</summary>
### Input
```console?lang=python
Password1234
informaticawetenschappen
Informaticawetenschappen
InformaticaWetenschappen
InformaticaWetenschappen!
```

### Output
```console?lang=python
Wrong password - attempt 1 - try again
Wrong password - attempt 2 - try again
Wrong password - attempt 3 - try again
Wrong password - attempt 4 - try again
Correct password
```
</details>