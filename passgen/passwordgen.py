import random
import string

num_of_letters = int(input("How many letters would you like in your password? "))
num_of_symbols = int(input("How many symbols would you like in your password? ")) 
num_of_nums = int(input("How many numbers would you like in your password? "))

password = ''.join(random.choice(seq=string.ascii_letters) for _ in range(num_of_letters)) 

password += ''.join(random.choice(seq=string.punctuation) for _ in range(num_of_symbols))

password += ''.join(random.choice(seq=string.digits) for _ in range(num_of_nums)) 

password_list = list(password)
random.shuffle(password_list)
randomized_password = ''.join(password_list)

print(randomized_password)