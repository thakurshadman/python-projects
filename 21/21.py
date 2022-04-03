import random

def build_cards_dict() -> dict :
    
    cards_dict:dict = {}
    for i in range(2,11):
        cards_dict[str(i)] = i
    cards_dict['J'] = 10
    cards_dict['Q'] = 10
    cards_dict['K'] = 10
    cards_dict['A'] = 11
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
            current_total += cards_dict[individual_card]
            ace_counter += 1
        else:
            current_total += cards_dict[individual_card]
            
    while current_total > 21:
        if ace_counter == 0:
            break
        else:
            ace_counter -= 1
            current_total -= 10
    
    return current_total
        

def prompt_hit()->bool:
    acceptable_inputs = {'y':True, 'yes':True,  'hit': True,  'n':False,  'no': False, 'stand':False }
    while True:
        try:
            player_choice = input('Type "y" if you would like to HIT or type "n" if you would like to STAND: ')
            print('\n')
            return acceptable_inputs[player_choice.lower()]
        except:
            print('Invalid Input\n')
    

def dealers_hits(dealers_score)->bool:
    if dealers_score < 17:
        return True
    else:
        return False
    
def check_who_won(player_score, dealers_score):
        #note for win condition dealer and player could both have 21
    if player_score == dealers_score:
        print('DRAW!')
    elif player_score == 21:
        print('Black Jack!\n')
    elif dealers_score > player_score :
        print('Better luck next time!\n')
    else:
        player_choice = prompt_hit()
        return player_choice
    
def check_if_bust(score) -> bool:
    if score > 21:
        print('Bust!')
        return True
    
def play_game():
    
    deck = build_cards_dict()
    players_hand = init_dealing(deck, 2)
    dealers_hand = init_dealing(deck, 2)
    concealed_dealers_hand = [dealers_hand[0], '?']
    player_choose_hit = True #just for testing
    dealer_choose_hit = True
    
    while player_choose_hit or dealer_choose_hit:
        player_score = get_hand_total(players_hand,deck)
        dealers_score = get_hand_total(dealers_hand,deck)
        print(f'Your Hand: {players_hand} Current Total: {player_score}' )
        print(f"Dealer's Hand: {concealed_dealers_hand}, {dealers_score}\n")
        player_choose_hit = prompt_hit()
        dealer_choose_hit = dealers_hits(dealers_score)
        if player_choose_hit:
            players_hand.extend(init_dealing(deck,1))
        if dealer_choose_hit:
            dealers_hand.extend(init_dealing(deck,1))
            concealed_dealers_hand.append('?')
    #Evaluate Score After exiting while-lopp
    
play_game()
