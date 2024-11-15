import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from skimage import measure
from stl import mesh

def triangulate_sdf(v, resolution=30):
    # sample the SDF at certain points
    l = w = h = resolution
    arr = np.zeros((l + 1, w + 1, h + 1))

    for x in range(l + 1):
        for y in range(w + 1):
            for z in range(h + 1):
                arr[x][y][z] = v.f((x - l//2) / l * 2, (y - w//2) / w * 2, (z - h//2) / h * 2)


    # Use marching cubes to obtain the surface mesh of the SDF
    verts, faces, normals, values = measure.marching_cubes(arr, 0)
    return verts, faces

def stlify_mesh(verts, faces, fname):
    m2 = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            m2.vectors[i][j] = verts[f[j],:]
    m2.save(fname)

def plot_sdf(verts, faces):
    # Display resulting triangular mesh using Matplotlib. This can also be done
    # with mayavi (see skimage.measure.marching_cubes docstring).
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Fancy indexing: `verts[faces]` to generate a collection of triangles
    mesh = Poly3DCollection(verts[faces])
    mesh.set_edgecolor('k')
    ax.add_collection3d(mesh)

    r = max([max(v) for v in verts])
    ax.set_xlim(0, r)
    ax.set_ylim(0, r)
    ax.set_zlim(0, r)

    plt.tight_layout()
    plt.show()

