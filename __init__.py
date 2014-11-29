# get point generation behavior down first
from visual import *
import random


class Terrain:

    def __init__ (self, width, height, depth, iterations):
        self.width = float(width)
        self.depth = float(depth)
        self.height = float(height)
#        # Array of points, organized by depening rows
        self.points = [
            [[0, self.height, 0], [self.width, self.height, 0]],
            [[0, self.height, self.depth], [self.width, self.height, self.depth]]
            ]

        for i in range(0, iterations):
            self.Rand_Points() # randomize points height
            self.Insert_Rows()
            self.Insert_Midpoints()

    def Get_Width (self):
        return self.width

    def Get_Depth (self):
        return self.depth

    def Get_Height (self):
        return self.height

    def Get_Points (self):
        return self.points

    def Print_Points (self):
        string = "[\n"
        for r in self.Get_Points():
            string += " [\n"
            for p in r:
                string += "  "
                string += str(p) + ",\n"

            string += " ]\n"

        string += "]"
        print(string)

    def Rand_Points (self):  # randomize the height of each point
        for i in range(0, len(self.points)):  # r[] (row) in s.points[][]
            for ie in range(0, len(self.points[i])):  # p[] (point) in r[] (row)
                self.points[i][ie][1] = self.points[i][ie][1] * random.uniform( # randomize height
                    float(len(self.points)) / float(len(self.points) + 1),
                    1.
                    )

    def Insert_Midpoints (self):
        for i in range(0, len(self.points)):  # r[] (row) in s.points[][]
            for ie in range(1, (2 * len(self.points[i])) - 1, 2):
                c = self.points[i][ie]  # local c: current
                n = self.points[i][ie-1]  # local n: next
                a = [  # a[], midpoint coordinates
                    (c[0] + n[0]) / 2,
                    (c[1] + n[1]) / 2,
                    (c[2] + n[2]) / 2
                    ]
                
                self.points[i].insert(ie, a)  # new item

    def Insert_Rows (self):
        for i in range(1, (2 * len(self.points)) - 1, 2):  # r[] (row) in s.points[][]
            self.points.insert(i, [])
            for ie in range(0, len(self.points[i+1])):
                c = self.points[i+1][ie]  # local c: current
                n = self.points[i-1][ie]  # local n: next
                a = [  # a[], midpoint coordinates
                    (c[0] + n[0]) / 2,
                    (c[1] + n[1]) / 2,
                    (c[2] + n[2]) / 2
                    ]
                
                self.points[i].append(a)  # new item

l = 100.
w = 200.
h = 200.

my_terrain = Terrain(w, h, l, 7)

scene = display(
    title = "LANDSCAPES by Random Midpoint Distribution",
    x = 0,
    y = 0,
    width = 700,
    height = 560,
    center = (0.5 * w, 0.75 * h, 0),
    background = (0, 0, 0))

distant_light(
    direction=(0.22, 0.44, 0.88),
    color = (0.8, 0.8, 0.8)
    )
    
draw_points = []
ps = my_terrain.Get_Points()

for i in range(0, len(ps)):
    for ie in range(0, len(ps)):
        p = ps[i][ie]
        dark = (p[1] + h) / (2. * h)  # local dark: darkness
        r = dark * (p[2] + l) / (2. * l)  # local r: red
        g = dark * (p[0] + w) / (2. * w)  # local g: green
        b = dark ** 2  # local b: blue
        x = (2. * p[0]) - w  # local x: x pos
        y = (2. * p[1]) - (2. * h) - (0.75 * p[2])  # local y: y pos
        z = (2. * p[2]) - l  # local z: z pos
        draw_points.append(
          points(
            pos = (p[0], p[1], p[2]),
            size_units = "world",
            color = (r, g, b)
            )
          )
        
##            pyramid(
##                pos = (x, y, z),
##                size_units = "world",
##                size = (
##                    1,
##                    2 * (points[i][ie+1][0] - points[i][ie-1][0]),
##                    2 * (points[i+1][ie][2] - points[i-1][ie][2])
##                    ),
##                color = (r, g, b),
##                axis = (0, 1, 0)
##                )
##            )
            

##points = my_terrain.Get_Points()
##pyramids = []
##
##for i in range(1, len(points), 2): # z axis
##    for ie in range(1, len(points[i]), 2): # x axis
##        pos = points[i][ie]
##        print(pos)
##        size = (10, 10, 10)
##        color = pos
##        print(color)
##        pyramids.append([pos, size, color])
##        
##                
##for shape in pyramids:
##    pyramid(
##        pos = shape[0],
##        axis = (0, 1, 0),
##        size_units = "world",
##        size = shape[1],
##        color = (1, 1, 1))
        
