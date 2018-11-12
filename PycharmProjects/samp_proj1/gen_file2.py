# Reading a large file using generators

def BeerData():

    f = open("recipeData.csv")
    for line in f:
        yield line

beer = BeerData()
print(next(beer))
print(next(beer))

# Generator comprehension
# for gen function to be called we used a variable ret = gf() and used ret to call next function


lc = [n**2 for n in [1,2,3,4,5]]
ge = (n**2 for n in [1,2,3,4,5])

print(next(ge))

lines = (line for line in open('recipeData.csv'))
print(next(lines))
print(next(lines))
print(next(lines))

cols = (l.split(',') for l in lines)
columns = next(cols) # the header is iterated and stored
beerdicts = (dict(zip(columns,data)) for data in cols)
print(next(beerdicts))

# Consume generator

beer_counts = {}
for bd in beerdicts:
    if bd['Style'] not in beer_counts:
        beer_counts[bd['Style']] = 1
    else:
        beer_counts[bd['Style']] += 1

print(beer_counts)

