def least_difference(a, b, c):
    """Dostring are used to provide documentation
    >>>least_difference(1,4,5)
    4
    """
    diff1 = abs(a - b)
    diff2 = min(a, b, c)
    diff3 = max(a, b, c)
    return min(diff1, diff2, diff3)


print(least_difference(3, 42, 52), least_difference(4, 5, 6))
help(least_difference)


def least_difference1(a, b, c):
    """Dostring are used to provide documentation
    >>>least_difference1(1,4,5)
    4
    """
    diff1 = abs(a - b)
    diff2 = min(a, b, c)
    diff3 = max(a, b, c)


# Though the above function is not returnng anything we can call it out from print statement, in this case it returns NONE
print(least_difference1(3, 42, 52), least_difference1(4, 5, 6))


def greet(who="collin"):
    print("Hello ", who)
    return "robo"


greet()


def call(fn, arg):
    return fn(fn(arg))


call(greet, "Satya")

# functions which operate on other functions are called higher order functions'


def mod_5(x):
    return x % 5


"""Return the remainder of x after dividing by 5"""


print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)
print(round(9.99999, 2))


def to_smash(total_candies, name=None):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.

    >>> to_smash(91)
    1
    """
    if name is not None:
        return total_candies % name
    else:
        return total_candies % 3


print(to_smash(10))
print(to_smash(10, 2))
