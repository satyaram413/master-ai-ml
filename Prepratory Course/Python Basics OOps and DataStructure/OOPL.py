class Solution:
    nums=0
    # instance Method just like __init__ method
    def twoSum(self):
        print("Satya")
        print(self.nums)
        print(self.target)
    def __init__(self,nums, target):
        self.nums =nums
        self.target= target
    #     __init__ and __str__ are called dunder methods because they end with __
    # to call __str__ method jst call the instance object.
    def __str__(self):
        print("Dunder Method")
        return f"Dunder Method {self.nums}"




# Python creates a new instance and passes it to the first parameter of .__init__().
# This essentially removes the self parameter, so you only need to worry about
# the name and age parameters.
# Attributes created in .__init__() are called instance attributes.
# An instance attribute’s value is specific to a particular instance of the class.
# All Dog objects have a name and an age, but the values for the name and age attributes will
# vary depending on the Dog instance.
#
# On the other hand, class attributes are attributes that have the same value for all class instances.
# You can define a class attribute by assigning a value to a variable name outside of .__init__().
b=Solution(12,24)
# b.twoSum(12,24)
b.nums=123
b.target=89
print(b.target)

b.twoSum()
print(b)