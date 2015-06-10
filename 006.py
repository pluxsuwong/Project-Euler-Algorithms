# Problem 6 - Sum Square Difference
print "Problem 6 - Sum Square Difference"

def sum_of_squares(num):
    sum = 0
    for x in range(1, num + 1):
	sum += x**2
    return sum

def square_of_sums(num):
    sum = 0
    for x in range(1, num + 1):
	sum += x
    return sum**2

final_diff = 0
num = 100
a = sum_of_squares(num)
b = square_of_sums(num)
if a > b:
    final_diff = a - b
else:
    final_diff = b - a

print final_diff
