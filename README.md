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
