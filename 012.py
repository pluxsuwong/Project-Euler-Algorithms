# Problem 12 - Highly Divisible Triangular Number
print "Problem 12 - Highly Divisible Triangular Number"

def check_divisors():
    ctr = 1 # Number of natural numbers already added
    tri_num = 1 # Triangle number
    while True:
	div_ctr = 0 # Divisor counter
	for x in range(1, tri_num + 1): 
	    if tri_num % x == 0:
		div_ctr += 1
	    if div_ctr > 500: # If > 500 divisors
	        return tri_num
	print "%d : %d" % (tri_num, div_ctr)
	ctr += 1
	tri_num += ctr

ans = check_divisors()
print ans
