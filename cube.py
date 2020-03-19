class cube():
    def __init__(self, name, s1, s2, s3, s4, s5, s6):
        self.name = name
        self.side_1 = self.get_color(s1)
        self.side_2 = self.get_color(s2)
        self.side_3 = self.get_color(s3)
        self.side_4 = self.get_color(s4)
        self.side_5 = self.get_color(s5)
        self.side_6 = self.get_color(s6)

    def get_color(self, color):
        if color == 1:
            return "green"
        elif color == 2:
            return "red"
        elif color == 3:
            return "blue"
        elif color == 4:
            return "white"
    def print_cube(self):
         print(self.name)
         print("side 1 {}".format(self.side_1))
         print("side 2 {}".format(self.side_2))
         print("side 3 {}".format(self.side_3))
         print("side 4 {}".format(self.side_4))
         print("side 5 {}".format(self.side_5))
         print("side 6 {}".format(self.side_6))
         print()
