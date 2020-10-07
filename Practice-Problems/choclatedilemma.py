"""
Agatha and Bertha are sisters eating chocolate given to them by their parents. Bertha has always suspected her parents
of considering Agatha as the favorite child. To settle this dispute once and for all, she decides to analyze all pieces
of chocolate split between them, and determine that if they both have an equal amount of chocolate, then no
favoritism exists.

Create a function that returns true if the total amount of chocolate is identical for each sister. All chocolate
are given in rectangular pieces that are represented by a pair of coordinates for length and width. Sum up the total
area of chocolate for each sister, and return true if the total area of chocolate is the same.

"""


def test_fairness(agatha, bertha):
    result_agatha = 0
    result_bertha = 0
    for i in range(len(agatha)):
        result_agatha+=agatha[i][0]* agatha[i][1]
    print (result_agatha)
    for j in range(len(bertha)):
        result_bertha+=bertha[j][0]*bertha[j][1]
    print result_bertha
    return result_agatha==result_bertha


print(test_fairness([[4, 3], [2, 4], [1,2]], [[6,2], [4,2], [1,1], [1,1]]))