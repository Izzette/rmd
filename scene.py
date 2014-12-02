import visual


class Scene:
    
    def __init__ (self):
        self.scene = visual.display(
            title = "LANDSCAPES by Random Midpoint Distribution",
            x = 0,
            y = 0,
            width = 700,
            height = 560,
            axis = (0., 0., 1.),
            background = (0., 0., 0.)
            )

    def Get_Scene(self):
        return self.scene

    def Set_Camera(self, pos="world", vertices=[[[]]]):
        if "world" == pos:
            self.scene.autoscale = True
        elif "center" == pos:
            row = vertices[len(vertices) / 2]
            vertex = row[len(row) / 2]
            self.scene.autoscale = False
            self.scene.center = (
                vertex[0] / 2.,
                vertex[1] + 10.,
                vertex[2] / 2.
                )
            self.scene.range = (vertex[0] + vertex[2]) / 4.

    def Set_Axis(self, axis=(0., 0., 1.)):
        self.scene.axis = axis

    def Exit(self):
        self.scene.visible = False
        del self.scene
