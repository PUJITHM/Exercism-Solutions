def is_armstrong(number):
    return number == reduce(lambda x, y: y ** len(str(number)) +  x, [0] + map(int,list(str(number)))):
    	