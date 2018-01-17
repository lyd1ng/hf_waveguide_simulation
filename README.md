usage: waveguide.py [-h] -a A -b B -m M -n N -w W -f F --x_min X_MIN --x_max
                    X_MAX --x_step X_STEP --y_min Y_MIN --y_max Y_MAX --y_step
                    Y_STEP --z_min Z_MIN --z_max Z_MAX --z_step Z_STEP --t_min
                    T_MIN [--t_max T_MAX] [--t_step T_STEP] --scale_x SCALE_X
                    --scale_y SCALE_Y --scale_z SCALE_Z -o O

optional arguments:
  -h, --help         show this help message and exit
  -a A               Width of the waveguide
  -b B               Height of the waveguide
  -m M               The m mode number
  -n N               The n mode number
  -w W               Frequency of the signale
  -f F               Field type to calculate (e, h)
  --x_min X_MIN      The minimal x coordinate
  --x_max X_MAX      The maximal x coordinate
  --x_step X_STEP    The x step
  --y_min Y_MIN      The minimal y coordinate
  --y_max Y_MAX      The maximal y coordinate
  --y_step Y_STEP    The y step
  --z_min Z_MIN      The minimal z coordinate
  --z_max Z_MAX      The maximal z coordinate
  --z_step Z_STEP    THe z step
  --t_min T_MIN      The start time
  --t_max T_MAX      The end time
  --t_step T_STEP    The timestep
  --scale_x SCALE_X  The x scale of all vectors
  --scale_y SCALE_Y  The x scale of all vectors
  --scale_z SCALE_Z  The x scale of all vectors
  -o O               The output file
