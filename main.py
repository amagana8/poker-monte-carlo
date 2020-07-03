from monte_carlo import *

#wrapper function that prompts user for inputs
#for the call to monteCarloPoker()
#and then prints out a setence summarizing the results
print("Enter your cards in the form '5c' for 5 of Clubs or 'Jh' for Jack of Hearts")
card1 = input("Enter your first card: ")
card2 = input("Enter your second card: ")
starting_hand = [card1, card2]

N = int(input("Enter number of times to simulate the round: "))
n_players = int(input("Enter number of other players in the game: "))
   
results = monteCarloPoker(N, n_players, starting_hand)
winPercent = results[0] * 100
losePercent = results[1] * 100
tiePercent = results[2] * 100
print("In {} different rounds, your hand of {} and {} won {:.3f}% of the rounds, lost {:.3f}% of the rounds, and tied {:.3f}% of the rounds.".format(N,card1,card2,winPercent,losePercent,tiePercent))
