# Problem 4 - Largest Palindrome Product
print "Problem 4 - Largest Palindrome Product"

# Check if num == reverse_num
def is_palindrome(num):
    if str(num) == str(num)[::-1]:
	return 1
    else:
	return 0

ans = 0
for i in range(0, 1000):
    for j in range(0, 1000):
	x = i*j
	if is_palindrome(x) != 0:
	    if x > ans:
		ans = x

print ans
