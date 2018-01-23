# What is the hf_waveguide_simulation?

The hf_waveguide_simulation mostly consists of two python scripts  
to simulate the radio frequency field of h-modes inside a rectangular  
waveguide.  
  
## waveguide.py
The waveguide.py script can be used to calculate the vectors of  
the electrical, magnetical or the pointing field of one h-mode  
inside a subrange of the waveguide.  
By specifying a start and a stop time the changes of the radio frequency field  
can be visualised.   
The output is compatible with gnuplot and gnuplot animated gif exportation.  

```
usage: waveguide_particle_current.py [-h] -a A -b B -m M -n N -w W -f F
                                     --x_min X_MIN --x_max X_MAX --y_min Y_MIN
                                     --y_max Y_MAX --z_min Z_MIN --z_max Z_MAX
                                     --t T [--particles PARTICLES]
                                     [--particle_speed PARTICLE_SPEED]
                                     [--iterations ITERATIONS]
                                     [--final_only FINAL_ONLY] [--po PO]
                                     [--dpo DPO]

optional arguments:
  -h, --help            show this help message and exit
  -a A                  Width of the waveguide
  -b B                  Height of the waveguide
  -m M                  The m mode number
  -n N                  The n mode number
  -w W                  Frequency of the signale
  -f F                  Field type to calculate (e, h)
  --x_min X_MIN         The minimal x coordinate
  --x_max X_MAX         The maximal x coordinate
  --y_min Y_MIN         The minimal y coordinate
  --y_max Y_MAX         The maximal y coordinate
  --z_min Z_MIN         The minimal z coordinate
  --z_max Z_MAX         The maximal z coordinate
  --t T                 Point of time
  --particles PARTICLES
                        Number of particles
  --particle_speed PARTICLE_SPEED
                        The speed of particles
  --iterations ITERATIONS
                        Number of iterations
  --final_only FINAL_ONLY
                        Output just the last iteration
  --po PO               The particle output file
  --dpo DPO             The discarded particle output file
```

## waveguide_particle_current.py  
The waveguide_particle_current.py script can be used to visualize  
the radio frequency field by funneling particles along the vectors.
The output is compatible with gnuplot and gnuplot animated gif exportation.

## Plotting with gnuplot
As the output is gnuplot compatible gnuplot scripts can be used to
plot the output of static simulations or export dynamic simulations 
to animated gifs.

1. plot_particles.gps
1. plot_particles_animated.gps
1. plot_vectors.gps
1. plot_vectors_animated.gps
