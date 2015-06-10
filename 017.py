# Problem 17 - Number Letter Counts
print "Problem 17 - Number Letter Counts"

u_dic = {'1':"one", '2':"two", '3':"three", '4':"four", '5':"five",\
	 '6':"six", '7':"seven", '8':"eight", '9':"nine", '0':""}
u_dic_i = {'1':"eleven", '2':"twelve", '3':"thirteen", '4':"fourteen", '5':"fifteen",\
	 '6':"sixteen", '7':"seventeen", '8':"eighteen", '9':"nineteen", '0':"ten"}
t_dic = {'1':"ten", '2':"twenty", '3':"thirty", '4':"forty", '5': "fifty",\
	 '6':"sixty", '7':"seventy", '8':"eighty", '9':"ninety", '0':""}
# Spelled 'forty', not "fourty"

def int_to_string_ctr(num):
    num_str = str(num)
    digits = len(num_str)
    char_ctr = 0
    if digits == 1:
	char_ctr = len(u_dic[num_str])
	print(u_dic[num_str]),
    elif digits == 2:
	if num_str[0] == '1':
	    char_ctr = len(u_dic_i[num_str[1]])
	    print(u_dic_i[num_str[1]]),
	else:
	    char_ctr = len(t_dic[num_str[0]]) + len(u_dic[num_str[1]])
	    print(t_dic[num_str[0]] + u_dic[num_str[1]]),
    elif digits == 3:	
	if num_str[1] == '1':
	    u_and_t_val = len(u_dic_i[num_str[2]])
	    print(u_dic_i[num_str[2]]),
	else:
	    u_and_t_val = len(t_dic[num_str[1]]) + len(u_dic[num_str[2]])
	    print(t_dic[num_str[1]] + u_dic[num_str[2]]),

	if u_and_t_val > 0:
	    char_ctr = u_and_t_val + len(u_dic[num_str[0]]) + 10
	    print(u_dic[num_str[0]] + "andhundred"),
	else:
	    char_ctr = len(u_dic[num_str[0]]) + 7
	    print(u_dic[num_str[0]] + "hundred"),
    elif digits == 4:
	char_ctr = 11
	print("onethousand"),
    else:
	print "ERROR: Invalid number of digits"
    print str(char_ctr)
    return char_ctr

total_sum = 0
for i in range(1, 1001):
    total_sum += int_to_string_ctr(i)

print total_sum
