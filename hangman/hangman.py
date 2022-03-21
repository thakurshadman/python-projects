import random


print('\nWELCOME TO HANGMAN!\n')

categories = ["Animal", "Sport", "Food"]

word_bank = {"Animal": ["cat", "dog", "elephant", "chicken", "mouse", "tiger", "horse", "fish", "python"], "Sport": [
    'soccer', 'basketball', 'golf', 'hockey', 'cricket', 'football', 'tennis', 'boxing'], "Food": ['pizza', 'burger', 'cake', 'pasta', 'samosa', 'chocolate', 'steak', 'kebab', 'taco']}

hangman_stage = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

for order, category in enumerate(categories):
    print(order, category)
    
print('\n')

users_cat_choice = int(input("Please enter the related number to select a category!: "))
print('\n*****************************************************')

entries_from_categories = word_bank[categories[users_cat_choice]]
word_to_guess = list(entries_from_categories[random.randint(0, len(entries_from_categories)-1)])

print(f"\nI'm a {len(word_to_guess)} letter {categories[users_cat_choice]}!")

blank_placeholders = []
for i in word_to_guess:
    blank_placeholders.append('_')

print(' '.join(blank_placeholders) + '\n')#                _ _ _ _ _ _

incorrect_guesses = set()
while len(incorrect_guesses) < 6:
    print(hangman_stage[len(incorrect_guesses)])
    print(f'Incorrect guesses: {"{}" if not incorrect_guesses else incorrect_guesses}\n')
    users_letter = input('Guess a letter: ')
    print('\n*****************************************************')
    for i in range(len(word_to_guess)):
        if word_to_guess[i] == users_letter:
            blank_placeholders[i] = users_letter
    if users_letter not in blank_placeholders:
        incorrect_guesses.add(users_letter)
    updated_placeholder_word = ' '.join(blank_placeholders)
    print('\n'+ updated_placeholder_word)
    if blank_placeholders == word_to_guess:
        print("Hurray you won!")
        exit()
    
print(hangman_stage[len(incorrect_guesses)])
print('You lose!')


