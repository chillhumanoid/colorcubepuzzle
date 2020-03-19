from cube import cube
'''
1 = green
2 = red
3 = blue
4 = white
'''
def start():
    cube_1 = cube("Cube 1", 1, 2, 2, 4, 3, 4)
    cube_2 = cube("Cube 2", 2, 1, 1, 1, 3, 4)
    cube_3 = cube("Cube 3", 2, 4, 4, 1, 1, 3)
    cube_4 = cube("Cube 4", 2, 3, 2, 1, 4, 3)
    cube_1.print_cube()
    cube_2.print_cube()
    cube_3.print_cube()
    cube_4.print_cube()

start()
