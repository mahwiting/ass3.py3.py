##########################################
#### EXERCISE 1 30 MARKS############
###########################################

# Assignment 3: Python

#PROBLEM 1
# Given the string:
s= 'fullstackslp'

# Q1
print(s[0])

# Q2
print(s[-1])

# Q3
print(s[4:9])

# Q4
print(s[-3:])

# Q5
print(s[6:9])

# Q6
print(s[::-1])

#PROBLEM 2

d1 = {'simple_key': 'hello'}

# Q1
print(d1['simple_key'])

# Q2

d2 = {'k1': {'k2': 'hello'}} 
print(d2['k1']['k2'])


# Q3
d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]} 

print(d3['k1'][0]['nest_key'][1][0])

# PROBLEM 3
age = 45
name = "Kyle"
print("Hello my dog's name is {} and he looks {} years old".format(name, age))