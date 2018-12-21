"""
Assuming a game of Monopoly with the standard board, a player starts on the GO
square and adds the scores on two 6-sided dice to determine the number of squares
they advance in a clockwise direction. Without any further rules we would expect
to visit each square with equal probability: 2.5%. However, landing on G2J (Go
To Jail), CC (community chest), and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player
to go directly to jail, if a player rolls three consecutive doubles, they do not
advance the result of their 3rd roll. Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player
lands on CC or CH they take a card from the top of the respective pile and, after
following the instructions, it is returned to the bottom of the pile. There are
sixteen cards in each pile, but for the purpose of this problem we are only
concerned with cards that order a movement; any instruction not concerned with
movement will be ignored and the player will remain on the CC/CH square.

    Community Chest (2/16 cards):
        Advance to GO
        Go to JAIL
    
    Chance (10/16 cards):
        Advance to GO
        Go to JAIL
        Go to C1
        Go to E3
        Go to H2
        Go to R1
        Go to next R (railway company)
        Go to next R
        Go to next U (utility company)
        Go back 3 squares.

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
The heart of this problem concerns the likelihood of visiting a particular
square. That is, the probability of finishing at that square after a roll. For
this reason it should be clear that, with the exception of G2J for which the
probability of finishing on it is zero, the CH squares will have the lowest
probabilities, as 5/8 request a movement to another square, and it is the final
square that the player finishes at on each roll that we are interested in. We
shall make no distinction between "Just Visiting" and being sent to JAIL, and we
shall also ignore the rule about requiring a double to "get out of jail",
assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can
concatenate these two-digit numbers to produce strings that correspond with sets
of squares.

Statistically it can be shown that the three most popular squares, in order, are
JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So
these three most popular squares can be listed with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.

Solution: 101524
"""
import random
from collections import Counter

def PE_84(die_size, seed=1):
    """
    >>> PE_84(6)
    '102400'

    >>> PE_84(4)
    '101524'
    """
    
    # seed random number generator
    random.seed(seed)
    
    # specify number of rolls
    TURN_LIMIT = 10000000
    
    current_cell = turn_counter = 0
    cell_counter = Counter()
    while turn_counter < TURN_LIMIT:
        
        # basic game mechanics
        turn_counter += 1
        roll, is_double_roll = roll_dice(die_size)
        current_cell = (current_cell + roll) % 40
        
        # allow for "three double rolls feature"
        if is_double_roll:
            double_roll_count += 1
        else:
            double_roll_count = 0

        if double_roll_count == 3:
            current_cell = 10
            double_roll_count = 0

        # take action depending on square landed on
        current_cell = check_square_action(current_cell)
        
        # mark current cell as "landed on"
        cell_counter[current_cell] += 1

    result_string = ""
    for key, _ in cell_counter.most_common(3):
        result_string += "{:0<2d}".format(key)
    return result_string


def roll_dice(die_size):
    roll1 = random.randint(1, die_size)
    roll2 = random.randint(1, die_size)
    return roll1 + roll2, roll1 == roll2


def check_square_action(current_cell):
    
    # allow for "Go To Jail"
    if current_cell == 30:
        return 10
    
    # allow for Community Chest cards
    if current_cell in {2, 17, 33}:
        
        random_community_chest_card = random.random()
        
        # "Advance To Go"
        if random_community_chest_card <= 0.0625:
            return 0
        
        # "Go To Jail"
        if random_community_chest_card <= 2 * 0.0625:
            return 10
    
    # allow for Chance cards
    if current_cell in {7, 22, 36}:
        
        random_chance_card = random.random()
        
        # "Advance To Go"
        if random_chance_card <= 0.0625:
            return 0
        
        # "Go To Jail"
        if random_chance_card <= 2 * 0.0625:
            return 10
        
        # Go To C1
        if random_chance_card <= 3 * 0.0625:
            return 11
        
        # Go to E3
        if random_chance_card <= 4 * 0.0625:
            return 24
        
        # Go to H2
        if random_chance_card <= 5 * 0.0625:
            return 39
        
        # Go to R1
        if random_chance_card <= 6 * 0.0625:
            return 5
        
        # Go back 3 squares
        if random_chance_card <= 7 * 0.0625:
            return current_cell - 3
        
        # Go to next U (utility company)
        if random_chance_card <= 8 * 0.0625:
            if current_cell < 12 or current_cell > 28:
                return 12
            else:
                return 28

        # Go to next R (railway company) x 2
        if random_chance_card <= 10 * 0.0625:
            if current_cell < 5 or current_cell > 35:
                return 5
            elif current_cell > 5 and current_cell < 15:
                return 15
            elif current_cell > 15 and current_cell < 25:
                return 25
            elif current_cell > 25 and current_cell < 35:
                return 35

    return current_cell


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
