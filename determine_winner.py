import numpy as np
from hand_evaluations import *
from tie_breakers import *

#compare the hands of two players to see who wins between them
#returns 0 if player1 wins, 1 if player2 wins, and 2 if there's a tie
def compareTwoPlayers(player1_cards, player2_cards, dealer_cards):
    #make players' hands by combining their starting cards each with the dealer's cards
    player1_hand = np.concatenate(player1_cards, dealer_cards)
    player2_hand = np.concatenate(player2_cards, dealer_cards)

    #list to hold ranks of players' hands
    ranks = [10, 10]

    #determine rank of each player's hand
    #the ranks are as follows
    #'Royal Flush: 1,
    #'Straight Flush: 2,
    #'Four of a Kind: 3,
    #Full House: 4,
    #Flush: 5,
    #Straight: 6,
    #Three of a Kind: 7,
    #Two Pair: 8,
    #One Pair: 9,
    #High Card: 10
    hands = [player1_hand, player2_hand]
    for i in range(len(hands)):
        if isOnePair(hands[i]):
            ranks[i] = 9

        if isTwoPair(hands[i]):
            ranks[i] = 8
        
        if isThreeOfAKind(hands[i]):
            ranks[i] = 7
        
        if isStraight(hands[i]):
            ranks[i] = 6
        
        if isFlush(hands[i]):
            ranks[i] = 5
        
        if isFullHouse(hands[i]):
            ranks[i] = 4

        if isFourOfAKind(hands[i]):
            ranks[i] = 3

        if isStraightFlush(hands[i]):
            ranks[i] = 2

        if isRoyalFlush(hands[i]):
            ranks[i] = 1

    #compares the rank of each player's hand to determine the winner
    #if both hands have the same rank then compare strength
    #of each hand to determine the who is the winner or if game is a tie
    if ranks[0] < ranks[1]:
        result = 0
    elif ranks[0] > ranks[1]:
        result = 1
    else:
        if ranks[0] == 10:
            result = highCardTie(player1_hand, player2_hand)
        elif ranks[0] == 9:
            result = onePairTie(player1_hand, player2_hand)
        elif ranks[0] == 8:
            result = twoPairTie(player1_hand, player2_hand)
        elif ranks[0] == 7:
            result = threeOfAKindTie(player1_hand, player2_hand)
        elif ranks[0] == 6:
            result = straightTie(player1_hand, player2_hand)
        elif ranks[0] == 5:
            result = flushTie(player1_hand, player2_hand)
        elif ranks[0] == 4:
            result = fullHouseTie(player1_hand, player2_hand)
        elif ranks[0] == 3:
            result = fourOfAKindTie(player1_hand, player2_hand)
        elif ranks[0] == 2:
            result = straightFlushTie(player1_hand, player2_hand)
        elif ranks[0] == 1:
            result = 2

    return result

#compares your hand with all other players in the game
#to determine if you won, lost, or tied
#returns 0 if for win, 1 for loss, and 2 for a tie
def whoWin(start_cards, players_cards, dealer_cards):
    for i in range(len(players_cards)):
        result = compareTwoPlayers(start_cards,players_cards[i],dealer_cards)
    return result
