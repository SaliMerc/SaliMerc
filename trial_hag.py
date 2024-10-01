import random
game_dictionary={
    'Game title:': 'Hangman game',
    'Game description:': 'The game allows the user to guess letters present in a randomly selected word',
    'Response for correct letter:': 'Congratulations, the letter is in the word',
    'Response for incorrec letter:': 'Oops! the letter is not in the word',
    'Win message:': 'Congratulations, you have won the game',
    'Lose message:': 'Sorry, you did not win this time'
    }
for key, values in game_dictionary.items():
    print(key, values)
words=['keith', 'loves', 'sleeping', 'alot', 'at', 'some', 'point', 'he', 'almost', 'slept', 'in', 'class', 'and',
       'missed', 'the', 'whole', 'lesson', 'which', 'was', 'essential']
random_word1=random.choice(words)
print(random_word1)
score=0
count=0
guessed_list=[]
while count<6:
    count+=1
    guessed_letter=input('Guess a letter in the random word: ')
    guessed_list.append(guessed_letter) 
    if guessed_list.count(guessed_letter)>1:
            guessed_list.remove(guessed_letter)
            print('You have already guessed this letter')
    else:
        if random_word1.find(guessed_letter)==-1:
            print('Letter not found in string')
            print(f'The remaining letters are "{random_word1}"')
            print(f'The letters you have guessed are: {guessed_list}')
        else:
            remaining_words=random_word1.replace(guessed_letter, '_ _')
            print('Letter found in the word')
            print(f'The remaining letters are "{remaining_words}"')
            score+=1      
            print(f'The letters you have guessed are: {guessed_list}')

total=len(random_word1)
print(f'Your right guesses are: {score} of {total}')
total_score=(score/total)*100
print(f'Your percentage score is {total_score}')
if total_score>=80:
    print(game_dictionary['Win message:'])
else:
    print(game_dictionary['Lose message:'])
   
#this is the end of te hnagman game
#the game enables the user to input a random letter then the presenc eof the letter in a randomly chosen word is checked
#if the letter is present, the user's count is incremented otherwise, nothing is done.
#however, if the user inputs a letter more than once, the program signifies them that they have already input that letter and it is not couted 
#thanks for following
