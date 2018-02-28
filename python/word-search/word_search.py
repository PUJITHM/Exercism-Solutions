def search_Puzzle(puzzle, word):
	for y in range(len(puzzle)):
		for x in range(len(puzzle[y])):
			if puzzle[y][x] == word[0]:
				#search right
				if word == puzzle[y][x:x+len(word)]:
					return (Point(x,y),Point(x+len(word)-1,y))
				#search left
				elif word == puzzle[y][x-len(word)+1:x+1][::-1]:
					return (Point(x,y),Point(x-len(word)+1,y))
				#seach upwards 
				if y+len(word) <= len(puzzle):
					flag = True
					for i in range(1,len(word)):
						if word[i] != puzzle[y+i][x]:
							flag = False
							break
					if flag:
						return (Point(x,y),Point(x,y+len(word)-1))
				#search downwards 
				if y-len(word) >= 0:
					flag = True
					for i in range(1,len(word)):
						if word[i] != puzzle[y-i][x]:
							flag = False
							break
					if flag:
						return (Point(x,y),Point(x,y-len(word)+1)) 
				#search diagonal upper top right to bottom left
				if len(word)-1 <= x and len(word)-1 <= y:
					flag = True
					for i in range(1,len(word)):
						if word[i] != puzzle[y-i][x-i]:
							flag = False
							break
					if flag:
						return (Point(x,y),Point(x-i,y-i)) 
				#search diagonal upper bottom left to top right
				if len(word)-1 <= len(puzzle)-x and len(word)-1 <= y:
					flag = True
					for i in range(1,len(word)):
						if word[i] != puzzle[y-i][x+i]:
							flag = False
							break
					if flag:
						return (Point(x,y),Point(x+i,y-i)) 
				#search diagonal upper bottom right to top left
				if len(word)-1 <= x and len(word)-1 <= len(puzzle)-y:
					flag = True
					for i in range(1,len(word)):
						if word[i] != puzzle[y+i][x-i]:
							flag = False
							break
					if flag:
						return (Point(x,y),Point(x-i,y+i)) 
				#search diagonal words top left to bottom right
				if len(word)-1 <= len(puzzle)-x and len(word)-1 <= len(puzzle)-y:
					flag = True
					for i in range(1,len(word)):
						if word[i] != puzzle[y+i][x+i]:
							flag = False
							break
					if flag:
						return (Point(x,y),Point(x+i,y+i)) 



class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch(object):
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def search(self, word):
    	if word:        	
        	return search_Puzzle(self.puzzle, word)