import random

def build_cards_dict() -> dict :
    
    cards_dict:dict = {}
    for i in range(1,11):
        cards_dict[str(i)] = i
    cards_dict['J'] = 10
    cards_dict['Q'] = 10
    cards_dict['K'] = 10
    cards_dict['A'] = (1,11)
    return cards_dict

def init_dealing(card_dict, num_of_cards)->list:
    
      initial_hand:list = []
      initial_hand = random.sample(card_dict.keys(),num_of_cards)
      return initial_hand

def get_hand_total(hand,cards_dict)->int:
    
    current_total:int = 0
    ace_counter: int = 0
    
    for individual_card in hand:
        if individual_card == 'A':
            ace_counter += 1
        else:
            current_total += cards_dict[individual_card]
            
    if ace_counter == 0:
        return current_total
    
    current_total += (11*ace_counter)
    
    while current_total > 21:
        if ace_counter == 0:
            break
        else:
            ace_counter -= 1
            current_total -= 10
    
    return current_total
        

def promptHit()->bool:
    acceptable_inputs = {'y':True, 'yes':True,  'hit': True,  'n':False,  'no': False, 'stand':False }
    while True:
        try:
            player_choice = input('Type "y" if you would like to HIT or type "n" if you would like to STAND: ')
            return acceptable_inputs[player_choice.lower()]
        except:
            print('Invalid Input\n')
    

    
    
def play_game():
    
    deck = build_cards_dict()
    players_hand = init_dealing(deck, 2)
    dealers_hand = init_dealing(deck, 2)
    player_score = get_hand_total(players_hand,deck)
    dealers_score = get_hand_total(dealers_hand,deck)
    print(f'Your Hand: {players_hand} Current Total: {player_score}' )
    print(f"Dealer's Hand: [{dealers_hand[0]}, ?]")
    player_choice:bool
    if player_score == 21:
        print('Black Jack! You Win!\n')
    elif dealers_hand == 21:
        print('Better luck next time!\n')
    else:
        player_choice = promptHit()
    if player_choice:
        players_hand.extend(init_dealing(deck,1))
        player_score = get_hand_total(players_hand,deck)
        print(f'Your Hand: {players_hand} Current Total: {player_score}' )
        
        
    

    
play_game()
