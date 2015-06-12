# Problem 20 - Factorial Digit Sum
print "Problem 20 - Factorial Digit Sum"

num = 1
for x in range(1, 101):
    num *= x
num_str = str(num)
num_len = len(num_str)
num_total = 0
for x in range(0, num_len):
    num_total += int(num_str[x])
print num_total
