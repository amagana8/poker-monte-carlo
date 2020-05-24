import numpy as np

#Convert card string to a value from 0-51
def cardNameToInt(name):
    suits = ['c','d','h','s']
    face_cards = {'T':10,'J':11,'Q':12,'K':13,'A':14}
   
    suit_value = suits.index(name[1])
    card_num = name[0]
    
    if card_num in face_cards.keys():
        card_num = face_cards[card_num]
    else:
        card_num = int(card_num)
    
    return suit_value + 4 * (card_num-2)

#generate hands for all the other players in the game
def generatePlayersCards(n_players,available_deck):
    updated_card_deck = available_deck
    np.random.shuffle(updated_card_deck)
    players_cards = np.empty((0,2))
    for i in range(n_players):
        temp = np.array([[updated_card_deck[0],updated_card_deck[1]]])
        players_cards = np.append(players_cards, temp, axis =0)
        updated_card_deck = np.delete(updated_card_deck, 0)
        updated_card_deck = np.delete(updated_card_deck, 0)
    players_cards = players_cards.astype(int)
    return(players_cards,updated_card_deck)

#generate the cards for the flop, turn, and river
def generateDealerCards(available_deck):
    updated_card_deck = available_deck
    np.random.shuffle(updated_card_deck)
    dealer_cards = np.array([])
    for i in range(5):
        dealer_cards = np.append(dealer_cards, updated_card_deck[0])
        updated_card_deck = np.delete(updated_card_deck, 0)
    dealer_cards = dealer_cards.astype(int)
    return(dealer_cards,updated_card_deck)
