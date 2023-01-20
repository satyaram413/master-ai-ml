
print("Hello")
myFloat=7.0;
print(myFloat)
myFloat= float(7)
print(myFloat)
myString ="My Fellow's Akka"
print(myString)
a, b=3,4;
print(a,b)
print(a + b)
print(a + b+ myFloat)
# print(a + b+ myString) doesnt work typcasting error nsupported format
print(17/3)
print(17//3)
print(17%3)
print(5**2)
print(5 * "hello")
print(type(myFloat))
print(-a)

# Order of Operations, PEMDAS- Parenthesis, Exponents, Multiplication/Division, addition/Subtraction
print(min(1,2,3,4))
print(abs(123))
print(int('901') + 1)
help(abs)

# All values are true expect for zero
# empty strings are treated as false,
print(bool(123))
print(bool(0))
print(bool("asf"))
print(bool(""))

# Conditional Statement
if not 0:
    print("Conditional")
elif "spam":
    print("Super")

# prepared_for_weather = (
#         have_umbrella
#         or ((rain_level < 5) and have_hood)
#         or (not (rain_level > 0 and is_workday))
# )
# help(abs)

# In python conditions are executed based on precedence, and not from left to right insie if condition
# https://docs.python.org/3/reference/expressions.html#operator-precedence
print(int(True))
if(myString=="My Fellow's Akka" and myString!= ""):
    print("sasas")