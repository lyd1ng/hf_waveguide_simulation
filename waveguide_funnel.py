#####################
#  ######################
#    ######################
#  ######################
######################
from cmath import *
from drange import drange
from argparse import ArgumentParser
from gplot_vector3 import gplot_vector3
from particle_funnel import funnel_particles_e_field, funnel_particles_h_field
import h_modes
from random import random

parser = ArgumentParser(allow_abbrev=False)
parser.set_defaults(required=True)
parser.add_argument("-a", type=float, help="Width of the waveguide", required=True)
parser.add_argument("-b", type=float, help="Height of the waveguide", required=True)
parser.add_argument("-m", type=float, help="The m mode number", required=True)
parser.add_argument("-n", type=float, help="The n mode number", required=True)
parser.add_argument("-w", type=float, help="Frequency of the signale", required=True)
parser.add_argument("-f", help="Field type to calculate (e, h)", required=True)
parser.add_argument("--x_min", type=float, help="The minimal x coordinate", required=True)
parser.add_argument("--x_max", type=float, help="The maximal x coordinate", required=True)
parser.add_argument("--y_min", type=float, help="The minimal y coordinate", required=True)
parser.add_argument("--y_max", type=float, help="The maximal y coordinate", required=True)
parser.add_argument("--z_min", type=float, help="The minimal z coordinate", required=True)
parser.add_argument("--z_max", type=float, help="The maximal z coordinate", required=True)
parser.add_argument("--t_min", type=float, help="Point of time", required=True)
parser.add_argument("--t_max", type=float, help="End time", required=True)
parser.add_argument("--t_step", type=float, help="Time step", required=True)
parser.add_argument("--particles", type=int, help="Number of particles")
parser.add_argument("--particle_speed", type=float, help="The speed of particles")
parser.add_argument("--iterations", type=int, help="Number of iterations")
parser.add_argument("--po", help="The particle output file")
parser.add_argument("--dpo", help="The discarded particle output file")

# Parse the Parameters
ARGS = parser.parse_args()

# Calculate the lambda_mn
lambda_mn = h_modes.get_lambda_mn(ARGS.w, ARGS.a, ARGS.b, ARGS.m, ARGS.n)

# Open outputfiles
particles_out_fd = open(ARGS.po, "w")
discarded_particles_out_fd = open(ARGS.dpo, "w")


# Initialise the particle lists
particles = list()
discarded_particles = list()
for i in range(0, ARGS.particles):
    x = ARGS.x_min + (ARGS.x_max - ARGS.x_min)*random()
    y = ARGS.y_min + (ARGS.y_max - ARGS.y_min)*random()
    z = ARGS.z_min + (ARGS.z_max - ARGS.z_min)*random()
    particles.append(gplot_vector3(x, y, z, 0, 0, 0))


# Run the simulation if the e field is specified
if ARGS.f == 'e':
    for t in drange(ARGS.t_min, ARGS.t_max, ARGS.t_step):
        # Initialise the particle lists
        particles = list()
        discarded_particles = list()
        for i in range(0, ARGS.particles):
            x = ARGS.x_min + (ARGS.x_max - ARGS.x_min)*random()
            y = ARGS.y_min + (ARGS.y_max - ARGS.y_min)*random()
            z = ARGS.z_min + (ARGS.z_max - ARGS.z_min)*random()
            particles.append(gplot_vector3(x, y, z, 0, 0, 0))
    
        # Run the real simulation
        funnel_particles_e_field(particles, discarded_particles, ARGS.iterations,
            ARGS.particle_speed, ARGS.a, ARGS.b, ARGS.m, ARGS.n, ARGS.w,
            lambda_mn, ARGS.x_min, ARGS.x_max, ARGS.y_min, ARGS.y_max,
            ARGS.z_min, ARGS.z_max, t)

        # Write particles to file
        if len(particles) > 0:
            for p in particles:
                particles_out_fd.write(p.str_as_particle() + "\n")
    
        # Write discarded particles to file
        if len(discarded_particles) > 0:
            for dp in discarded_particles:
                discarded_particles_out_fd.write(dp.str_as_particle() + "\n")

        #End both blocks with two empty lines (gnuplot specific)
        particles_out_fd.write("\n\n")
        discarded_particles_out_fd.write("\n\n")


# Run the simulation if the h field is specified
if ARGS.f == 'h':
    for t in drange(ARGS.t_min, ARGS.t_max, ARGS.t_step):
        # Initialise the particle lists
        particles = list()
        discarded_particles = list()
        for i in range(0, ARGS.particles):
            x = ARGS.x_min + (ARGS.x_max - ARGS.x_min)*random()
            y = ARGS.y_min + (ARGS.y_max - ARGS.y_min)*random()
            z = ARGS.z_min + (ARGS.z_max - ARGS.z_min)*random()
            particles.append(gplot_vector3(x, y, z, 0, 0, 0))
    
        # Run the real simulation
        funnel_particles_h_field(particles, discarded_particles, ARGS.iterations,
            ARGS.particle_speed, ARGS.a, ARGS.b, ARGS.m, ARGS.n, ARGS.w,
            lambda_mn, ARGS.x_min, ARGS.x_max, ARGS.y_min, ARGS.y_max,
            ARGS.z_min, ARGS.z_max, t)

        # Write particles to file
        if len(particles) > 0:
            for p in particles:
                particles_out_fd.write(p.str_as_particle() + "\n")
    
        # Write discarded particles to file
        if len(discarded_particles) > 0:
            for dp in discarded_particles:
                discarded_particles_out_fd.write(dp.str_as_particle() + "\n")

        #End both blocks with two empty lines (gnuplot specific)
        particles_out_fd.write("\n\n")
        discarded_particles_out_fd.write("\n\n")


# Run the simulation if the h field is specified
# Close files
particles_out_fd.close()
discarded_particles_out_fd.close()
