f = open("countries.txt", mode='r')
countries = []
for line in f:
    line = line.strip()
    countries.append(line)
for country in countries:
    if country[0] == 'I':
        print(country)
f.close()
