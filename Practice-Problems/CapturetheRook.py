"""
A chessboard has rows numbered 1-8 and columns numbered A-H. In chess, rooks are pieces that can any number of squares
horizontally or vertically.Given the location of your rook and your opponent's rook, determine whether or not you can
capture your opponent's rook with your own. For this exercise, assume there are no other pieces that are blocking.
Your position and your opponent's position are represented as the first and second element
of the input list, respectively.
For instance, in this example: can_capture(["A8", "E8"]) True your rook (at A8) can take your opponents rook (at E8)
by moving horizontally.
"""


def can_capture(rooks):
    if rooks[0][0] == rooks[1][0] or rooks[0][1] == rooks[1][1]:
        return True
    else:
        return False


print (can_capture(["A8", "E8"]))
print (can_capture(["A1", "B2"]))
print(can_capture(["H4", "H3"]))
print (can_capture(["F5", "C8"]))