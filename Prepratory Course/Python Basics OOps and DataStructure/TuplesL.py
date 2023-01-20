t=(1,2,4)
print(t)
# or
t= 1,2,4,5,"Red"
print(t)
# tuples are immutables
# Tuples are often used for functions that have multiple return values like as_integer_ratio()
x=0.125;
numerator , denominator= x.as_integer_ratio()
print(x.as_integer_ratio())
print(numerator, denominator, sep="/")
a=1
b=0
a,b=b,a
print(a,b)