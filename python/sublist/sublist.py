SUBLIST = 'SUBLIST'
SUPERLIST = 'SUPERLIST'
EQUAL = 'EQUAL'
UNEQUAL = 'UNEQUAL'


def check_lists(first_list, second_list):
    if first_list == second_list:
    	return EQUAL
    if  len(first_list) < len(second_list):
    	shorter_list = first_list
    	longer_list = second_list
    else:
    	shorter_list = second_list
    	longer_list = first_list
    if len(first_list) is 0:
    	return SUBLIST
    if len(second_list) is 0:
    	return SUPERLIST
    for i in range(len(longer_list) - len(shorter_list) + 1):
    	if longer_list[i] == shorter_list[0]:
    		flag = True
    		for j in range(1,len(shorter_list)):
    			if longer_list[i+j] != shorter_list[j]:
    				flag = False
    				break
    		if flag:
    			if len(first_list) < len(second_list):
    				return SUBLIST
    			else:
    				return SUPERLIST
    return UNEQUAL