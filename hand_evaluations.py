import numpy as np

#lists of cards categorized by their number/face
twos = [i for i in range (0,4)]
threes = [i for i in range (4,8)]
fours = [i for i in range(8,12)]
fives = [i for i in range(12,16)]
sixes = [i for i in range(16,20)]
sevens = [i for i in range(20,24)]
eights = [i for i in range(24,28)]
nines = [i for i in range(28,32)]
tens = [i for i in range(32,36)]
jacks = [i for i in range(36,40)]
queens = [i for i in range(40,44)]
kings = [i for i in range(44,48)]
aces = [i for i in range(48,52)]

card_nums = [twos,threes,fours,fives,sixes,sevens,eights,nines,tens,jacks,queens,kings,aces]

def isFlush(hand):
    #lists with all the cards of each suit
    clubs = [i for i in range(0,52,4)]
    diamonds = [i for i in range(1,52,4)]
    hearts = [i for i in range(2,52,4)]
    spades = [i for i in range(3,52,4)]

    suits = [clubs,diamonds,hearts,spades]

    #check both players' hands for flushes
    for suit in suits:
        if len(np.intersect1d(hand, suit)) == 5:
            return True
        else:
            return False
    
def isStraight(hand):
    #list to hold number/face values of cards
    player_nums = []

    #convert cards from 0-51 value to thier number/face value
    for i in range(len(hand)):
        for j in range(len(card_nums)):
            if hand[i] in card_nums[j]:
                player_nums.append(j+2)
    
    #check if the card numbers/faces are consecutive to determine if hand is a straight
    player_nums = np.sort(player_nums)
    if player_nums == list(range(np.min(player_nums), np.max(player_nums)+1)):
        return True
    else: 
        return False

def isStraightFlush(hand):
    if isFlush(hand) and isStraight(hand):
        return True
    else:
        return False

def isRoyalFlush(hand):
    #checks if hand is a straight flush with lowest card being a ten
    if isStraightFlush(hand) and (np.min(hand) in range(32,36)):
        return True
    else:
        return False

def isFourOfAKind(hand):
    for card_num in card_nums:
        if len(np.intersect1d(hand, card_num)) == 4:
            return True
        else:
            return False

def isThreeOfAKind(hand):
    for card_num in card_nums:
        if len(np.intersect1d(hand, card_num)) == 3:
            return True
        else:
            return False

def isOnePair(hand):
    for card_num in card_nums:
        if len(np.intersect1d(hand, card_num)) == 2:
            return True
        else:
            return False

def isFullHouse(hand):
    if isThreeOfAKind(hand) and isOnePair(hand):
        return True
    else:
        return False

def isTwoPair(hand):
    pairs = 0
    for card_num in card_nums:
        if len(np.intersect1d(hand, card_num)) == 2:
            pairs += 1
    
    if pairs == 2:
        return True
    else:
        return False