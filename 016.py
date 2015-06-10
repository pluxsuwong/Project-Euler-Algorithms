# Problem 16 - Power Digit Sum
print "Problem 16 - Power Digit Sum"

big_num = 2**1000
big_num_str = str(big_num)

big_num_digs = []
for i in range(0, len(big_num_str)):
    big_num_digs.append(int(big_num_str[i]))

total_sum = 0
for dig in big_num_digs:
    total_sum += dig

print total_sum
