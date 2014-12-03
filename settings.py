class Setting:

    def __init__(
        self, window_size=[500, 500],
        camera_size=[1., 1., 1.],
        terrain_size=[1., 1., 1.],
        size_units="world",
        color="abs",
        pos=[0., 0., 0.],
        axis=[0., 0., 1.]
        ):
        self.camera_size = camera_size
        self.terrain_size = terrain_size
        self.size_units = size_units
        self.color = color
        self.pos = pos
        self.axis = axis

    def Get_Window_Size(self):
        return self.window_size

    def Get_Camera_Size(self):
        return self.camera_size

    def Get_Terrain_Size(self):
        return self.terrain_size

    def Get_Size_Units(self):
        return self.size_units

    def Get_Color(self):
        return self.color

    def Get_Pos(self):
        return self.pos

    def Get_Axis(self):
        return self.axis


def init():
    global settings
    settings = Setting()


def Get():
    try:
        return settings  # lint:ok
    except:
        init()
        return settings  # lint:ok
