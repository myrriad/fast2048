# To run on TI-84:

Send A2048.8xp, M2048.8xp, S2048.8xp, D2048.8xp to the calculator.

A2048 is the main program, and you run it to play the game.

# Descriptions

A2048 is the main program.

S2048, M2048, and D2048 are dependency subroutines.\
S2048 shifts the numbers left.\
M2048 performs the merge. prgmS2048 followed by prgmM2048 results in a game step.\
D2048 displays the game list data using a trick involving and 'Fix 2'.

# Theorycrafting

derivation.PNG provides a derivation for the left shift in S2048.\
Similar boolean logic was used to program M2048.

S2048 and M2048 only work for the case of shifting left. In order to allow all directions to work, the list is transformed in our desired direction, then transformed back.

S2048 and M2048 are state functions and are technically O(n).

Benchmark: 25 shifts in 38.52s = 1.54 s/shift
