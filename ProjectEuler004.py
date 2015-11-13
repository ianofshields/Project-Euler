# Project Euler problem 004.
#
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 x 99
#
# Find the largest palindrome made from the product of two 3-digit numbers.

largest = 0
for firsttest in range(100, 999):
    for secondtest in range(100, 999):
        if str(firsttest * secondtest) == str(firsttest * secondtest)[::-1]:
            if largest < firsttest * secondtest:
			    largest = firsttest * secondtest
			
print "The largest palindrome made from the product of two 3-digit numbers is :", largest
