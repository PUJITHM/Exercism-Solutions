# Globals for the bearings
# Change the values as you see fit
EAST = 'EAST'
NORTH = 'NORTH'
WEST = 'WEST'
SOUTH = 'SOUTH'

rotations = {
				'EAST' : {
							'left' : NORTH,
							'right' : SOUTH
						 },

				'NORTH' : {
							'left' : WEST,
							'right' : EAST
						 },

				'WEST' : {
							'left' : SOUTH,
							'right' : NORTH
						 },

				'SOUTH' : {
							'left' : EAST,
							'right' : WEST
						 }
			}


advances_to = {
				EAST : (1,0),
				NORTH : (0,1),
				WEST : (-1,0),
				SOUTH : (0,-1)
			   }


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.coordinates = (x, y)


    def turn_right(self):
    	self.bearing = rotations[self.bearing]['right']
    
    def turn_left(self):
    	self.bearing = rotations[self.bearing]['left']

    def advance(self):
    	(x, y) = advances_to[self.bearing]
    	self.coordinates = (self.coordinates[0] + x , self.coordinates[1] + y)

    def simulate(self,prog):
    	for action in prog:
    		if action is 'L':
    			self.turn_left()
    		elif action is 'R':
    			self.turn_right()
    		elif action is 'A':
    			self.advance()