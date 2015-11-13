# Project Euler problem 001.
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

sumofmultiples = 0
for testnumber in range(1000):
	if testnumber % 3 == 0 or testnumber % 5 == 0:
		sumofmultiples += testnumber
			
print "The sum of the multiple of 3 and 5 below 1000 is: ",sumofmultiples
