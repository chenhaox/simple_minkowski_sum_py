import itertools
from scipy.spatial import ConvexHull
import numpy as np
import functools
def bi_minkowski_sum(a, b):
    """
    calculate the minkowski sum of a and b
    :param a: list of points 2D/3D  [[vertex1,vertex2,vertex3],[...],...]
    :param b: list of points 2D/3D  [[vertex1,vertex2,vertex3],[...],...]
    :return: minkowski sum of two list of points
    """
    result = list(itertools.product(a, b))
    final = [(np.array(i[0])+np.array(i[1])).tolist() for i in result]
    finalnp = np.array(final)
    final = finalnp[ConvexHull(finalnp,qhull_options="QJ").vertices].tolist()
    return final

if __name__ == "__main__":
    import trimesh
    # load object
    objtrimsh_box = trimesh.load('./objects/box.stl')
    objtrimsh_bunny = trimesh.load('./objects/bunny.stl')
    objtrimsh_housing = trimesh.load('./objects/housing.stl')
    # objtrimsh_box.show()
    # objtrimsh_bunny.show()
    # objtrimsh_housing.show()
    # minkowski_sum
    vertices_sum = functools.reduce(bi_minkowski_sum,[objtrimsh_box.vertices,objtrimsh_bunny.vertices,objtrimsh_housing.vertices])
    objtrimsh_sum = trimesh.Trimesh(vertices=vertices_sum)
    objtrimsh_convexhull =  objtrimsh_sum.convex_hull
    objtrimsh_convexhull.show()