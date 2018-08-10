#####################################
#### PART 6: EXERCISE REVIEW  #######
#####################################

# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.

###############
## Problem 1 ##
###############

# Given the string:
s = 'django'

# Use indexing to print out the following:
# 'd'
print("problem 1:", s[0])

# 'o'
print("problem 2:", s[5])

# 'djan'
print("problem 3:", s[0], s[1], s[2], s[3])

# 'jan'
print("problem 4:", s[1], s[2], s[3])

# 'go'
print("problem 5:", s[4], s[5])

# Bonus: Use indexing to reverse the string
print("problem 4:", s[1], s[2], s[3])

print("Bonus:", s[::-1])

###############
## Problem 2 ##
###############

# Given this nested list:
l = [3, 7, [1, 4, 'hello']]
# Reassign "hello" to be "goodbye"
l[2][2] = "Goodbye"
print("Nested Problem:", l)


###############
## Problem 3 ##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key': 'hello'}
print("Keys 1:", d1["simple_key"])

d2 = {'k1': {'k2': 'hello'}}
print("Keys 2", d2["k1"]["k2"])

d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print("Keys 3", d3["k1"][0]["nest_key"][1])

###############
## Problem 4 ##
###############

# Use a set to find the unique values of the list below:
mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
print("Problem 4:", set(mylist))

###############
## Problem 5 ##
###############

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"

print(f"Hello my dogs name is {name} and he is {age} years old")
# print("Hello my dogs name is {} and he is {} years old".format(name, age))

# i = 1
# while i<5:
# 	print (f"i is: {i}")
# 	i += 1