# Project Euler - problem 009 - SPECIAL PYTHAGOREAN TRIPLET
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

sumofprimes = 0
testnumbers = set(range(2000001,1,-2))
while testnumbers:
    prime = testnumbers.pop()
    sumofprimes += prime
    testnumbers.difference_update(xrange(prime*2, 2000001, prime))

print "The sum of all the primes bellow two million is: ",sumofprimes
