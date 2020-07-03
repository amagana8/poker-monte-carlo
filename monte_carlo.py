import numpy as np
from card_hands_generator import *
from determine_winner import whoWin

#N - number of times to simulate the round
#n_players - number of other players in game
#starting_hand - your 2 starting cards you were dealt
def monteCarloPoker(N, n_players, starting_hand):
    win_probability = 0
    lose_probability = 0
    tie_probability = 0
    for i in range(N):
        #create deck
        deck = np.array([])
        for i in range(52):
            deck = np.append(deck, i)
        deck = deck.astype(int)

        #create starting hand
        start_hand = np.array([])
        for card in starting_hand:
            card_value = cardNameToInt(card)
            start_hand = np.append(start_hand, card_value)
        start_hand = start_hand.astype(int)

        #remove starting_hand from deck
        index1 = np.argwhere(deck == start_hand[0])
        deck = np.delete(deck, index1)

        index2 = np.argwhere(deck == start_hand[1])
        deck = np.delete(deck, index2)

        #generate hands for game
        dealer_tup = generateDealerCards(deck)
        dealer_cards = dealer_tup[0]
        deck = dealer_tup[1]
    
        player_tup = generatePlayersCards(n_players, deck)
        players_cards = player_tup[0]
        deck = dealer_tup[1]

        #determine winner
        result = whoWin(start_hand, players_cards, dealer_cards)

        #determine probabilities
        if result == 0:
            win_probability += 1/N
        if result == 1:
            lose_probability += 1/N
        if result == 2:
            tie_probability += 1/N

    return [win_probability, lose_probability, tie_probability]
