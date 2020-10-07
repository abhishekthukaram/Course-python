"""
Limit a Number's Value
Create a function that takes three number arguments one number as an input and two additional numbers representing
the endpoints of a closed range  and return the number limited to this range.
If the number falls within the range, the number should be returned.
If the number is less than the lower limit of the range, the lower limit should be returned.
If the number is greater than the upper limit of the range, the upper limit should be returned.
Examples
limit_number(5, 1, 10) gives 5
limit_number(-3, 1, 10) gives 1
limit_number(14, 1, 10) gives 10
limit_number(4.6, 1, 10) gives 4.6
"""


def limit_number(num, range_low, range_high):
    if range_high >= num >= range_low:
        return num
    elif num< range_low:
        return range_low
    else:
        return range_high


print limit_number(5, 1, 10)
print limit_number(-3, 1, 10)
print limit_number(14, 1, 10)