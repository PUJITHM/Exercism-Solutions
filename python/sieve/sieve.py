def sieve(limit):
	numbers = [True for _ in range(limit+1)]
	for prime in range(2,(int(limit**(0.5))+1)):
		if numbers[prime]:
			j = 0
			while prime*prime+j*prime <= limit:
				numbers[prime*prime+j*prime] = False
				j += 1

	return [prime for prime,value in enumerate(numbers) if value][2:]