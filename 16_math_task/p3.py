import numpy as np

poly_1 = [[-10,30],[10,20],[15,10],[-20,10],[-10,30]]
poly_2 = [[-20,25],[15,25],[10,10],[-10,10],[-20,25]]

final_cord_of_intersept = []

for ploy_1_index in range(0,len(poly_1)-1):
    for poly_2_index in range(0,len(poly_2)-1):

        #line segment 1
        point_p1 = np.array(poly_1[ploy_1_index])
        point_p2 = np.array(poly_1[ploy_1_index+1])
        
        #line segment 2
        point_q1 = np.array(poly_2[poly_2_index])
        point_q2 = np.array(poly_2[poly_2_index+1])
        
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
                intersect_point = point_p2 + (t * r)
                # print(point_p2 + (t * r),'Intersect')
                if list(intersect_point) not in final_cord_of_intersept:
                    final_cord_of_intersept.append(list(intersect_point))
                
        #For colliner
        if not corss_product_of_r_s and (not for_u): 
            t0 = np.dot((point_q2-point_p2),r) / (np.dot(r,r))
            t1 = t0 + (np.dot(s,r) / (np.dot(r,r)))
            
            #for colliner with overlapping
            if (0<=t0 and 1>=t0) or (0<=t1 and 1>= t0):
                # print('yes')
                if (min(point_p1[0],point_p2[0])<=point_q1[0] and max(point_p1[0],point_p2[0])>=point_q1[0]) and (min(point_p1[1],point_p2[1])<=point_q1[1] and max(point_p1[1],point_p2[1])>=point_q1[1]):
                    if list(point_q1) not in final_cord_of_intersept:
                        final_cord_of_intersept.append(list(point_q1))
                        
                if (min(point_p1[0],point_p2[0])<=point_q2[0] and max(point_p1[0],point_p2[0])>=point_q2[0]) and (min(point_p1[1],point_p2[1])<=point_q2[1] and max(point_p1[1],point_p2[1])>=point_q2[1]):
                    if list(point_q2) not in final_cord_of_intersept:
                        final_cord_of_intersept.append(list(point_q2))
                        
                if (min(point_q1[0],point_q2[0])<=point_p1[0] and max(point_q1[0],point_q2[0])>=point_p1[0]) and (min(point_q1[1],point_q2[1])<=point_p1[1] and max(point_q1[1],point_q2[1])>=point_p1[1]):
                    if list(point_p1) not in final_cord_of_intersept:
                        final_cord_of_intersept.append(list(point_p1))
                        
                if (min(point_q1[0],point_q2[0])<=point_p2[0] and max(point_q1[0],point_q2[0])>=point_p2[0]) and (min(point_q1[1],point_q2[1])<=point_p2[1] and max(point_q1[1],point_q2[1])>=point_p2[1]):
                    if list(point_p2) not in final_cord_of_intersept:
                        final_cord_of_intersept.append(list(point_p2))

print(final_cord_of_intersept)
        
        














