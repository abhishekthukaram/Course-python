"""
Write a function that takes an integer flight_length (in minutes) and a list of integers movie_lengths (in minutes) and
returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.
"""


def inflight(flight_length, movie_lengths):
    second_movie_list = set()
    for i in range(len(movie_lengths)):
        if len(movie_lengths) == 0:
            return False
        second_movie = flight_length - movie_lengths[i]
        if second_movie in second_movie_list:
            return True
        second_movie_list.add(movie_lengths[i])
    return False
