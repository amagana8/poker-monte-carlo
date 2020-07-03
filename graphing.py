import numpy as np
import matplotlib.pyplot as plt
from monte_carlo import *

def monteCarloSims(M,N,n_players,starting_hand):
    win_prob = np.array([])
    for i in range(M):
        results = monteCarloPoker(N, n_players, starting_hand)
        win_prob = np.append(win_prob, results[0])
    return win_prob


print("Enter your cards in the form '5c' for 5 of Clubs or 'Jh' for Jack of Hearts")
card1 = input("Enter your first card: ")
card2 = input("Enter your second card: ")
starting_hand = [card1, card2]

win_prob_20 = monteCarloSims(100, 20, 3, starting_hand)
win_prob_100 = monteCarloSims(100, 100, 3, starting_hand)
mean_20 = np.mean(win_prob_20)
mean_100 = np.mean(win_prob_100)
std_20 = np.std(win_prob_20)
std_100 = np.std(win_prob_100)


plt.hist(win_prob_20,alpha=0.5, label='20 games')
plt.hist(win_prob_100,alpha=0.5, label='100 games')
plt.title('Starting Hand ' + str(starting_hand))
plt.legend(loc='upper left')
plt.xlabel('Probability of Winning')
plt.ylabel('# of Occurances')
plt.show()
