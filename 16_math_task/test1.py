from matplotlib.pyplot import flag
import numpy as np
# point_p1 = np.array([10,20])
# point_p2 = np.array([15,10])
# point_q1 = np.array([20,10])
# point_q2 = np.array([-10,10])

# point_p1 = np.array([-20,10])
# point_p2 = np.array([15,10])
# point_q1 = np.array([10,10])
# point_q2 = np.array([-10,10])

# point_p1 = np.array([-20,10])
# point_p2 = np.array([15,10])
# point_q1 = np.array([15,10])
# point_q2 = np.array([-10,10])

temp = []

# point_p1 = np.array([-20,10])
# point_p2 = np.array([15,10])
# point_q1 = np.array([15,10])
# point_q2 = np.array([-20,10])


point_p1 = np.array([-20,10])
point_p2 = np.array([15,10])
point_q1 = np.array([15,10])
point_q2 = np.array([20,10])

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

#For intersection
if corss_product_of_r_s:
    t = for_t/corss_product_of_r_s
    u = for_u/corss_product_of_r_s
    if (t >= 0 and t <= 1) and (u >=0 and u <= 1) and (point_q2 + (u * s))[0]==(point_q2 + (u * s))[0] and (point_q2 + (u * s))[1]==(point_q2 + (u * s))[1]:
        print(point_p2 + (t * r),'Intersect')
        temp.append(point_p2 + (t * r))
        
#For colliner
if not corss_product_of_r_s and (not for_u): 
    t0 = np.dot((point_q2-point_p2),r) / (np.dot(r,r))
    t1 = t0 + (np.dot(s,r) / (np.dot(r,r)))
    print(t0,t1)
    
    #for colliner with overlapping
    if (0<=t0 and 1>=t0) or (0<=t1 and 1>= t0):
        # print('yes')
        if (min(point_p1[0],point_p2[0])<=point_q1[0] and max(point_p1[0],point_p2[0])>=point_q1[0]) and (min(point_p1[1],point_p2[1])<=point_q1[1] and max(point_p1[1],point_p2[1])>=point_q1[1]):
            flag = False
            for cord in temp:
                if (cord[0] != point_q1[0]) or (cord[1]!= point_q1[1]):
                    flag = True
                else:
                    flag = False
                    break
            if flag:
                temp.append(point_q1)
            elif len(temp) == 0:
                temp.append(point_q1)
        if (min(point_p1[0],point_p2[0])<=point_q2[0] and max(point_p1[0],point_p2[0])>=point_q2[0]) and (min(point_p1[1],point_p2[1])<=point_q2[1] and max(point_p1[1],point_p2[1])>=point_q2[1]):
            flag = False
            for cord in temp:
                if (cord[0] != point_q2[0]) or (cord[1]!= point_q2[1]):
                    flag = True
                else:
                    flag = False
                    break
            if flag:
                temp.append(point_q2)
        if (min(point_q1[0],point_q2[0])<=point_p1[0] and max(point_q1[0],point_q2[0])>=point_p1[0]) and (min(point_q1[1],point_q2[1])<=point_p1[1] and max(point_q1[1],point_q2[1])>=point_p1[1]):
            flag = False
            for cord in temp:
                if (cord[0] != point_p1[0]) or (cord[1]!= point_p1[1]):
                   flag = True
                else:
                    flag = False
                    break
            if flag:
                temp.append(point_p1)
        if (min(point_q1[0],point_q2[0])<=point_p2[0] and max(point_q1[0],point_q2[0])>=point_p2[0]) and (min(point_q1[1],point_q2[1])<=point_p2[1] and max(point_q1[1],point_q2[1])>=point_p2[1]):
            flag = False
            for cord in temp:
                if (cord[0] != point_p2[0]) or (cord[1]!= point_p2[1]):
                   flag = True
                else:
                    flag = False
                    break
            if flag:
                temp.append(point_p2)

print(temp)
