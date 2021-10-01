hands = [[1, 2], [123, 4, 3], [2, "Hello", "World"]]
print(hands[0][1])
# //next closest
# list are mutable

# // more farthest
print(hands[-1][1])

# slicing a list
print((hands[1:-1]))
hands[2] = [3, 5, 6]
print(hands)

planets = ["mer", "ven", "ear", "Mars"]
print(planets)
planets[:3] = ["mercury", "venus", "earth"]
print(planets)
print(len(planets))
print(sorted(planets))
print(planets)
print(sum(hands[1]))
d = [1, 2, 3][1:]
print(len(d))
# //you can pass list of lists for max function, the same doesnt work with sum function, sum function only takes list of integer
print(max(hands))
x = 12 + 3j
y = 3
print(x.imag)
print(y.bit_length())
help(y.bit_length)
planets.append("pluto")
# append adds to the last, pop removes last entry from the list
print(planets)
if "earth" in planets:
    print(planets.index("earth"))

party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']


def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    q = round(len(arrivals)/2)
    l = arrivals[q:-1]
    return name in l


print(fashionably_late(party_attendees, "Adela"))

# def fashionably_late(arrivals, name):
#     order = arrivals.index(name)
#     return order >= len(arrivals) / 2 and order != len(arrivals) - 1
