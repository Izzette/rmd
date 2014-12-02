import visual


class Points:

    def __init__ (self):
        self.points = []
        self.frame = visual.frame()

    def Del_Points (self):
        while 0 < len(self.points):
            self.points[0].visible = False
            self.points.pop(0)

    def Add_Points (self, terrain, color="abs"):
        vertices = terrain.Get_Vertices()
        length, width, height = terrain.Get_Size()
        for i in range(0, len(vertices)):
            for ie in range(0, len(vertices)):
                vertex = vertices[i][ie]
                  # default colors
                red = vertex[0] / 1
                green = vertex[1] / height
                blue = vertex[2] / length
                if "mid" == color:  # mid to full colors
                    dark = (vertex[1] + height) / (2. * height)  # local dark: darkness
                    red = dark * (vertex[2] + length) / (2. * length)  # red: color
                    green = dark * (vertex[0] + width) / (2. * width)  # green: color
                    blue = dark ** 2  # blue: color
                    
                x = vertex[0]  # local x: pos
                y = vertex[1]  # local y: pos
                z = vertex[2]  # local z: pos
                self.points.append(
                  visual.points(  # add point to vPython
                    pos = (vertex[0], vertex[1], vertex[2]),
                    size_units = "world",
                    frame = self.frame,
                    color = (red, green, blue)
                    )
                  )

    def Set_Points (self, terrain, color=""):
        self.Del_Points()
        self.Add_Points(terrain, color)
        
        
