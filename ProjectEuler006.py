# Project Euler - problem 006 - SUM SQUARE DIFFERENCE
#
# The sum of the squares of the first ten natural numbers is,
# 1(2) + 2(2) + ... + 10(2) = 385
#
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
#
# Hence the difference between the sum of the squares of the first
# ten natural numbers and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.

sumofsquares = 0
totaltosquare = 0
for count in range(101):
	sumofsquares += count**2
	totaltosquare += count
    
print """The difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum is: """, totaltosquare**2 - sumofsquares
