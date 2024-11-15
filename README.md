# pysdf
This is a simple library for converting an SDF into an STL file for 3d printing. Unlike other SDF CAD software, this does not define any primative shapes that you use boolean operations on; rather you simply define a class containing a function `f(x, y, z)` which returns the distance at the given point. This allows easy translation of complex implicit mathematical formulae into 3D models.

# Examples

A 3D model generated by `V1` in `test.py`. Note that a low resolution of 60 was used, which results in the underlying voxel grid being visible. Using a higher resolution like 100 or 200 is recommended before printing, although may be rather intensive to generate for testing.

![A 3D printed vase](vase.jpg)
