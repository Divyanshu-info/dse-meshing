import pyvista as pv
mesh = pv.read(
    "Cup/Cup.ply")
mesh.plot()
