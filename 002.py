# Problem 2 - Even Fibonacci Numbers
print "Problem 2 - Even Fibonacci Numbers"

sum = 0
a = 1
b = 2
while b < 4000000:
    if b % 2 == 0:
        sum += b
    x = a + b
    a = b
    b = x

print sum
