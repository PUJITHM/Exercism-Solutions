import re
def calculate(question):
    res=0
    opr_count=0
    operations=['plus','minus','multiplied by','divided by']
    num=re.findall('[-+]?\d+',question)
    words=re.findall('\w+',question)
    # for i=0 to operations.count-1
    #     if question.contains
    #op=findall(operations,question)
    for j in operations:
        if j in question:
            opr_count+=1
    if len(num)==0:
        raise ValueError ("Non math question")
    elif len(num)==3 and opr_count<2:
        raise ValueError ("missing_operation")
    elif len(num)==2 and opr_count>1:
        raise ValueError ("missing_number")    
    elif len(num)==3 and len(words)<7:
    	raise ValueError ("error")
    for i in words:
    	if i==operations[0]:
    		if res==0:
    			res = int(num[0]) + int(num[1])
    		else:
    			res += int(num[2])
    	elif i==operations[1]:
    		if res==0:
    			res = int(num[0]) - int(num[1])
    		else:
    			res -= int(num[2])
    	elif i==operations[2]:
    		if res==0:
    			res = int(num[0]) * int(num[1])
    		else:
    			res *= int(num[2])
    	elif i==operations[3]:
    		if res==0:
    			res = int(num[0]) / int(num[1])
    		else:
    			res /= int(num[2])
    	elif i == 'cubed' :
    	 	raise ValueError ("Unkown operation")
    return (res)


q="What is -12 divided by 2 divided by -3?"
calculate(q)