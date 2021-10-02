# Poker-Monte-Carlo
Uses Monte Carlo Methods to determine the probability that a given starting hand in poker will win the round.\
This program simulates multiple games, randomizing the other players' cards as well as the flop, turn, and river each time, to determine the probability your starting hand will win any given game.

The program asks the user for their starting hand, the number of other players in the game, and how many times to simulate the game.\
Afterwards, it tells you the percentage of those rounds that your hand won, lost, or tied. Thus, giving you the probability your starting hand will win the game.

# Graphs
These graphs are made using data generated by this program. They show how the precision of the probability estimates increase as more games are simulated.\
Below are graphs for 3 different starting hands.

### Ace of Spades and Ace of Hearts
![image](https://user-images.githubusercontent.com/26752458/135728430-3331a045-03be-4fab-86a1-c731c82e6586.png)

### 2 of Clubs and 7 of Diamonds
![image](https://user-images.githubusercontent.com/26752458/135728410-9a31035d-0e4b-4e8a-9cb8-8a18cb5b4a55.png)

### 6 of Diamonds and Jack of Hearts
![image](https://user-images.githubusercontent.com/26752458/135728399-cc2cc567-e745-4eb6-a0a3-d58159e0063d.png)

# Examples
Example results with different starting hands.\
Below are screenshots for the same 3 staring hands above.

### Ace of Spades and Ace of Hearts
![image](https://user-images.githubusercontent.com/26752458/135726108-7d551682-6a53-4d6e-94f7-d2d2178d5883.png)

### 2 of Clubs and 7 of Diamonds
![image](https://user-images.githubusercontent.com/26752458/135726155-33004fe0-6ad9-4ee8-b4dc-c3eb2438bc81.png)

### 6 of Diamonds and Jack of Hearts
![image](https://user-images.githubusercontent.com/26752458/135726207-a63fa33b-78c6-4264-adba-2abda95dcc50.png)

# Dependencies
This program uses the following python packages.
  * NumPy
    * Numpy is used throughout the program for many of the various calculations.
  * Matplotlib
    * Matplotlib is not necessary for this program. It is only used here to produce graphs like the ones above, to show how the probability estimates are affected by the number of games simulated.
