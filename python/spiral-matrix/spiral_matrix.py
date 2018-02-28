import math


# traveling across the sprial path

def do_Spiral(x, y, num, step, spiral_matrix):
	#assign first value
	spiral_matrix[x][y] = num
	#travel right 
	for _ in range(step):
		y += 1
		num += 1
		spiral_matrix[x][y] = num
	#travel downwords 
	for _ in range(step):
		x += 1
		num += 1
		spiral_matrix[x][y] = num
	#travel left
	for _ in range(step):
		y -= 1
		num += 1
		spiral_matrix[x][y] = num
	#travel upwards
	for _ in range(step-1):
		x -= 1
		num += 1
		spiral_matrix[x][y] = num
	return num+1


def spiral(size):
	spiral_matrix = [0] * size
	for i in xrange(size):
		spiral_matrix[i] = [0] * size
		
	num = 1
	#for each round travel in sprial path 
	for i in xrange(int(math.ceil(size/2.0))):
		num = do_Spiral(i,i,num,size-(i*2)-1,spiral_matrix)
	return spiral_matrix