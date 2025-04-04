# <b>Assignment</b>
You are going to make a 2-person game. First, ask player 1 for a number. Then, ask player 2 to guess the number. If they guess too low, let them know that the correct number is higher. If they guess too high, let them know that the correct number is lower. If it is correct, congratulate player 2 and stop the game.

<br>
<br>

# <b>Examples</b>
<details markdown="1"><summary>Example 1</summary>
### Input
```console?lang=python
77
10
50
100
80
70
77
```

### Output
```console?lang=python
The correct number is higher than 10
The correct number is higher than 50
The correct number is lower than 100
The correct number is lower than 80
The correct number is higher than 70
Congratulations! 77 is the correct number!
```
</details>

<details markdown="1"><summary>Example 2</summary>
### Input
```console?lang=python
5
4
5
```

### Output
```console?lang=python
The correct number is higher than 4
Congratulations! 5 is the correct number!
```
</details>

<details markdown="1"><summary>Example 3</summary>
### Input
```console?lang=python
5
6
5
```

### Output
```console?lang=python
The correct number is lower than 6
Congratulations! 5 is the correct number!
```
</details>

<details markdown="1"><summary>Example 4</summary>
### Input
```console?lang=python
5
5
```

### Output
```console?lang=python
Congratulations! 5 is the correct number!
```
</details>