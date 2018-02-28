

import math

def do_Spiral(x, y, num, step, spiral_matrix):
	print "data",x, y, num
	#assign first value
	spiral_matrix[x][y] = num
	#travel right 
	for i in range(1,step+1):
		y += 1
		num += 1
		spiral_matrix[x][y] = num
	#travel downwords 
	for i in range(1,step+1):
		x += 1
		num += 1
		spiral_matrix[x][y] = num
	#travel left
	for i in range(1,step+1):
		y -= 1
		num += 1
		spiral_matrix[x][y] = num
	#travel upwards
	for i in range(1,step):
		x -= 1
		num += 1
		spiral_matrix[x][y] = num

	print step, spiral_matrix,"\n\n\n"
	return num+1


def spiral(size):
	spiral_matrix = list()
	for i in xrange(0,size):
		spiral_matrix.append(list())
		for j in xrange(1,size+1):
			spiral_matrix[i].append(0)
	num = 1
	for i in xrange(0,int(math.ceil(size/2.0))):
		num = do_Spiral(i,i,num,size-(i*2)-1,spiral_matrix)
	return spiral_matrix
