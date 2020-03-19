
from cube import cube
from itertools import permutations, product
'''
1 = green
2 = red
3 = blue
4 = white
'''
def start():
    cube_1 = [side(1,1),side(2,2),side(2,3),side(4,4),side(3,5),side(4,6)]
    c1_pos = get_possible(cube_1)
    cube_2 = [side(2,1),side(1,2),side(1,3),side(1,4),side(3,5),side(4,6)]
    c2_pos = get_possible(cube_2)
    cube_3 = [side(2,1),side(4,2),side(4,3),side(1,4),side(1,5),side(3,6)]
    c3_pos = get_possible(cube_3)
    cube_4 = [side(2,1),side(3,2),side(2,3),side(1,4),side(4,5),side(3,6)]
    c4_pos = get_possible(cube_4)
    master = list(product(c1_pos, c2_pos, c3_pos, c4_pos))
    final = check_cubes(master, 0)
    final = check_sol(final)
    print_final(final)

def check_sol(master):
    test = []
    c1_sides = []
    c2_sides = []
    c3_sides = []
    c4_sides = []
    for solutions in master:
        x = 1
        for cube in solutions:
            pair = [get_color(cube[0]["color"]), get_color(cube[2]["color"])]
            pair_r = [pair[1], pair[0]]
            if x == 1:
                if pair in c1_sides or pair_r in c1_sides:
                    pass
                else:
                    c1_sides.append(pair)
            elif x == 2:
                if pair in c2_sides or pair_r in c2_sides:
                    pass
                else:
                    c2_sides.append(pair)
            elif x == 3:
                if pair in c3_sides or pair_r in c3_sides:
                    pass
                else:
                    c3_sides.append(pair)
            elif x == 4:
                if pair in c4_sides or pair_r in c4_sides:
                    pass
                else:
                    c4_sides.append(pair)
            x += 1
    c1 = (c1_sides[0][0], c1_sides[1][0], c1_sides[0][1], c1_sides[1][1])
    c2 = (c2_sides[0][0], c2_sides[1][0], c2_sides[0][1], c2_sides[1][1])
    c3 = (c3_sides[0][0], c3_sides[1][0], c3_sides[0][1], c3_sides[1][1])
    c4 = (c4_sides[0][0], c4_sides[1][0], c4_sides[0][1], c4_sides[1][1])
    master = [c1, c2, c3, c4]
    return master

def side(color, side):
    s = {"color": color, "side":side}
    return s

def check_cubes(master, i):
    final = []
    for i in range(4):
        for x in master:
            c1 = x[0][i]
            c2 = x[1][i]
            c3 = x[2][i]
            c4 = x[3][i]
            c1c = c1["color"]
            c2c = c2["color"]
            c3c = c3["color"]
            c4c = c4["color"]
            if not (c1c==c2c or c1c==c3c or c1c==c4c or c2c==c3c or c2c==c4c or c3c==c4c):
                final.append(x)
        master = final.copy()
        final = []
    return master

def get_color(num):
    if num == 1:
        return "g"
    elif num == 2:
        return "r"
    elif num == 3:
        return "b"
    elif num == 4:
        return "w"

def print_final(final):
    side_1 = []
    side_2 = []
    side_3 = []
    side_4 = []
    for x in final:
        side_1.append(x[0])
        side_2.append(x[1])
        side_3.append(x[2])
        side_4.append(x[3])

    c1_s1 = "  {} - 1 ".format(side_1[0])
    c1_s2 = "  {} - 2 ".format(side_2[0])
    c1_s3 = "  {} - 3 ".format(side_3[0])
    c1_s4 = "  {} - 4 ".format(side_4[0])

    c2_s1 = "  {} - 1 ".format(side_1[1])
    c2_s2 = "  {} - 2 ".format(side_2[1])
    c2_s3 = "  {} - 3 ".format(side_3[1])
    c2_s4 = "  {} - 4 ".format(side_4[1])

    c3_s1 = "  {} - 1 ".format(side_1[2])
    c3_s2 = "  {} - 2 ".format(side_2[2])
    c3_s3 = "  {} - 3 ".format(side_3[2])
    c3_s4 = "  {} - 4 ".format(side_4[2])

    c4_s1 = "  {} - 1 ".format(side_1[3])
    c4_s2 = "  {} - 2 ".format(side_2[3])
    c4_s3 = "  {} - 3 ".format(side_3[3])
    c4_s4 = "  {} - 4 ".format(side_4[3])

    print("----------------- -------------------")
    print("|             SOLUTION              |")
    print("---------------------------------- --")
    print("| cube 1 | cube 2 | cube 3 | cube 4 |")
    print("-------------------------------------")
    print("|{}|{}|{}|{}|".format(c1_s1, c2_s1, c3_s1, c4_s1))
    print("|{}|{}|{}|{}|".format(c1_s2, c2_s2, c3_s2, c4_s2))
    print("|{}|{}|{}|{}|".format(c1_s3, c2_s3, c3_s3, c4_s3))
    print("|{}|{}|{}|{}|".format(c1_s4, c2_s4, c3_s4, c4_s4))
    print("-------------------------------------")
    print()
def get_possible(cube):
    option_1 = cube[:-2]
    option_2 = [cube[0], cube[2], cube[4], cube[5]]
    option_3 = [cube[1], cube[3], cube[4], cube[5]]

    list_1 = get_final_pos(option_1, 1, 3, 2, 4)
    list_2 = get_final_pos(option_2, 1, 3, 5, 6)
    list_3 = get_final_pos(option_3, 2, 4, 5, 6)
    master = []
    for a in list_1:
        master.append(a)
    for b in list_2:
        master.append(b)
    for c in list_3:
        master.append(c)
    return master

def get_final_pos(opt, CHECK_1, CHECK_2, CHECK_3, CHECK_4):
    perm = permutations(opt)
    li = list(perm)
    final = li.copy()
    for i in li:
        if i[0]["side"] == CHECK_1 and not i[2]["side"] == CHECK_2:
            final.remove(i)
        elif i[0]["side"] == CHECK_3 and not i[2]["side"] == CHECK_4:
            final.remove(i)
        elif i[0]["side"] == CHECK_2 and not i[2]["side"] == CHECK_1:
            final.remove(i)
        elif i[0]["side"] == CHECK_4 and not i[2]["side"] == CHECK_3:
            final.remove(i)
        elif i[1]["side"] == CHECK_1 and not i[3]["side"] == CHECK_2:
            final.remove(i)
        elif i[1]["side"] == CHECK_2 and not i[3]["side"] == CHECK_1:
            final.remove(i)
        elif i[1]["side"] == CHECK_3 and not i[3]["side"] == CHECK_4:
            final.remove(i)
        elif i[1]["side"] == CHECK_4 and not i[3]["side"] == CHECK_3:
            final.remove(i)
    return final

start()
