# Problem 9 - Special Pythagorean Triplet
print "Problem 9 - Special Pythagorean Triplet"

def check_pythagorean_constraint(a, b, c):
    if (a**2 + b**2 == c**2):
	return True
    else:
	return False

def check_sum_constraint(a, b, c):
    if (a + b + c) == 1000:
	return True
    else:
	return False

def check_order_constraint(a, b, c):
    if a < b and b < c:
	return True
    else:
	return False

def check_constraints(a, b, c):
    if check_pythagorean_constraint(a, b, c) and check_sum_constraint(a, b, c) and check_order_constraint(a, b, c):
	return True
    else:
	return False

def wrapper_func():
    i = 0
    j = 0
    k = 0
    for i in range(1, 1000):
	for j in range(i, 1000):
	    for k in range(j, 1000):
		if check_constraints(i, j, k):
		    return i*j*k

print wrapper_func()
