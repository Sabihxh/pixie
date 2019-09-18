def generate_primes_under(n=100):
	"""
	Returns list of all prime numbers <= n
	"""
	for possiblePrime in range(2, n + 1): # Assume number is prime until shown it is not. 
		isPrime = True
		for num in range(2, int(possiblePrime ** 0.5) + 1):
			if possiblePrime % num == 0:
				isPrime = False
				break        
		if isPrime:
			yield possiblePrime

