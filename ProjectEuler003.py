# Project Euler problem 001.
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

target = 600851475143
primetest = 2;

while (target > primetest):
	if (target % primetest == 0):
		target /= primetest
		primetest = 2
	else:
		primetest += 1

print "The largest prime factor of the number 60085147513 is: ", primetest
