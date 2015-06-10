# Problem 7 - 10001st Prime
print "Problem 7 - 10001st Prime"

# Clever little function
def is_prime(a):
    return all(a % i for i in xrange(2, a))

counter = 0
x = 2
ans = 0
while counter < 10001:
    if is_prime(x) != 0:
	counter += 1
	ans = x
	print "%5d : %d" % (counter, ans)
    x += 1

print ans
