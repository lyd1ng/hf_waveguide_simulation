from gplot_vector3 import gplot_vector3
from h_modes import h_vector, e_vector, scale_vector


# Discard every particle outside the boundaries
# This way only particles inside the waveguide are updated
def discard_particles(particles, x_min, x_max,
        y_min, y_max, z_min, z_max):
    discarded_particles = list()
    for i in range(0, len(particles)):
        if (particles[i].x < x_min or particles[i].x > x_max or
            particles[i].y < y_min or particles[i].y > y_max or
            particles[i].z < z_min or particles[i].z > z_max):
                # Remove particle from particles and add it
                # to discarded_particles
                discarded_particles.append(particles[i])
    # Now we have to delete every discarded particle from
    # particle list
    for dp in discarded_particles:
        if dp in particles:
            particles.remove(dp)


# Move every particle (gplot_vector3) in particles along
# the e field at fix t
# This way particles hopefully accumulate at e field vortices
def funnel_particles_e_field(args):
    particles, speed, a, b, m, n, omega, lambda_mn, x_min, x_max, y_min, y_max, z_min, z_max, t = args
    discard_particles(particles, x_min, x_max,
    y_min, y_max, z_min, z_max)
    for p in particles:
        v = e_vector(a, b, m, n, omega, lambda_mn, p.x, p.y, p.z, t)
        scale_vector(v, speed, speed, speed)
        p.x += v.dx.real
        p.y += v.dy.real
        p.z += v.dz.real
        p.dx = v.dx.real
        p.dy = v.dy.real
        p.dz = v.dz.real
    return particles

# Move every particle (gplot_vector3) in particles along
# the h field at fix t
# This way particles hopefully accumulate at h field vortices
def funnel_particles_h_field(args):
    particles, speed, a, b, m, n, omega, lambda_mn, x_min, x_max, y_min, y_max, z_min, z_max, t = args
    # Check for particles outsite the waveguide
    discard_particles(particles, x_min, x_max,
        y_min, y_max, z_min, z_max)
    # Move every particle one step
    for p in particles:
        v = h_vector(a, b, m, n, omega, lambda_mn, p.x, p.y, p.z, t)
        scale_vector(v, speed, speed, speed)
        p.x += v.dx.real
        p.y += v.dy.real
        p.z += v.dz.real
        p.dx = v.dx.real
        p.dy = v.dy.real
        p.dz = v.dz.real
    return particles
