def find_first_prime_which_devides(natural_number):
	temp = natural_number
	numbers = list()
	while temp:
		temp -= 1
		numbers += [True]
	for prime in xrange(2,(long(natural_number**(0.5))+1)):
		if numbers[prime]:
			if natural_number % prime == 0:
				print "rt",prime
				return prime

			j = 0
			while prime*prime+j*prime <= natural_number:
				numbers[prime*prime+j*prime] = False
				j += 1
	return natural_number

	

def prime_factors(natural_number):
	prime_factors = list()
	while natural_number != 1:
		prime = find_first_prime_which_devides(natural_number)
		print "pf",prime
		prime_factors.append(prime)
		natural_number /= prime
	return prime_factors

print prime_factors(93819012551)	