def is_pangram(sentence):
    try:
    	pangram = sorted(list(set(sentence.lower())))
    	return 'z' == pangram[pangram.index('a')+25] and pangram.count('z') == 1
    except Exception as e:	
    	return False
