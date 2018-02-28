from robot_simulator import Robot, NORTH, EAST, SOUTH, WEST

robot = Robot(EAST, 2, -7)
robot.simulate("RRAAAAALA")
print (robot.coordinates)
print (robot.bearing)