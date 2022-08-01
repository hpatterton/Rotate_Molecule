# =========================================================================================================
# Implementation of a rudimentary molecular viewer
# The molecule is drawn as simple line drawing (no anti-aliasing)
# The PDB format filename must be hardcoded in this file
# The left, right, up and down arrow keys and the Z and X key rotate the molecule on the X, Y and Z axes
# The larger than and smaller than keys zoom the image
# No exception handling done to keep it simple!
# =========================================================================================================

import pygame
import numpy
from class_PDB import PDB

def rotate_array(vector_array, angle, axis):
	sin_angle = numpy.sin(angle*2*numpy.pi/360)
	cos_angle = numpy.cos(angle*2*numpy.pi/360)
	# only calculate the rotation matrix that you need
	if axis == 0:
		X_matrix = numpy.array([[1,0,0], [0,cos_angle, sin_angle],[0, -sin_angle,cos_angle]])
		new_vector_array = vector_array.dot(X_matrix)
	elif axis == 1:
		Y_matrix = numpy.array([[cos_angle,0,-sin_angle],[0,1,0],[sin_angle,0,cos_angle]])
		new_vector_array = vector_array.dot(Y_matrix)
	elif axis == 2:
		Z_matrix = numpy.array([[cos_angle,sin_angle,0],[-sin_angle,cos_angle,0],[0,0,1]])
		new_vector_array = vector_array.dot(Z_matrix)
	else:
		new_vector_array = vector_array
	return(new_vector_array)

def draw_molecule(coordinates, connections, screen, scale, offset, forecolour):
	number_of_atoms = len(coordinates)
	# draw the connections
	for i in range(len(connections)):
		start = connections[i][0]
		for j in range(1,len(connections[i])):
			end = connections[i][j]
			pygame.draw.line(screen, forecolour, (scale*coordinates[start][0]+offset[0],scale*coordinates[start][1]+offset[1]),(scale*coordinates[end][0]+offset[0],scale*coordinates[end][1]+offset[1]),1)

if __name__ == "__main__":

	pygame.init()
	screen_width = 900
	screen_height = 600
	screen = pygame.display.set_mode((screen_width, screen_height))
	# read molecule coordinates and connectivity lists
    # chabe the path to reflect the location of your PDB file
	path = 'C:\\Users\\hpatterton\\Documents\\CBCB\\Degrees\\BSc Hons\\2021\\Docking\\TSA_2_1.pdb'
	pdb_file = PDB(path)
	pdb_file.ReadFile(path)
	coordinates = pdb_file.GetCoordinates()
	#print(coordinates)
	coordinates = pdb_file.CenterMolecule(coordinates)
	connect = pdb_file.GetConnections()
	#print(connect)

	offset = (screen_width/2,screen_height/2,0)
	scale = 40
	new_scale = scale
	black = (0,0,0)
	white = (255,255,255)
	play_on = True
	pygame.key.set_repeat(10,10)
	draw_molecule(coordinates,connect, screen,scale,offset,white)
	pygame.display.update()

	while play_on:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				play_on = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					new_coordinates = rotate_array(coordinates, -1, 1)
				elif event.key == pygame.K_RIGHT:
					new_coordinates = rotate_array(coordinates, 1, 1)
				elif event.key == pygame.K_UP:
					new_coordinates = rotate_array(coordinates, 1, 0)
				elif event.key == pygame.K_DOWN:
					new_coordinates = rotate_array(coordinates, -1, 0)
				elif event.key == pygame.K_z:
					new_coordinates = rotate_array(coordinates, -1, 2)
				elif event.key == pygame.K_x:
					new_coordinates = rotate_array(coordinates, 1, 2)
				elif event.key == pygame.K_COMMA:
					new_scale = scale - 1
				elif event.key == pygame.K_PERIOD:
					new_scale = scale + 1
			else:
				new_coordinates = coordinates
		#perspective_cube = adjust_pespective(cube,distance_to_screen,offset[2])
		draw_molecule(coordinates,connect, screen,scale,offset,black)
		#perspective_new_cube = adjust_pespective(new_cube, distance_to_screen, offset[2])
		draw_molecule(new_coordinates,connect,screen,new_scale,offset,white)
		coordinates = new_coordinates
		scale = new_scale
		pygame.display.update()
	pygame.quit()
