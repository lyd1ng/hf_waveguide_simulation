#####################
#  ######################
#    ######################
#  ######################
######################
from cmath import *
from drange import drange
from argparse import ArgumentParser
from gplot_vector3 import gplot_vector3
from particle_current import funnel_particles_e_field, funnel_particles_h_field
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
parser.add_argument("--t", type=float, help="Point of time", required=True)
parser.add_argument("--particles", type=int, help="Number of particles")
parser.add_argument("--particle_speed", type=float, help="The speed of particles")
parser.add_argument("--iterations", type=int, help="Number of iterations")
parser.add_argument("--final_only", type=int, help="Output just the last iteration")
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
    for i in range(0, ARGS.iterations):
        # Move every particle one step along the e field
        funnel_particles_e_field(particles, discarded_particles,
        ARGS.particle_speed, ARGS.a, ARGS.b, ARGS.m, ARGS.n, ARGS.w,
        lambda_mn, ARGS.x_min, ARGS.x_max, ARGS.y_min, ARGS.y_max,
        ARGS.z_min, ARGS.z_max, ARGS.t)
    
        # Write particles and discarded particles to file if every iteration
        # should be safed or its the last iteration
        if (ARGS.final_only == 0 ) or ( i == ARGS.iterations - 1):
            for p in particles:
                particles_out_fd.write(p.str_as_real() + "\n")
            for dp in discarded_particles:
                discarded_particles_out_fd.write(dp.str_as_real() + "\n")
            # Terminate frames with "\n\n" to make gnuplot gif
            # exportation possible
            particles_out_fd.write("\n\n")
            discarded_particles_out_fd.write("\n\n")


# Run the simulation if the h field is specified
if ARGS.f == 'h':
    for i in range(0, ARGS.iterations):
        # Move every particle one step along the h field
        funnel_particles_h_field(particles, discarded_particles,
        ARGS.particle_speed, ARGS.a, ARGS.b, ARGS.m, ARGS.n, ARGS.w,
        lambda_mn, ARGS.x_min, ARGS.x_max, ARGS.y_min, ARGS.y_max,
        ARGS.z_min, ARGS.z_max, ARGS.t)
    
        # Write particles and discarded particles to file if every iteration
        # should be safed or its the last iteration
        if (ARGS.final_only == 0 ) or ( i == ARGS.iterations - 1):
            for p in particles:
                particles_out_fd.write(p.str_as_real() + "\n")
            for dp in discarded_particles:
                discarded_particles_out_fd.write(dp.str_as_real() + "\n")
            # Terminate frames with "\n\n" to make gnuplot gif
            # exportation possible
            particles_out_fd.write("\n\n")
            discarded_particles_out_fd.write("\n\n")


# Close files
particles_out_fd.close()
discarded_particles_out_fd.close()
