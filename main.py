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
    print_final(final)

def side(color, side):
    s = {"color": color, "side":side}
    return s

def check_cubes(master, i):
    final = []
    for x in master:
        c1 = x[0][i]
        c2 = x[1][i]
        c3 = x[2][i]
        c4 = x[3][i]
        c1_c = c1["color"]
        c2_c = c2["color"]
        c3_c = c3["color"]
        c4_c = c4["color"]
        if c1_c == c2_c or c1_c == c3_c or c1_c == c4_c:
            pass
        elif c2_c == c3_c or c2_c == c4_c:
            pass
        elif c3_c == c4_c:
            pass
        else:
            final.append(x)
    if not i == 3:
        i += 1
        return check_cubes(final, i)
    else:
        return final

def get_color(num):
    if num == 1:
        return "g"
    elif num == 2:
        return "r"
    elif num == 3:
        return "b"
    elif num == 4:
        return "w"

def get_side(num):
    if num == 1:
        return "top"
    elif num == 2:
        return "back"
    elif num == 3:
        return "bottom"
    elif num == 4:
        return "front"
    elif num == 5 or num == 6:
        return "side"

def print_cube(cube):
    for x in cube.values():
        print(x)
def print_final(final):
    y = 1
    for x in final:
        c1 = x[0]
        c2 = x[1]
        c3 = x[2]
        c4 = x[3]
        c1_to = c1[0]
        c1_ba = c1[1]
        c1_bo = c1[2]
        c1_fr = c1[3]
        c1_c_to = get_color(c1_to["color"])
        c1_c_ba = get_color(c1_ba["color"])
        c1_c_bo = get_color(c1_bo["color"])
        c1_c_fr = get_color(c1_fr["color"])

        c2_to = c2[0]
        c2_ba = c2[1]
        c2_bo = c2[2]
        c2_fr = c2[3]
        c2_c_to = get_color(c2_to["color"])
        c2_c_ba = get_color(c2_ba["color"])
        c2_c_bo = get_color(c2_bo["color"])
        c2_c_fr = get_color(c2_fr["color"])

        c3_to = c3[0]
        c3_ba = c3[1]
        c3_bo = c3[2]
        c3_fr = c3[3]
        c3_c_to = get_color(c3_to["color"])
        c3_c_ba = get_color(c3_ba["color"])
        c3_c_bo = get_color(c3_bo["color"])
        c3_c_fr = get_color(c3_fr["color"])

        c4_to = c4[0]
        c4_ba = c4[1]
        c4_bo = c4[2]
        c4_fr = c4[3]
        c4_c_to = get_color(c4_to["color"])
        c4_c_ba = get_color(c4_ba["color"])
        c4_c_bo = get_color(c4_bo["color"])
        c4_c_fr = get_color(c4_fr["color"])

        c1_s_to = " {}-top    ".format(c1_c_to)
        c1_s_ba = " {}-back   ".format(c1_c_ba)
        c1_s_bo = " {}-bottom ".format(c1_c_bo)
        c1_s_fr = " {}-front  ".format(c1_c_fr)

        c2_s_to = " {}-top    ".format(c2_c_to)
        c2_s_ba = " {}-back   ".format(c2_c_ba)
        c2_s_bo = " {}-bottom ".format(c2_c_bo)
        c2_s_fr = " {}-front  ".format(c2_c_fr)

        c3_s_to = " {}-top    ".format(c3_c_to)
        c3_s_ba = " {}-back   ".format(c3_c_ba)
        c3_s_bo = " {}-bottom ".format(c3_c_bo)
        c3_s_fr = " {}-front  ".format(c3_c_fr)

        c4_s_to = " {}-top    ".format(c4_c_to)
        c4_s_ba = " {}-back   ".format(c4_c_ba)
        c4_s_bo = " {}-bottom ".format(c4_c_bo)
        c4_s_fr = " {}-front  ".format(c4_c_fr)

        print("---------------------------------------------")
        print("|                SOLUTION {}                 |".format(y))
        print("---------------------------------------------")
        print("|  CUBE 1  |  CUBE 2  |  CUBE 3  |  CUBE 4  |")
        print("---------------------------------------------")
        print("|{}|{}|{}|{}|".format(c1_s_to, c2_s_to, c3_s_to, c4_s_to))
        print("|{}|{}|{}|{}|".format(c1_s_ba, c2_s_ba, c3_s_ba, c4_s_ba))
        print("|{}|{}|{}|{}|".format(c1_s_bo, c2_s_bo, c3_s_bo, c4_s_bo))
        print("|{}|{}|{}|{}|".format(c1_s_fr, c2_s_fr, c3_s_fr, c4_s_fr))
        print("----------------------------------------------")
        print()
        y += 1

def get_possible(cube):
    option_1 = cube[:-2]
    option_2 = [cube[0], cube[2], cube[4], cube[5]]
    option_3 = [cube[1], cube[3], cube[4], cube[5]]
    perm1 = permutations(option_1)
    perm2 = permutations(option_2)
    perm3 = permutations(option_3)
    l1 = list(perm1)
    l1_final = l1.copy()
    l2 = list(perm2)
    l2_final = l2.copy()
    l3 = list(perm3)
    l3_final = l3.copy()
    master_list = []
    for i in l1:
        if i[0]["side"] == 1 and not i[2]["side"] == 3:
            l1_final.remove(i)
        elif i[0]["side"] == 2 and not i[2]["side"] == 4:
            l1_final.remove(i)
        elif i[0]["side"] == 3 and not i[2]["side"] == 1:
            l1_final.remove(i)
        elif i[0]["side"] == 4 and not i[2]["side"] == 2:
            l1_final.remove(i)
        elif i[1]["side"] == 1 and not i[3]["side"] == 3:
            l1_final.remove(i)
        elif i[1]["side"] == 3 and not i[3]["side"] == 1:
            l1_final.remove(i)
        elif i[1]["side"] == 2 and not i[3]["side"] == 4:
            l1_final.remove(i)
        elif i[1]["side"] == 4 and not i[3]["side"] == 2:
            l1_final.remove(i)
    for i in l2:
        if i[0]["side"] == 1 and not i[2]["side"] == 3:
            l2_final.remove(i)
        elif i[0]["side"] == 3 and not i[2]["side"] == 1:
            l2_final.remove(i)
        elif i[0]["side"] == 5 and not i[2]["side"] == 6:
            l2_final.remove(i)
        elif i[0]["side"] == 6 and not i[2]["side"] == 5:
            l2_final.remove(i)
        elif i[1]["side"] == 1 and not i[3]["side"] == 3:
            l2_final.remove(i)
        elif i[1]["side"] == 3 and not i[3]["side"] == 1:
            l2_final.remove(i)
        elif i[1]["side"] == 5 and not i[3]["side"] == 6:
            l2_final.remove(i)
        elif i[1]["side"] == 6 and not i[3]["side"] == 5:
            l2_final.remove(i)
    for i in l3:
        if i[0]["side"] == 2 and not i[2]["side"] == 4:
            l3_final.remove(i)
        elif i[0]["side"] == 4 and not i[2]["side"] == 2:
            l3_final.remove(i)
        elif i[0]["side"] == 5 and not i[2]["side"] == 6:
            l3_final.remove(i)
        elif i[0]["side"] == 6 and not i[2]["side"] == 5:
            l3_final.remove(i)
        elif i[1]["side"] == 2 and not i[3]["side"] == 4:
            l3_final.remove(i)
        elif i[1]["side"] == 4 and not i[3]["side"] == 2:
            l3_final.remove(i)
        elif i[1]["side"] == 5 and not i[3]["side"] == 6:
            l3_final.remove(i)
        elif i[1]["side"] == 6 and not i[3]["side"] == 5:
            l3_final.remove(i)
    for item in l1_final:
        master_list.append(item)
    for item in l2_final:
        master_list.append(item)
    for item in l3_final:
        master_list.append(item)
    return master_list

start()
