from click import prompt


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
    name = prompt("What is your name?: ")
    return name

def prompt_bid()->int:
    bid = int(prompt('What is your bid?: '))
    
def prompt_other_participants()->bool:
    is_there_more_participants = prompt()