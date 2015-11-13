# Project Euler - problem 007 - 10001ST PRIME NUMBER
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
#
# What is the 10001st prime number?

def testifprime(primecandidate):
    for j in range(3, int(1 + (primecandidate**0.5)), 2):
        if primecandidate % j == 0:
			return 0
    return 1

primecount = 1
primecandidate = 3
while primecount < 10001:
    if testifprime(primecandidate):
        primecount += 1
    primecandidate += 2

print "The 10001st prime number is: ", primecandidate-2
