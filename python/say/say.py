#data 
basic_num = {
			 0: ' zero',
			 1: ' one', 
			 2: ' two', 
			 3: ' three', 
			 4: ' four', 
			 5: ' five', 
			 6: ' six', 
			 7: ' seven', 
			 8: ' eight', 
			 9: ' nine', 
			 10: ' ten', 
			 11: ' eleven', 
			 12: ' twelve', 
			 13: ' thirteen', 
			 14: ' fourteen', 
			 15: ' fifteen', 
			 16: ' sixteen', 
			 17: ' seventeen', 
			 18: ' eighteen', 
			 19: ' nineteen', 
			 20: ' twenty', 
			 30: ' thirty', 
			 40: ' forty', 
			 50: ' fifty', 
			 60: ' sixty', 
			 70: ' seventy', 
			 80: ' eighty', 
			 90: ' ninety'
			 }
and_flag = True

#This function will split the 3 digit num into hundreds, tens and units places of num
def split_Three_Digits(num):
	return ( (num%1000-num%100)/100, (num%100-num%10)/10, num%10 )

#This function will 
def handle_Three_Digit(num,flag):
	temp = str()
	global and_flag
	if flag and and_flag:
		temp = " and"
		and_flag = False

	if num in basic_num:							# If num in basic numbers
		return temp + basic_num[num]
	msg = str()
													# splliting num into hundreds, tens and units places 
	(h, t, u) = split_Three_Digits(num)
													# compute hundreds 
	if h:
		msg = basic_num[h] + " hundred"
													# if 'and' is required append and
	if num%100 and (h or flag):
		msg += " and"
		and_flag = False
													#if last 2 digits are in basic numbers
	if num%100 in basic_num and num%100:
		return msg + basic_num[num%100]
													#compute last 2 digits
	if t>=2:
		return msg + basic_num[t*10] + "-" + basic_num[u][1:]
	return msg

		

def say(number):
	try:															
		number = int(number)
	except Exception as e:
		raise e
	if number < 0 or number >= 1e12:
		raise ValueError("ValueError")
	if number in basic_num:
		return basic_num[number].strip()
	places = {0:"", 1:" thousand", 2:" million", 3:" billion"}
	place = 0
	global and_flag 
	and_flag = True
	msg = str()
	number = str(number)
	right = len(number)-1
	while right>1:
		left = right-2
		if left<0:	
			left=0
		if int(number[left:right+1]) == 0:
			right -= 3
			place += 1
			continue
		flag = False
		if left > 0 and and_flag:
			flag = True
		msg = handle_Three_Digit(int(number[left:right+1]),flag) + places[place] + msg
		right -= 3
		place += 1
	if right>=0:
		if int(number[:right+1]):
			msg = handle_Three_Digit(int(number[:right+1]),False) + places[place] + msg
	return msg.strip()