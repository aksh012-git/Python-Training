# Python program to find total area of two
# overlapping Rectangles
# Returns Total Area of two overlap
# rectangles


def overlappingArea(l1, r1, l2, r2):
	x = 0
	y = 1
	x_dist = (min(r1[x], r2[x]) -
			max(l1[x], l2[x]))

	y_dist = (min(r1[y], r2[y]) -
			max(l1[y], l2[y]))
    
	areaI = 0
	if x_dist > 0 and y_dist > 0:
		areaI = x_dist * y_dist

	print(r1,r2,l1,l2,areaI,x_dist,y_dist)



# Driver's Code
l1 = [3, 2]
r1 = [6, 5]
l2 = [5, 4]
r2 = [8, 7]

# Function call
print(overlappingArea(l1, r1, l2, r2))

# This code is contributed by Manisha_Ediga
