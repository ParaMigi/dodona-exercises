# <b>Opdracht</b>
Schrijf een programma dat de gebruiker om een woord of zin vraagt en dan weergeeft hoeveel klinkers en medeklinkers er in zitten.

<details markdown="1"><summary>Wat zijn klinkers en medeklinkers?</summary>
- Klinkers: `a`, `e`, `i`, `o`, `u`
- Medeklinkers: `b`, `c`, `d`, `f`, `g`, `h`, `i`, `j`, `k`, `l`, `m`, `n`, `p`, `q`, `r`, `s`, `t`, `v`, `w`, `x`, `z`
- Speciaal geval: `y`, want het hangt van de uitspraak af of dit een klinker of medeklinker is. Deze letter laten we buiten beschouwing en zal dus niet voorkomen in de oefening.
- Spatie: als er een zin wordt gegeven zullen er dus spaties tussen de woorden staan. Dit moet bij geen van de twee categorieën gerekend worden.
- Hoofdletters: we zullen voor het gemak in deze oefening enkel met kleine letters werken. Je hoeft dus geen rekening te houden met hoofdletters.
- Accenten en trema's: we zullen voor het gemak in deze oefening geen letters met accenten of trema's gebruiken. Je hoeft dus geen rekening te houden met letters met accenten of trema's.
</details>

<br>
<br>

# <b>Voorbeelden</b>

<details markdown="1"><summary>Voorbeeld 1</summary>
### Invoer
```console?lang=python
informaticawetenschappen is een leuk vak
```

### Uitvoer
```console?lang=python
Klinkers: 15
Medeklinkers: 21
```
</details>

<details markdown="1"><summary>Voorbeeld 2</summary>
### Invoer
```console?lang=python
letters
```

### Uitvoer
```console?lang=python
Klinkers: 2
Medeklinkers: 5
```
</details>