import random


print('WELCOME TO HANGMAN!\n')

categories = ["Animal", "Sport", "Food"]
categories_entries = {"Animal": ["cat", "dog", "elephant", "chicken", "mouse", "tiger", "horse", "fish", "python"], "Sport": [
    'soccer', 'basketball', 'golf', 'hockey', 'cricket', 'football', 'tennis', 'boxing'], "Food": ['pizza', 'burger', 'cake', 'pasta', 'samosa', 'chocolate', 'steak', 'kebab', 'taco']}

for order, category in enumerate(categories):
    print(order, category)
print('\n')
users_cat_choice = int(
    input("Please enter the related number to select a category!: "))
entries = categories_entries[categories[users_cat_choice]]
word_to_guess = entries[random.randint(0, len(entries)-1)]
print(f"\nI'm a {len(word_to_guess)} letter {categories[users_cat_choice]}!")
blank_placeholders = ''
for i in word_to_guess:
    blank_placeholders += '_ '

print(blank_placeholders + '\n')

incorrect_guesses = set()
correct_guesses = set()
users_letter = input('Guess a letter: ')

for i in range(len(word_to_guess)):
    if word_to_guess[i] == users_letter:
        correct_guesses.add(users_letter)
        splitted = list(blank_placeholders)
        splitted[i*2] = users_letter
        blank_placeholders = ''.join(splitted)
print(blank_placeholders)