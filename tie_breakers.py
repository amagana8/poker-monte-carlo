import numpy as np
from hand_evaluations import card_nums, cardIntsToCardNums

def highCardTie(p1_hand, p2_hand):
    #convert list of card values to numbers/faces
    p1_nums = cardIntsToCardNums(p1_hand)
    p2_nums = cardIntsToCardNums(p2_hand)

    #compares each player's high card
    #if both hands have the same high card, then compares next highest cards
    #until there is a winner or all cards have been compared
    result = 2
    while(result == 2 and len(p1_nums) > 0):
        #find the highest card in each player's hand
        p1_high_card = np.max(p1_nums)
        p2_high_card = np.max(p2_nums)

        #compare each player's high card to determine winner
        if p1_high_card > p2_high_card:
            result = 0
        elif p1_high_card < p2_high_card:
            result = 1
        else:
            p1_nums.remove(p1_high_card)
            p2_nums.remove(p2_high_card)
    return result

def onePairTie(p1_hand, p2_hand):
    #find the pair each player has
    for card_num in card_nums:
        if len(np.intersect1d(p1_hand, card_num)) == 2:
            pair1 = np.intersect1d(p1_hand, card_num)
        if len(np.intersect1d(p2_hand, card_num)) == 2:
            pair2 = np.intersect1d(p2_hand, card_num)
    
    #find the number/face of each pair
    for i in range(len(pair1)):
        for j in range(len(card_nums)):
            if pair1[i] in card_nums[j]:
                pair1_type = j+2

    for i in range(len(pair2)):
        for j in range(len(card_nums)):
            if pair2[i] in card_nums[j]:
                pair2_type = j+2

    #compare pairs to determine the winner
    if pair1_type > pair2_type:
        result = 0
    elif pair1_type < pair2_type:
        result = 1
    else:
        result = highCardTie(p1_hand, p2_hand)  
    return result

def twoPairTie(p1_hand, p2_hand):
    #find the pairs and put both in a list for each player
    pairs_p1 = []
    pairs_p2 = []
    for card_num in card_nums:
        if len(np.intersect1d(p1_hand, card_num)) == 2:
            pairs_p1.append(np.intersect1d(p1_hand, card_num).tolist())
        if len(np.intersect1d(p2_hand, card_num)) == 2:
            pairs_p2.append(np.intersect1d(p2_hand, card_num).tolist())
    
    #order the pairs in each list from highest to lowest
    if onePairTie(pairs_p1[0], pairs_p1[1]) != 0:
        pairs_p1.reverse()
    
    if onePairTie(pairs_p2[0], pairs_p2[1]) != 0:
        pairs_p2.reverse()

    #compare pairs to determine winner
    tie_result = onePairTie(pairs_p1[0], pairs_p2[0])
    if tie_result == 0 or tie_result == 1:
        result = tie_result
    elif tie_result == 2:
        tie_result_2 = onePairTie(pairs_p1[1], pairs_p2[1])
        if tie_result_2 == 0 or tie_result_2 == 1:
            result = tie_result_2
        else:
            result = highCardTie(p1_hand, p2_hand)  
    return result

def threeOfAKindTie(p1_hand, p2_hand):
    #find the triple each player has
    for card_num in card_nums:
        if len(np.intersect1d(p1_hand, card_num)) == 3:
            triple1 = np.intersect1d(p1_hand, card_num)
        if len(np.intersect1d(p2_hand, card_num)) == 3:
            triple2 = np.intersect1d(p2_hand, card_num)

    #find the number/face of each triple
    for i in range(len(triple1)):
        for j in range(len(card_nums)):
            if triple1[i] in card_nums[j]:
                triple1_type = j+2

    for i in range(len(triple2)):
        for j in range(len(card_nums)):
            if triple2[i] in card_nums[j]:
                triple2_type = j+2
    
    #compare triples to determine the winner
    if triple1_type > triple2_type:
        result = 0
    elif triple1_type < triple2_type:
        result = 1
    else:
        result = highCardTie(p1_hand, p2_hand)
    return result

def straightTie(p1_hand, p2_hand):
    #can compare the highest card of each hand to compare 
    #stregnths of straights
    result = highCardTie(p1_hand, p2_hand)
    return result

def flushTie(p1_hand, p2_hand):
    #if two players have a flush, then the player with
    #the highest card wins
    result = highCardTie(p1_hand, p2_hand)
    return result

def fullHouseTie(p1_hand, p2_hand):
    #find the triple each player has
    for card_num in card_nums:
        if len(np.intersect1d(p1_hand, card_num)) == 3:
            triple1 = np.intersect1d(p1_hand, card_num)
        if len(np.intersect1d(p2_hand, card_num)) == 3:
            triple2 = np.intersect1d(p2_hand, card_num)

    #find the number/face of each triple
    for i in range(len(triple1)):
        for j in range(len(card_nums)):
            if triple1[i] in card_nums[j]:
                triple1_type = j+2

    for i in range(len(triple2)):
        for j in range(len(card_nums)):
            if triple2[i] in card_nums[j]:
                triple2_type = j+2
    
    #compare triples to determine the winner
    #if the triples are the same then
    #compare the pairs
    if triple1_type > triple2_type:
        result = 0
    elif triple1_type < triple2_type:
        result = 1
    else:
        result = onePairTie(p1_hand, p2_hand)
    return result

def fourOfAKindTie(p1_hand, p2_hand):
    #find the quartet each player has
    for card_num in card_nums:
        if len(np.intersect1d(p1_hand, card_num)) == 4:
            quartet1 = np.intersect1d(p1_hand, card_num)
        if len(np.intersect1d(p2_hand, card_num)) == 4:
            quartet2 = np.intersect1d(p2_hand, card_num)

    #find the number/face of each triple
    for i in range(len(quartet1)):
        for j in range(len(card_nums)):
            if quartet1[i] in card_nums[j]:
                quartet1_type = j+2

    for i in range(len(quartet2)):
        for j in range(len(card_nums)):
            if quartet2[i] in card_nums[j]:
                quartet2_type = j+2
    
    #compare quartets to determine the winner
    #if the quartets are the same then
    #compare the last card
    if quartet1_type > quartet2_type:
        result = 0
    elif quartet1_type < quartet2_type:
        result = 1
    else:
        result = highCardTie(p1_hand, p2_hand)
    return result

def straightFlushTie(p1_hand, p2_hand):
    #can compare the highest card of each hand to compare 
    #stregnths of straight flushes
    result = highCardTie(p1_hand, p2_hand)
    return result
