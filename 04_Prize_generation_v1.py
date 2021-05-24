# Could not remember if I should use randint or randrange so checked that
# randint would randomly generate all four of the numbers 1, 2, 3, 4

import random

NUM_TRIALS = 10

for item in range(0, NUM_TRIALS):

    # randint finds numbers between given endpoints, including both endpoints
    prize_num = random.randint(1,4)
    print(prize_num)
    