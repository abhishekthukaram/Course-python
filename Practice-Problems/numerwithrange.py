"""
Given a number and a dictionary with min and max properties, return True if the number lies
within the given range (inclusive).
is_in_range(4, { "min": 0, "max": 5 }) gives True
is_in_range(4, { "min": 4, "max": 5 }) gives True
is_in_range(4, { "min": 6, "max": 10 }) gives False
is_in_range(5, { "min": 5, "max": 5 }) gives True
"""

def is_in_range(n, r):
    if n >= r['min'] and n <=r['max']:
        return True
    else:
        return False


print is_in_range(4, { "min": 0, "max": 5 })
print is_in_range(4, { "min": 4, "max": 5 })
print is_in_range(4, { "min": 6, "max": 10 })
print is_in_range(5, { "min": 5, "max": 5 })