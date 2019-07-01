# import your Point class

# open the file from stdin for reading

# read in all lines in the input file, create the points, and add them to a Python list

# create an empty dictionary

# for each data point read in from the file...

	# compare the current point to all other input points and compute the slope

		# if the points are equal, continue (use the overridden __eq__ method)

		# else, compute the slope between the two points

		# if the str(slope) does not exist as a key in the dictionary...
		# add the str(slope) as the key and add both points to the set

		# else, calculate the slope between the current point and all other
		# points in the set; if they all match, add the point to the set

# once you've processed all of the points, go through the dictionary and find all keys
# who have a set of length 4; these will be your lines consisting of 4 collinear points

# plot each of these lines using the stddraw library and submit each one along with your code
