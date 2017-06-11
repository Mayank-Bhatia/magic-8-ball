import random
from time import sleep 

possible_answers = ["It is certain", "It is decidedly so", "Without a doubt",
                    "Yes, definitely", "You may rely on it", "As I see it, yes",
                    "Most likely", "Outlook good", "Yes", "Signs point to yes",
                    "Reply hazy try again", "Ask again later",
                    "Better not tell you now", "Cannot predict now",
                    "Concentrate and ask again", "Don't count on it",
                    "My reply is no", "My sources say no", "Outlook not so good",
                    "Very doubtful"]

while True:
    Question = input('\n' '''Hi! I'm the Magic 8 Ball, ask me anything: ''')
    if Question == 'q':
        print('\n', 'Thanks for playing!')
        break
    else:
        print('thinking...')
        sleep(2.0)
        print('\n', random.choice(possible_answers), '\n' '\n' '\n'
              '~ Play again, or q to quit ~')
