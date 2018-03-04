def flatten(iterable):
    flatten_array = list()
    if iterable is None:
    	return []
    try:
    	for array in iterable:
    		flatten_array += flatten(array)
    	return flatten_array
    except Exception as e:
    	return [iterable]