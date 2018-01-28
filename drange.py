#####################
#  ######################
#    ###     drange.py  ###
#  ######################
######################

# A generator object similar to range but with decimal step
def drange(start, stop, step):
	r = start
	while r < stop:
		yield r
		r += step
