from os import system, name

def Greeting():
    
    gavel = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
                          
Welcome to the secret auction!
'''
    print(gavel)
    
def prompt_name()->str:
    
    name = input("What is your name?: ")
    return name

def prompt_bid()->int:
    
    input_is_valid = False
    while not input_is_valid:
        try:
            bid = int(input('What is your bid?: $'))
            if bid > -1:
                return bid
            else:
                raise ValueError()
        except ValueError:
            print("Invalid Input!\n")
    
def prompt_other_participants()->bool:
    
    input_is_valid = False
    while not input_is_valid:
        try:
            is_there_more_participants = input('Are there any other bidders?(y / n): ')
            if is_there_more_participants == 'y':
                return True
            elif is_there_more_participants == 'n':
                return False
            else:
                raise ValueError('Invalid Input!\n')
        except ValueError as err:
            print(err)

def clear():
      
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
        
