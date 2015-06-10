# Problem 3 - Largest Prime Factor
print "Problem 3 - Largest Prime Factor"

def is_prime(a):
    return all(a % i for i in xrange(2, a))

def find_max_prime(old_record, num):
    if num != 0 and is_prime(num) != 0:
	return num
    else:
	x = 2
	curr_record = 0
	while num % x != 0:
	    x += 1
	new_num = num / x
	if x > old_record:
	    curr_record = x
	else:
	    curr_record = old_record
	new_record = find_max_prime(curr_record, new_num)
	if new_record > curr_record:
	    return new_record
	else:
	    return curr_record

num = 600851475143
max_ans = find_max_prime(0, num)

print max_ans
