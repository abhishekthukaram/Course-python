"""
Andy, Ben and Charlotte are playing a board game. The three of them decided to come up with a new scoring system.
A player's first initial ("A", "B" or "C") denotes that player scoring a single point. Given a string of capital
letters, return a list of the players' scores.

For instance, if ABBACCCCAC is written when the game is over, then Andy scored 3 points, Ben scored 2 points,
and Charlotte scored 5 points, since there are 3 instances of letter A, 2 instances of letter B, and 5 instances of
letter C. So the list [3, 2, 5] should be returned.
"""


def calculate_scores(txt):
    count_a=count_b=count_c =0
    for i in txt:
        if i =="A":
            count_a+=1
        elif i=='B':
            count_b+=1
        else:
            count_c+=1
    return [count_a,count_b,count_c]