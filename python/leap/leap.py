def is_leap_year(year):
    if year % 4 == 0:
    	if year % 100 == 0:
    		if year % 400 == 0:
    			return True			# ... divisible by 4, 100 and 400 
    		else:
    			return False		# ... divisible by 4, 100 and not by 400
    	else:
    		return True				# ... divisible by 4  
    else:
    	return False				# ... not divisible by 4 