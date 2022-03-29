from typing import Union

def encode_or_decode()->Union[str,bool]:
    usersChoice = input('Type "decode" to to decrypt a message, type "encode" to to decrypt a message: ')
    if usersChoice.lower() == 'decode' or usersChoice.lower()== 'encode':
        return usersChoice
    else:
        return False

def prompt_message()->str:
    return input('Enter your message: ')

def prompt_shift_number()->int:
    return int(input('Enter the shift number: ')) 

def encode_message(message: str, shift: int)->str:
    encoded_msg = []
    for letter in message:
        if letter.islower():
            encoded_msg.append(chr((ord(letter) + shift - 97)%26 + 97)) 
        elif letter.isupper():
            encoded_msg.append(chr((ord(letter) + shift + 65)%26 + 65))
        else:
            encoded_msg.append(letter)
    return ''.join(encoded_msg)

def decode_message(encoded_msg: str, shift: int)->str:
    decoded_msg = []
    for letter in encoded_msg:
        if letter.islower():
            decoded_msg.append(chr((ord(letter) - shift - 97)%26 + 97)) 
        elif letter.isupper():
            decoded_msg.append(chr((ord(letter) - shift + 65)%26 + 65))
        else:
            decoded_msg.append(letter)
    return ''.join(decoded_msg)
    

def ceasar_cipher():
    users_choice = encode_or_decode()
    if users_choice =='encode':
        users_message = prompt_message()
        shift_number = prompt_shift_number()
        encoded_message = encode_message(users_message,shift_number)
        print(encoded_message)
    elif users_choice == 'decode':
        users_encoded_message = prompt_message()
        shift_number = prompt_shift_number()
        decoded_message = decode_message(users_encoded_message,shift_number)
        print(decoded_message)
    else:
        print('INVALID INPUT!')
        
if __name__ == "__main__":
    ceasar_cipher()
        
