import random

with open('txt.txt', 'r') as fopen:
    lines = fopen.readlines()

word_guess = random.choice(lines).strip()
counter = len(word_guess)
print('Hasło to jeden ze składników pancakes')
print('Hasło sklada sie z ', counter, 'liter.')
turns = 6
print('Masz', 6, 'prob, aby odgadnac hasło!')

def game(user_guess):
    turns=6
    user_guess = []
    used_letter = []
    blank = []
    for i in range(counter):
        user_guess.append('_')


    used_letters = ''

    while turns > 0:
        to_show = user_guess
        print(to_show)
        guess = input('Podaj litere,lub cale haslo jesli juz je znasz:')
        guess = guess.lower()
        if guess == word_guess:
            print('Wygrana! to jest to słowo:', guess)
            break

        if guess in word_guess:
            turns -= 1
            for index in range(counter):
                if word_guess[index] == guess:
                    user_guess[index] = guess
        else:
            turns -= 1

            if guess in used_letter:
                print('Nie mozesz uzyc tej litery, już jej użyłeś ! ')
                blank.append(guess)
            else:
                used_letter.append(guess)
            print('Użyte litery', used_letter)





        if turns == 0:
            print(" _________")
            print("|	 |")
            print("|	 O")
            print("|	\|/")
            print("|	 |")
            print("|	/ \ ")
            print("|________")
            print('Koniec gry')
            break
        elif turns == 5:
            print("_________")
            print("|	 |")
            print("|	    ")
            print("|	   ")
            print("|	  ")
            print("|	   ")
            print("|________")
        elif turns == 4:
            print("_________")
            print("|	 |")
            print("|	 0  ")
            print("|	   ")
            print("|	  ")
            print("|	   ")
            print("|________")
        elif turns == 3:
            print("_________")
            print("|	 |")
            print("|	 0  ")
            print("|	 |")
            print("|	 |")
            print("|	   ")
            print("|________")
        elif turns == 2:
            print("_________")
            print("|	 |")
            print("|	 0  ")
            print("|	\|")
            print("|	 |")
            print("|	   ")
            print("|________")
        elif turns == 1:
            print("_________")
            print("|	 |")
            print("|	 0  ")
            print("|	\|")
            print("|	 |")
            print( "|	/ ")
            print("|________")





        print('Zostało Ci prób ->', turns)
        print('Podaj kolejna litere.')



turns = 6
game(turns)
