# Project Euler problem 005.
#
# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly
# divisible by all of the numbers from 1 to 20?

testnumber = 0
found = False
while not found:
	testnumber += 20
	counter = 0
	for testdivisor in range(11,20):
		if testnumber % testdivisor == 0:
			counter +=1
	if counter == 9:
		found = True
print """The smallest positive number that is evenly divisible
by all of the numbers from 1 to 20 is: """, testnumber
