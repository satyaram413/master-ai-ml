
import this
s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.islower():
        print(char, end='\n')

for i in range(5):
    print("Doing Important work i =", i)
i=0
while i < 10:
    print("i::: ", i)
    i+=1
squares=[n**2 for n in range(10)]
print(squares)

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)

print(sum([num%7==0 for num in [1,2,3,4,5,6,7,7,14,46,32,42]]))

negtive_array=[5,-1,2,4,-4,-5]
print(len([num for num in negtive_array if num < 0]))
print(sum([num < 0 for num in negtive_array]))

def word_search(documents, keyword):
    # list to hold the indices of matching documents
    indices = []
    # Iterate through the indices (i) and elements (doc) of documents
    for i, doc in enumerate(documents):
        # Split the string doc into a list of words (according to whitespace)
        tokens = doc.split()
        # Make a transformed list where we 'normalize' each word to facilitate matching.
        # Periods and commas are removed from the end of each word, and it's set to all lowercase.
        normalized = [token.rstrip('.,').lower() for token in tokens]
        # Is there a match? If so, update the list of matching indices.
        if keyword.lower() in normalized:
            indices.append(i)
    return indices