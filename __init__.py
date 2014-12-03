import scene
import scape
import settings
import points
import time

settings.init()
scene.init()
terrain = scape.Terrain([100., 100., 100.], 8)
points = points.Vertices_To_Points(terrain.Get_Vertices())
scene.Draw(points)