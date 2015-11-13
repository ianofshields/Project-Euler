# python

a = 600851475143
i = 2;

while (a > i):
	if (a%i == 0):
		a /= i
		i = 2
	else:
		i += 1

print i
