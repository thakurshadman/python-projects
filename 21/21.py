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

def init_dealing(card_dict)->list:
    
      initial_hand:list = []
      initial_hand = random.sample(card_dict.keys(),2)
      return initial_hand

def get_hand_total(hand,cards_dict)-> int:
    
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
        
     
    
            