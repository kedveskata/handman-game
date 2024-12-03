# Akasztófa játék
*Fejlesztői dokumentáció*

Akasztófa játék az Haladó Python órán tanult kifejezésekkel. 

## Megjelenése
![hangman_program](https://github.com/user-attachments/assets/d11d5268-c4bd-47e3-89ee-76d18c1204fc)

## Megoldás
Fontos listák, változók és függvények
## Importált csomagok
*random*
*string* –> ascii_uppercase
*tkinter* –> *
*tkinter* –> messagebox
## Listák
[string] word_list: a kitalálandó szavakat tartalmazza
[string] hangman: a *string*-ből összeállított akasztófa szakaszait tartalmazza 
## Változók
[string] **text_color**: a megjelenő program szövegszínét itt tároljuk
[string] **random_word**: a *word_list*-ből kiválasztott véletlenszerű szó
[string] **word_with_spaces**: *random_word* karakterei között szóközök vannak
[integer] **number_of_wrong_guesses**: sikertelen tippeket
[integer] **won**: nyert körök
[integer] **lost**: elvesztett körök

[list] **word**: a kitalálandó szó karaktereit tárolja
[list] **guessed**: *guess_word*-nek a *char* tömbje

[label] **hangman_Label**: maga az akasztófa tartója
[label] **guess_word**: kitalálandó szó 
## Függvények
**new_game**: új játékot kezd
**guess**: a játékmenetéért felel, ellenőrzi, hogy a kitalálandó szó karakterei megegyeznek-e a felhasználó által beütött karakterekkel. 
## Algoritmusok
Itt ellenőzi, hogy a beütött betű megegyezik-e a kitalálandó szó bármely karakterével.

```
for c in range(len(word)):
    if word[c] == char:
        guessed[c] = char
    guess_word.set("".join(guessed))
```

Az ascii_uppercase-en végigfutva létrehoz gombokat az angol ábécé betűinek.

```
for char in ascii_uppercase:
    Button(root, text=char, command=lambda char=char: guess(char), fg=text_color, font=('Verdena 18'), width=4).grid(row=1 + n // 9, column=n % 9)
    n += 1
```
 
## Program működése
![hangman](https://github.com/user-attachments/assets/0ebe057e-655e-4513-a50e-755aa8d8d273)
 
## Fejlesztési lehetőségek
Jelenítse meg a már megtippelt betűket.

