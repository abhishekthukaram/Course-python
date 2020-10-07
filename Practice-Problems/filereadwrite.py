f = open('file.txt', 'r')
countries=[]
for line in f:
    line = line.strip()
    countries.append(line)

f.close()
#print (countries)
#print(len(countries))
for country in countries:
    if country.startswith('T'):
        print (country)

file = open('scores.txt', 'w')

while True:
    participant = raw_input("Name:")
    if participant == 'quit':
        print "Quitting"
        break
    score = raw_input("Score for"+ participant+ "")
    file.write(participant+ "," + score+ '\n')
file.close()