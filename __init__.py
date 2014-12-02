import scene
import scape
import points
import time

terrain = scape.Terrain((100., 100., 100.), 8)

scene = scene.Scene()
scene.Set_Camera("center", terrain.Get_Vertices())
scene.Set_Axis((0., 0., 0.))
points = points.Points()

points.Add_Points(terrain, "mid")
