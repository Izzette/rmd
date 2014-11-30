import random

class Terrain:

    def __init__ (self, size, iterations=0):
        self.size = size
        width, depth, height = size
#        # Array of vertices, organized by depening rows
        self.vertices = [
            [
                [0, height, 0],
                [width, height, 0]
            ],
            [
                [0, height, depth],
                [width, height, depth]
            ]
        ]

        self.Itterate(iterations)

    def Itterate (self, iterations=1):
        for i in range(0, iterations):
            self.Rand_Vertices() # randomize vertices height
            self.Insert_Rows()
            self.Insert_Midpoints()

    def Get_Size (self):
        return self.size

    def Get_Vertices (self):
        return self.vertices

    def Print_Vertices (self):
        string = "[\n"
        for r in self.vertices:
            string += " [\n"
            for p in r:
                string += "  "
                string += str(p) + ",\n"

            string += " ]\n"

        string += "]"
        print(string)

    def Rand_Vertices (self):  # randomize the height of each point
        for i in range(0, len(self.vertices)):  # r[] (row) in s.vertices[][]
            for ie in range(0, len(self.vertices[i])):  # p[] (point) in r[] (row)
                self.vertices[i][ie][1] = self.vertices[i][ie][1] * random.uniform( # randomize height
                    float(len(self.vertices)) / float(len(self.vertices) + 1),
                    1.
                    )

    def Insert_Midpoints (self):
        for i in range(0, len(self.vertices)):  # r[] (row) in s.vertices[][]
            for ie in range(1, (2 * len(self.vertices[i])) - 1, 2):
                c = self.vertices[i][ie]  # local c: current
                n = self.vertices[i][ie-1]  # local n: next
                a = [  # a[], midpoint coordinates
                    (c[0] + n[0]) / 2,
                    (c[1] + n[1]) / 2,
                    (c[2] + n[2]) / 2
                    ]
                
                self.vertices[i].insert(ie, a)  # new item

    def Insert_Rows (self):
        for i in range(1, (2 * len(self.vertices)) - 1, 2):  # r[] (row) in s.vertices[][]
            self.vertices.insert(i, [])
            for ie in range(0, len(self.vertices[i+1])):
                c = self.vertices[i+1][ie]  # local c: current
                n = self.vertices[i-1][ie]  # local n: next
                a = [  # a[], midpoint coordinates
                    (c[0] + n[0]) / 2,
                    (c[1] + n[1]) / 2,
                    (c[2] + n[2]) / 2
                    ]
                
                self.vertices[i].append(a)  # new item
