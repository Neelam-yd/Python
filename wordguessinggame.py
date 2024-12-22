import random
print('hello , you have to guess a word from the given words :')

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
print(words)
random_word = random.choice(words);# Choose a random word
total_chances = 12 ;
count = 0;
while total_chances > count:
    guessed = input("enter the guessed word :").strip().lower()
    count += 1;
    if guessed == random_word:
         print(f"Congatulation your guess is correct");
    elif guessed != random_word:
         print(f"your guess is wrong");
 
if count == total_chances and guessed != random_word:
    print(f"😢 Sorry, you're out of chances. The correct word was '{random_word}'.")