# Problem 001 - Multiples of 3 and 5
print "Problem 001 - Multiples of 3 and 5"

sum = 0
for x in range(0, 1000):
    if x % 3 == 0 or x % 5 == 0 :
        sum += x

print sum
