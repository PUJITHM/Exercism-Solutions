def reverse(string):
	r_string = str()
	for i in xrange(1, len(string)+1):
		r_string = r_string + string[-i]
	return r_string	
