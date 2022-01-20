import random

words = ['hello', 'shady', 'seven']
todays_word = random.choice(words)
print('Enter your first guess: ')
todays_word_split = list(todays_word)
# print(todays_word_split)

x = 0

green1 = False 
green2 = False 
green3 = False 
green4 = False 
green5 = False 


while (x<=5):
    print('Guess #' + str(x+1) + '. Enter your guess here: ')
    wordcheck = True
    while (wordcheck):
        guess = input()
        if len(guess) == 5:
            wordcheck = False
        else: 
            print('Try again. Please enter a 5 letter word: ')
    guess_split = list(guess)
    if guess_split[0]==todays_word_split[0]:
        print('1. Green')
        green1 = True 
    elif guess_split[0] in todays_word_split:
        print('1. Yellow')
    else:
        print('1. Gray')
    if guess_split[1]==todays_word_split[1]:
        print('2. Green')
        green2 = True
    elif guess_split[1] in todays_word_split:
        print('2. Yellow')
    else:
        print('2. Gray')
    if guess_split[2]==todays_word_split[2]:
        print('3. Green')
        green3 = True
    elif guess_split[2] in todays_word_split:
        print('3. Yellow')
    else:
        print('3. Gray')
    if guess_split[3]==todays_word_split[3]:
        print('4. Green')
        green4 = True
    elif guess_split[3] in todays_word_split:
        print('4. Yellow')
    else:
        print('4. Gray')
    if guess_split[4]==todays_word_split[4]:
        print('5. Green')
        green5 = True
    elif guess_split[4] in todays_word_split:
        print('5. Yellow')
    else:
        print('5. Gray')
    if (green1 & green2 & green3 & green4 & green5):
        print('Congrats you won!')
        break
    else: 
        x = x+1
        green1 = False
        green2 = False
        green3 = False
        green4 = False
        green5 = False
if x == 5: 
    print('Sorry, you lost :(')