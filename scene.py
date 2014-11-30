import visual

def Scene():
    scene = visual.display(
        title = "LANDSCAPES by Random Midpoint Distribution",
        x = 0,
        y = 0,
        width = 700,
        height = 560,
        axis = (0., 0., 1.),
        background = (0., 0., 0.)
        )

def Get_Scene():
    return scene

def Set_Camera(pos="world", vertices=[[[]]]):
    if "world" == pos:
        scene.autoscale = True
    elif "center" == pos:
        row = vertices[len(vertices) / 2]
        vertex = row[len(row) / 2]
        
        scene.center = (
            vertex[0] / 2.,
            vertex[1] + 10.,
            vertex[2] / 2.
            )

def Set_Axis(axis=(0., 0., 1.)):
    scene.axis = axis

def Exit():
    del scene
