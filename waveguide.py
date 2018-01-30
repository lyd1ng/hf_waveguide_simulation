#####################
#  ######################
#    ######################
#  ######################
######################
from cmath import *
from argparse import ArgumentParser
import h_modes

parser = ArgumentParser(allow_abbrev=False)
# Required Parameters
parser.add_argument("-a", type=float, help="Width of the waveguide", required=True)
parser.add_argument("-b", type=float, help="Height of the waveguide", required=True)
parser.add_argument("-m", type=float, help="The m mode number", required=True)
parser.add_argument("-n", type=float, help="The n mode number", required=True)
parser.add_argument("-w", type=float, help="Frequency of the signale", required=True)
parser.add_argument("-f", help="Field type to calculate (e, h, p)", required=True)
parser.add_argument("-o", help="The output file", required=True)
parser.add_argument("--x_min", type=float, help="The minimal x coordinate", required=True)
parser.add_argument("--x_max", type=float, help="The maximal x coordinate", required=True)
parser.add_argument("--x_step", type=float, help="The x step", required=True)
parser.add_argument("--y_min", type=float, help="The minimal y coordinate", required=True)
parser.add_argument("--y_max", type=float, help="The maximal y coordinate", required=True)
parser.add_argument("--y_step", type=float, help="The y step", required=True)
parser.add_argument("--z_min", type=float, help="The minimal z coordinate", required=True)
parser.add_argument("--z_max", type=float, help="The maximal z coordinate", required=True)
parser.add_argument("--z_step", type=float, help="THe z step", required=True)
parser.add_argument("--t_min", type=float, help="The start time", required=True)
parser.add_argument("--t_max", type=float, help="The end time", required=True)
parser.add_argument("--t_step", type=float, help="The timestep", required=True) 
parser.add_argument("--scale_x", type=float, help="The x scale of all vectors", required=True)
parser.add_argument("--scale_y", type=float, help="The x scale of all vectors", required=True)
parser.add_argument("--scale_z", type=float, help="The x scale of all vectors", required=True)

# Parse the Parameters
ARGS = parser.parse_args()

#Calculate the lambda_mn
lambda_mn = h_modes.get_lambda_mn(ARGS.w, ARGS.a, ARGS.b, ARGS.m, ARGS.n)

#Open outputfile
output_fd = open(ARGS.o, "w")

if ARGS.f == 'e':
    for v in h_modes.e_field(ARGS.a, ARGS.b, ARGS.m, ARGS.n, ARGS.w, lambda_mn,
            ARGS.x_min, ARGS.x_max, ARGS.x_step,
            ARGS.y_min, ARGS.y_max, ARGS.y_step,
            ARGS.z_min, ARGS.z_max, ARGS.z_step,
            ARGS.t_min, ARGS.t_max, ARGS.t_step):
        if ( v is not None ):
            h_modes.scale_vector(v, ARGS.scale_x, ARGS.scale_y, ARGS.scale_z)
            output_fd.write(v.str_as_real() + "\n")
        else:
            output_fd.write("\n\n")

if ARGS.f == 'h':
    for v in h_modes.h_field(ARGS.a, ARGS.b, ARGS.m, ARGS.n, ARGS.w, lambda_mn,
            ARGS.x_min, ARGS.x_max, ARGS.x_step,
            ARGS.y_min, ARGS.y_max, ARGS.y_step,
            ARGS.z_min, ARGS.z_max, ARGS.z_step,
            ARGS.t_min, ARGS.t_max, ARGS.t_step):
        if ( v is not None ):
            h_modes.scale_vector(v, ARGS.scale_x, ARGS.scale_y, ARGS.scale_z)
            output_fd.write(v.str_as_real() + "\n")
        else:
            output_fd.write("\n\n")

if ARGS.f == 'p':
    for v in h_modes.p_field(ARGS.a, ARGS.b, ARGS.m, ARGS.n, ARGS.w, lambda_mn,
            ARGS.x_min, ARGS.x_max, ARGS.x_step,
            ARGS.y_min, ARGS.y_max, ARGS.y_step,
            ARGS.z_min, ARGS.z_max, ARGS.z_step,
            ARGS.t_min, ARGS.t_max, ARGS.t_step):
        if ( v is not None ):
            h_modes.scale_vector(v, ARGS.scale_x, ARGS.scale_y, ARGS.scale_z)
            output_fd.write(v.str_as_real() + "\n")
        else:
            output_fd.write("\n\n")

output_fd.close()
