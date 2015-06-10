# Problem 12 - Highly Divisible Triangular Number
print "Problem 12 - Highly Divisible Triangular Number"

def check_divisors():
    ctr = 1 # Number of natural numbers already added
    tri_num = 1 # Triangle number
    while True:
	x = 1
	upper_bound = tri_num + 1
	div_ctr = 0 # Divisor counter
	while x < upper_bound:
	    if tri_num % x == 0:
		div_ctr += 1
		upper_bound = tri_num / x
	    if div_ctr > 250: # If > 500 divisors
	        return tri_num
	    x += 1
	ctr += 1
	tri_num += ctr

ans = check_divisors()
print ans
