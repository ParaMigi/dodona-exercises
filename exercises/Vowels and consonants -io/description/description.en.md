# <b>Assignment</b>
Write a program that asks the user for a word or sentence and then displays the number of vowels and consonants that it contains.

<details markdown="1"><summary>What are vowels and consonants?</summary>
- Vowels: `a`, `e`, `i`, `o`, `u`
- Consonants: `b`, `c`, `d`, `f`, `g`, `h`, `i`, `j`, `k`, `l`, `m`, `n`, `p`, `q`, `r`, `s`, `t`, `v`, `w`, `x`, `z`
- Special case: `y`, because whether this is a vowel or consonant depends on the pronunciation. We will not consider this letter for this exercise and it will not appear.
- Space: if a sentence is given there will be spaces between the words. The spaces should count to neither of the two categories.
- Capital letters: for the convenience of the exercise we will only work with lowercase letters in this exercise. So you do not need to account for capital letters.
</details>

<br>
<br>

# <b>Examples</b>

<details markdown="1"><summary>Example 1</summary>
### Input
```console?lang=python
computer science is a great subject
```

### Output
```console?lang=python
Vowels: 12
Consonants: 18
```
</details>

<details markdown="1"><summary>Example 2</summary>
### Input
```console?lang=python
letters
```

### Output
```console?lang=python
Vowels: 2
Consonants: 5
```
</details>