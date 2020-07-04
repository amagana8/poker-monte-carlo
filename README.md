# Poker-Monte-Carlo
Uses Monte Carlo Methods to determine the probability a starting hand in poker will win the round.\
Given the starting hand you were dealt in a game of Texas Hold 'Em Poker, this program simulates multiple games, randomizing the other players' cards as well as the flop,turn, and river each time, to determine the probability your starting hand will win any given game.

The program asks the user for their starting hand, the number of other players in the game, and how many times to simulate the game.\
It then tells you the percentage of those rounds that your hand won, lost, or tied. Thus, giving you the probability your starting hand will win the game.

# Graphs
These graphs are made using data generated my code. They show how the precision of the probability estimates increase as more games are simulated.\
There is a graph for 3 different starting hands.

### Ace of Spades and Ace of Hearts
<img src="https://i.imgur.com/BV1V1RY.png" width="500"/>

### 2 of Clubs and 7 of Diamonds
<img src="https://i.imgur.com/gzQ0JG2.png" width="500"/>

### 6 of Diamonds and Jack of Hearts
<img src="https://i.imgur.com/zbO6KNC.png" width="500"/>

# Examples
Example results with different starting hands.\
There is a screenshot for each of the 3 staring hands above.

### Ace of Spades and Ace of Hearts
![screenshot1](https://i.imgur.com/YVbRE8G.png)

### 2 of Clubs and 7 of Diamonds
![screenshot2](https://i.imgur.com/Qa30QCY.png)

### 6 of Diamonds and Jack of Hearts
![screenshot3](https://i.imgur.com/grvOxES.png)

# Dependencies
This program uses the following python packages.
  * NumPy
    * Numpy is used throughout the program for many of the various calculations.
  * Matplotlib
    * Matplotlib is not necessary to use this program. It is only used here to produce graphs like the ones above, to show the change in the probability estimates as more games are simulated.
