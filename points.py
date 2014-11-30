import visual

def Set_Points(terrain, color="abs"):
    points = []
    frame = visual.frame()
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
                
            x = (2. * vertex[0]) - width  # local x: pos
            y = (2. * vertex[1]) - (2. * height) - (0.75 * vertex[2])  # local y: pos
            z = (2. * vertex[2]) - length  # local z: pos
            points.append(
              visual.points(  # add point to vPython
                pos = (vertex[0], vertex[1], vertex[2]),
                size_units = "world",
                frame = frame,
                color = (red, green, blue)
                )
              )
        
