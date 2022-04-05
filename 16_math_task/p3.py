# TASK 3:
# ETA - TBD
# Find area between 2 overlapping polygons (can be any type of polygon)
# polygon1 = [(-10, 30), (10, 20), (15, 10), (-20, 10)]
# polygon2 = [(-20, 25), (15, 25), (15, 15), (-20, 20)]
# Area = 172


# reference - https://stackoverflow.com/questions/563198/how-do-you-detect-where-two-line-segments-intersect
import numpy as np

#line segment 1
point_p1 = np.array([10,10])
point_p2 = np.array([20,10])

#line segment 2
point_q1 = np.array([5,10])
point_q2 = np.array([10,10])

#find line segment 1 end point like "point_p2" to "point_p2 + r" 
# point_p2 + r = point_p1
r = point_p1 - point_p2

#find line segment 2 end point like "point_q2" to "point_q2 + s" 
# point_q2 + s = point_q1
s =  point_q1 - point_q2


# our t = (point_q2-point_p2) x s/ (r x s)
# our u = (point_q2-point_p2) x r/ (r x s)

#corss product of r x s
corss_product_of_r_s = np.cross(r,s)

#corss product of (point_q2-point_p2) x s
for_t = np.cross((point_q2-point_p2),s)

#corss product of (point_q2-point_p2) x r
for_u = np.cross((point_q2-point_p2),r)

if corss_product_of_r_s:
    t = for_t/corss_product_of_r_s
    u = for_u/corss_product_of_r_s
    
    if (t >= 0 and t <= 1) and (u >=0 and u <= 1) and (point_q2 + (u * s))[0]==(point_q2 + (u * s))[0] and (point_q2 + (u * s))[1]==(point_q2 + (u * s))[1]:
        print(point_p2 + (t * r),'@@@@')

if not corss_product_of_r_s and (not for_u): 
    t0 = np.dot((point_q2-point_p2),r) / (np.dot(r,r))
    t1 = t0 + (np.dot(s,r) / (np.dot(r,r)))
    print(t0,t1,'----')
    # print(point_p2 + (t1 * r),'----')
    # print(point_q1 + (t1 * s),'----')
    if (0<=t0 and 1>=t0) or (0<=t1 and 1>= t0):
        print('yes')
        if point_p1[1] == point_q1[1] and point_p2[1] == point_q2[1]:
            print('y same') 
        else:
            print('x same')
