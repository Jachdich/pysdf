
from math import *
import pysdf

class V1:
    def r(z):
        l = 0.3
        n = 0.8
        return -l * (z+1)**2 + 1 + n*z

    def t(z):
        return -0.3*z**2 + 1

    def f(x, y, z):
        return max(x**2 + y**2 - V1.r(z) - 0.1 * cos(12 * atan2(y,x) + 15*z*V1.t(z)), V1.top(x,y,z))

    def top(x, y, z):
        if z > 0.99 or z < -0.99:
            return 10000000
            # return max(x**2 + y**2 - V1.r(z) - 0.1 * cos(12 * atan2(y,x) + 15*z*V1.t(z)), 0)
        return -10000000

class V2:
    # radius depends on z
    def r(z):
        l = 0.4
        n = 0.25
        return -l*(z-n)**2+0.9

    # twist factor depends on z
    def t(z):
        return -0.3*z**2 + 1

    # f(x, y, z) defines the signed distance field
    def f(x, y, z):
        return x**2 + y**2 - V2.r(z) * (1 + 0.1 * cos(12 * atan2(y,x) + 15*z*V2.t(z)))

verts, faces = pysdf.triangulate_sdf(V1, resolution=100)
pysdf.stlify_mesh(verts, faces, "mysurface.stl")
pysdf.plot_sdf(verts, faces)
