import random


class Terrain:

    def __init__(self, size=[1., 1., 1.], iterations=0):
        self.size = size  # array = [floats], len() == 3
#         # Array of vertices, organized by depening rows
        self.vertices = [
            [
                [0, size[1], 0],
                [size[0], size[1], 0]
            ],
            [
                [0, size[1], size[2]],
                [size[0], size[1], size[2]]
            ]
        ]
        self.Itterate(iterations)

    def Itterate(self, iterations=1):
        for i in range(0, iterations):
            self.Rand_Vertices()  # randomize vertices height
            self.Insert_Rows()
            self.Insert_Midpoints()

    def Get_Size(self):
        return self.size

    def Get_Vertices(self):
        return self.vertices

    def Print_Vertices(self):
        string = "[\n"
        for r in self.vertices:
            string += " [\n"
            for p in r:
                string += "  ["
                string += str(p[0])
                for i in range(1, 3):
                    string += ", "
                    string += str(p[i])

                string += "]\n"

            string += " ]\n"

        string += "]"
        print(string)

    def Rand_Vertices(self):  # randomize the height of each point
#         # r[] (row) in s.vertices[][]
        for i in range(0, len(self.vertices)):
#             # p[] (point) in r[] (row)
            for ie in range(0, len(self.vertices[i])):
#                 # randomize height
                vertex = self.vertices[i][ie][1]
                self.vertices[i][ie][1] = vertex * random.uniform(
                    float(len(self.vertices)) / float(len(self.vertices) + 1),
                    1.
                    )

    def Insert_Midpoints(self):
        for i in range(0, len(self.vertices)):  # r[] (row) in s.vertices[][]
            for ie in range(1, (2 * len(self.vertices[i])) - 1, 2):
                c = self.vertices[i][ie]  # local c: current
                n = self.vertices[i][ie - 1]  # local n: next
                a = [  # a[], midpoint coordinates
                    (c[0] + n[0]) / 2,
                    (c[1] + n[1]) / 2,
                    (c[2] + n[2]) / 2
                    ]

                self.vertices[i].insert(ie, a)  # new item

    def Insert_Rows(self):
#         # r[] (row) in s.vertices[][]
        for i in range(1, (2 * len(self.vertices)) - 1, 2):
            self.vertices.insert(i, [])
            for ie in range(0, len(self.vertices[i + 1])):
                c = self.vertices[i + 1][ie]  # local c: current
                n = self.vertices[i - 1][ie]  # local n: next
                a = [  # a[], midpoint coordinates
                    (c[0] + n[0]) / 2,
                    (c[1] + n[1]) / 2,
                    (c[2] + n[2]) / 2
                    ]

                self.vertices[i].append(a)  # new item
