from cmath import *
from gplot_vector3 import gplot_vector3, cross_product
from drange import drange

j = complex(0, 1)

# Returns the lambda to given omega
def get_lambda_free(omega):
	return 299792458.0 / (omega/(2.0*pi))


# Returns the wavelength within the waveguide
def get_lambda_wg(omega, a):
    lambda_free = get_lambda_free(omega)
    return lambda_free / sqrt(1.0 - (lambda_free / 2.0*a)**2)


# Returns lambda_m_n for a specific mode and frequency
def get_lambda_mn(omega, a, b, m, n):
	lambda_free = get_lambda_free(omega)
	return lambda_free / sqrt(1.0 - ((m/(2.0*a))**2 +
            (n/(2.0*b))**2)*lambda_free**2)


# Returns the Z component of the h_m_n mode at x, y, z, t
def hz(a, b, m, n, omega, lambda_mn, x, y, z, t):
    p1 = cos(m*pi*(x/a))
    p2 = cos(n*pi*(y/b))
    p3 = e**(j*(omega*t-((2.0*pi*z)/lambda_mn)))
    return p1*p2*p3


# Returns the X component of the h_m_n mode at x, y, z, t
def hx(a, b, m, n, omega, lambda_mn, x, y, z, t):
    p1 = sin(m*pi*(x/a))
    p2 = cos(n*pi*(y/b))
    p3 = e**(j*(omega*t-((2.0*pi*z)/lambda_mn)))
    return p1*p2*p3


# Returns the Y component of the h_m_n mode at x, y, z, t
def hy(a, b, m, n, omega, lambda_mn, x, y, z, t):
    p1 = cos(m*pi*(x/a))
    p2 = sin(n*pi*(y/b))
    p3 = e**(j*(omega*t-((2.0*pi*z)/lambda_mn)))
    return p1*p2*p3


# Return the h_m_n field vector at x, y, z, t
def h_vector(a, b, m, n, omega, lambda_mn, x, y, z, t):
    dx = hx(a, b, m, n, omega, lambda_mn, x, y, z, t)
    dy = hy(a, b, m, n, omega, lambda_mn, x, y, z, t)
    dz = hz(a, b, m, n, omega, lambda_mn ,x, y, z, t)
    return gplot_vector3(x, y, z, dx, dy, dz)


# Returns the electrical X component of the h_m_n mode at x, y, z, t
def ex(a, b, m, n, omega, lambda_mn, x, y, z, t):
    p1 = cos(m*pi*(x/a))
    p2 = sin(n*pi*(y/b))
    p3 = e**(j*(omega*t-((2.0*pi*z)/lambda_mn)))
    return p1*p2*p3


# Returns the electrical Y component of the h_m_n mode at x, y, z, t
def ey(a, b, m, n, omega, lambda_mn, x, y, z, t):
    p1 = -sin(m*pi*(x/a))
    p2 = cos(n*pi*(y/b))
    p3 = e**(j*(omega*t-((2.0*pi*z)/lambda_mn)))
    return p1*p2*p3


# Returns the electrical Z component of the h_m_n mode at x, y, z, t
def ez(a, b, m, n, omega, lambda_mn, x, y, z, t):
    return 0


# Return the h_m_n field vector at x, y, z, t
def e_vector(a, b, m, n, omega, lambda_mn, x, y, z, t):
    dx = ex(a, b, m, n, omega, lambda_mn, x, y, z, t)
    dy = ey(a, b, m, n, omega, lambda_mn, x, y, z, t)
    dz = ez(a, b, m, n, omega, lambda_mn ,x, y, z, t)
    return gplot_vector3(x, y, z, dx, dy, dz)


# Returns the h_field inside specified interval at time t as a list of
# gplot_vector3
def h_field(a, b, m, n, omega, lambda_mn, x_min, x_max, dx,
        y_min, y_max, dy, z_min, z_max, dz, t_min, t_max, t_step):
    for t in drange(t_min, t_max, t_step):
        for z in drange(z_min, z_max, dz):
            for y in drange(y_min, y_max, dy):
                for x in drange(x_min, x_max, dx):
                    vector_dx = hx(a, b, m, n, omega, lambda_mn, x, y, z, t)
                    vector_dy = hy(a, b, m, n, omega, lambda_mn, x, y, z, t)
                    vector_dz = hz(a, b, m, n, omega, lambda_mn, x, y, z, t)
                    yield gplot_vector3(x, y, z, vector_dx, vector_dy, vector_dz)
        # Returning None to specify the end of one time frame
        yield None


# Returns the e_field inside specified interval at time t as a list of
# gplot_vector3
def e_field(a, b, m, n, omega, lambda_mn, x_min, x_max, dx,
        y_min, y_max, dy, z_min, z_max, dz, t_min, t_max, t_step):
    for t in drange(t_min, t_max, t_step):
        for z in drange(z_min, z_max, dz):
            for y in drange(y_min, y_max, dy):
                for x in drange(x_min, x_max, dx):
                    vector_dx = ex(a, b, m, n, omega, lambda_mn, x, y, z, t)
                    vector_dy = ey(a, b, m, n, omega, lambda_mn, x, y, z, t)
                    vector_dz = ez(a, b, m, n, omega, lambda_mn, x, y, z, t)
                    yield gplot_vector3(x, y, z, vector_dx, vector_dy, vector_dz)
        # Returning None to specify the end of one time frame
        yield None


# Return the p_field (pointing vector field) by iteration over
# two joined generators h_field and e_field
def p_field(a, b, m, n, omega, lambda_mn, x_min, x_max, dx,
        y_min, y_max, dy, z_min, z_max, dz, t_min, t_max, t_step):
    for e, h in zip(e_field(a, b, m, n, omega, lambda_mn, x_min, x_max, dx,
        y_min, y_max, dy, z_min, z_max, dz, t_min, t_max, t_step),
        h_field(a, b, m, n, omega, lambda_mn, x_min, x_max, dx,
        y_min, y_max, dy, z_min, z_max, dz, t_min, t_max, t_step)):
            yield cross_product(e, h)


def scale_vector(vector, scalex, scaley, scalez):
    vector.dx *= scalex
    vector.dy *= scaley
    vector.dz *= scalez
