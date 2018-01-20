import math

# A python represantation of a gnuplot 3d vector
class gplot_vector3:
    def __init__(self, x, y, z, dx, dy, dz):
        self.x = x
        self.y = y
        self.z = z
        self.dx = dx
        self.dy = dy
        self.dz = dz

    # Multiple ways to print the vector    
    def str_as_abs(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.z) + " " + str(abs(self.dx)) + " " + str(abs(self.dy)) + " " +  str(abs(self.dz))


    def str_as_real(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.z) + " " + str(self.dx.real) + " " + str(self.dy.real) + " " +  str(self.dz.real)


    def str_as_imag(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.z) + " " + str(self.dx.imag) + " " + str(self.dy.imag) + " " +  str(self.dz.imag)

    def str_as_complete(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.z) + " " + str(self.dx.real + self.dx.imag) + " " + str(self.dy.imag + self.dy.real) + " " + str(self.dz.imag + self.dz.real)

    # deprecated
    def str_as_particle(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.z) 


    def __str__(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.z) + " " + str(self.dx) + " " + str(self.dy) + " " +  str(self.dz)

    # Calculates the abs whether the vector is complex or not
    def __abs__(self):
        if isinstance(self.dx, complex) or isinstance(self.dy, complex) or isinstance(self.dz, complex):
            return math.sqrt(abs(self.dx)**2 + abs(self.dy)**2 + abs(self.dz)**2)
        else:
            return math.sqrt(self.dx**2 + self.dy**2 + self.dz**2)


# The cross product of two gplot_vector3 instances
# used to calculate the pointing vector
def cross_product(v1, v2):
    if v1 is None or v2 is None:
        return None
    result = gplot_vector3(v1.x, v1.y, v1.z, 0, 0, 0)
    result.dx = v1.dy*v2.dz - v1.dz*v2.dy
    result.dy = v1.dz*v2.dx - v1.dx*v2.dz
    result.dz = v1.dx*v2.dy - v1.dy*v2.dx
    return result

