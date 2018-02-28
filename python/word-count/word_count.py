def word_count(phrase):
    import re

    # Regular expression to extract words from phrase
    
    words = re.findall('([a-z]+\'?[a-z])',phrase.lower()) + re.findall('([0-9])+',phrase.lower())
    collection = {}
    for item in words:
    	if item in collection:
    		collection[item] += 1
    	else:
    		collection[item] = 1
    return collection