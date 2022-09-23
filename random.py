import random

name = input("What is your name? ")
print("Let's start the workout hahahaha", name)

wordlist = ['turkiye', 'istanbul', 'galatasaray', 'kebab', 'ankara']
word = random.choice(wordlist)
tries = 10
display = '_' * len(word)

game_over = False
while not game_over:
    print('you have ' + str(tries) + ' fingers remaining.')
    print(display)
    guess = input('Please guess a letter: ')

    i = 0
    if guess in word:
        while word.find(guess, i) != -1:
            i = word.find(guess, i)
            display = display[:i] + guess + display[i + 1:]
            i += 1
        print('Correct!')
    else:
        print('Sorry, wrong guess.')
        tries -= 1

    if word == display:
        print('You win! the word was ' + word)

    if tries == 0:
        print('Sorry, you fell of the bar, the word was ' + word)
        game_over = True