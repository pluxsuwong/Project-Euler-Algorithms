# Problem 14 - Longest Collatz Sequence
print "Problem 14 - Longest Collatz Sequence"

def odd_rule(num):
    return 3*num + 1

def even_rule(num):
    return num / 2

def collatz_seq(start):
    chain_ctr = 0
    num = start
    while num != 1:
	if num % 2 == 0:
	    num = even_rule(num)
	else:
	    num = odd_rule(num)
	chain_ctr += 1
    return chain_ctr

record_list = []
for start_num in range(1, 1000000):
    record_cnt = collatz_seq(start_num)
    record_list.append((record_cnt, start_num))

record_list.sort()
print record_list[-1]
