# Find the overlapping area of two rectangles
# Rectangles can be in any direction
# A = 2      E = 4   left point
# B = 2      F = 4   top point
# C = 6      G = 8   right point
# D = 6      H = 8   bottom point

# Ans = 4

r1_1 = [2,6]
r1_2 = [6,2]

r2_1 = [4,4]
r2_2 = [8,8]

r1_slop = (r1_1[0] - r1_2[0])/(r1_1[1] - r1_2[1])
r2_slop = (r2_1[0] - r2_2[0])/(r2_1[1] - r2_2[1])

print(r1_slop,r2_slop)

r1_1_ = []
r1_2_ = []
r2_1_ = []
r2_2_ = []

if r1_slop < 0:
    r1_1_.append(min(r1_1[0],r1_2[0]))
    r1_1_.append(min(r1_1[1],r1_2[1]))
    r1_2_.append(max(r1_1[0],r1_2[0]))
    r1_2_.append(max(r1_1[1],r1_2[1]))  
if r2_slop < 0:
    print(r2_slop)
    
    