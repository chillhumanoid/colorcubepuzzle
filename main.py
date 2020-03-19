from itertools import permutations, product

'''
1 - Green
2 - Red
3 - Blue
4 - White
'''
def start():
    cube1_possible = create_cube(1, 2, 2, 4, 3, 4)
    cube2_possible = create_cube(2, 1, 1, 1, 3, 4)
    cube3_possible = create_cube(2, 4, 4, 1, 1, 3)
    cube4_possible = create_cube(2, 3, 2, 1, 4, 3)

    master = list(product(cube1_possible, cube2_possible, cube3_possible, cube4_possible))
    master = check_cubes(master, 0)
    master = check_solution(master)
    print_final(master)

def create_cube(side1_color, side2_color, side3_color, side4_color, side5_color, side6_color):
    side1 = side(side1_color, 1)
    side2 = side(side2_color, 2)
    side3 = side(side3_color, 3)
    side4 = side(side4_color, 4)
    side5 = side(side5_color, 5)
    side6 = side(side6_color, 6)

    cube = [side1, side2, side3, side4, side5, side6]
    possible = get_possible_solutions(cube)

    return possible

def side(color, side):
    return {"color":color,"side":side}

def get_possible_solutions(cube):
    option1 = cube[:-2]                             #option 1 does not include sides 5 and 6 in the array
    option2 = [cube[0], cube[2], cube[4], cube[5]]  #option 2 does not include sides 2 and 4 in the array
    option3 = [cube[1], cube[3], cube[4], cube[5]]  #option 3 does not include sides 1 and 3 in the array

    list1 = get_final_possible(option1, 1, 3, 2, 4) #checks argument 2 and 3 and argument 4 and 5 against each other
    list2 = get_final_possible(option2, 1, 3, 5, 6) #checks argument 2 and 3 and argument 4 and 5 against each other
    list3 = get_final_possible(option3, 2, 4, 5, 6) #checks argument 2 and 3 and argument 4 and 5 against each other

    master = []
    for possibility in list1:
        master.append(possibility)
    for possibility in list2:
        master.append(possibility)
    for possibility in list3:
        master.append(possibility)

    return master

def get_final_possible(option, check1, check2, check3, check4):
    permutations_ = list(permutations(option))
    master = permutations_.copy()
    for possibility in permutations_:
        side1, side2, side3, side4 = possibility[0:4]
        if side1["side"] == check1 and not side3["side"] == check2:
            master.remove(possibility)
        elif side1["side"] == check2 and not side3["side"] == check1:
            master.remove(possibility)
        elif side1["side"] == check3 and not side3["side"] == check4:
            master.remove(possibility)
        elif side1["side"] == check4 and not side3["side"] == check3:
            master.remove(possibility)
        elif side2["side"] == check1 and not side4["side"] == check2:
            master.remove(possibility)
        elif side2["side"] == check2 and not side4["side"] == check1:
            master.remove(possibility)
        elif side2["side"] == check3 and not side4["side"] == check4:
            master.remove(possibility)
        elif side2["side"] == check4 and not side4["side"] == check3:
            master.remove(possibility)

    return master

def check_cubes(master, i):
    temporary = []
    for i in range(4):
        for possibility in master:
            cube1 = possibility[0][i]
            cube2 = possibility[1][i]
            cube3 = possibility[2][i]
            cube4 = possibility[3][i]

            cube1_color = cube1["color"]
            cube2_color = cube2["color"]
            cube3_color = cube3["color"]
            cube4_color = cube4["color"]

            if cube1_color == cube2_color or cube1_color == cube3_color or cube1_color == cube4_color:
                pass
            elif cube2_color == cube3_color or cube2_color == cube4_color:
                pass
            elif cube3_color == cube4_color:
                pass
            else:
                temporary.append(possibility)
        master = temporary.copy()
        temporary = []
    return master

def check_solution(master):
    cube1_sides = []
    cube2_sides = []
    cube3_sides = []
    cube4_sides = []
    for solutions in master:
        cube_number = 1
        for cube in solutions:
            pair = [get_color(cube[0]["color"]), get_color(cube[2]["color"])]
            pair_reversed = [pair[1], pair[0]]
            if cube_number == 1:
                cube1_sides = check_pairs(pair, pair_reversed, cube1_sides)
            elif cube_number == 2:
                cube2_sides = check_pairs(pair, pair_reversed, cube2_sides)
            elif cube_number == 3:
                cube3_sides = check_pairs(pair, pair_reversed, cube3_sides)
            elif cube_number == 4:
                cube4_sides = check_pairs(pair, pair_reversed, cube4_sides)
            cube_number += 1

    cube1 = get_cube_from_sides(cube1_sides)
    cube2 = get_cube_from_sides(cube2_sides)
    cube3 = get_cube_from_sides(cube3_sides)
    cube4 = get_cube_from_sides(cube4_sides)
    return [cube1, cube2, cube3, cube4]

def get_color(color_number):
    if   color_number == 1: return "g"
    elif color_number == 2: return "r"
    elif color_number == 3: return "b"
    elif color_number == 4: return "w"

def check_pairs(pair, pair_reversed, cube_sides):
    if not (pair in cube_sides or pair_reversed in cube_sides):
        cube_sides.append(pair)
    return cube_sides

def get_cube_from_sides(cube_sides):
    return (cube_sides[0][0], cube_sides[1][0], cube_sides[0][1], cube_sides[1][1])

def print_final(final):
    side_1 = []
    side_2 = []
    side_3 = []
    side_4 = []
    for cube in final:
        side_1.append(cube[0])
        side_2.append(cube[1])
        side_3.append(cube[2])
        side_4.append(cube[3])

    cube1_side1 = "  {} - 1 ".format(side_1[0])
    cube1_side2 = "  {} - 2 ".format(side_2[0])
    cube1_side3 = "  {} - 3 ".format(side_3[0])
    cube1_side4 = "  {} - 4 ".format(side_4[0])

    cube2_side1 = "  {} - 1 ".format(side_1[1])
    cube2_side2 = "  {} - 2 ".format(side_2[1])
    cube2_side3 = "  {} - 3 ".format(side_3[1])
    cube2_side4 = "  {} - 4 ".format(side_4[1])

    cube3_side1 = "  {} - 1 ".format(side_1[2])
    cube3_side2 = "  {} - 2 ".format(side_2[2])
    cube3_side3 = "  {} - 3 ".format(side_3[2])
    cube3_side4 = "  {} - 4 ".format(side_4[2])

    cube4_side1 = "  {} - 1 ".format(side_1[3])
    cube4_side2 = "  {} - 2 ".format(side_2[3])
    cube4_side3 = "  {} - 3 ".format(side_3[3])
    cube4_side4 = "  {} - 4 ".format(side_4[3])

    print("----------------- -------------------")
    print("|             SOLUTION              |")
    print("---------------------------------- --")
    print("| cube 1 | cube 2 | cube 3 | cube 4 |")
    print("-------------------------------------")
    print("|{}|{}|{}|{}|".format(cube1_side1, cube2_side1, cube3_side1, cube4_side1))
    print("|{}|{}|{}|{}|".format(cube1_side2, cube2_side2, cube3_side2, cube4_side2))
    print("|{}|{}|{}|{}|".format(cube1_side3, cube2_side3, cube3_side3, cube4_side3))
    print("|{}|{}|{}|{}|".format(cube1_side4, cube2_side4, cube3_side4, cube4_side4))
    print("-------------------------------------")
    print()

start()
