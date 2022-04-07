import numpy as np

poly_1 = [[-10,30],[10,20],[13,18],[-20,10],[-10,30]]
poly_2 = [[-20,30],[15,25],[15,15],[-5,10],[-20,25]]

final_cord_of_intersept = []

for cord_index_1 in range(0,len(poly_1)-1):
    for cord_index_2 in range(0,len(poly_2)-1):
        point_p1 = np.array(poly_1[cord_index_1])
        #adding end point of point_p1
        add_end_point = abs(poly_1[cord_index_1][0])
        point_p2 = np.array(poly_1[cord_index_1]) + np.array([add_end_point + (35*2),0])
        
        
        #for ploy_2 line point
        point_q1 = np.array(poly_2[cord_index_2])
        point_q2 = np.array(poly_2[cord_index_2+1])
        
        # print(point_p1,point_p2)
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
                final_cord_of_intersept.append(list(point_p1))
                
        #For colliner
        if not corss_product_of_r_s and (not for_u): 
            t0 = np.dot((point_q2-point_p2),r) / (np.dot(r,r))
            t1 = t0 + (np.dot(s,r) / (np.dot(r,r)))
            
            #for colliner with overlapping
            if (0<=t0 and 1>=t0) or (0<=t1 and 1>= t0):
                # print('yes')
                if (min(point_p1[0],point_p2[0])<=point_q1[0] and max(point_p1[0],point_p2[0])>=point_q1[0]) and (min(point_p1[1],point_p2[1])<=point_q1[1] and max(point_p1[1],point_p2[1])>=point_q1[1]):
                        final_cord_of_intersept.append(list(point_p1))
                        
                if (min(point_p1[0],point_p2[0])<=point_q2[0] and max(point_p1[0],point_p2[0])>=point_q2[0]) and (min(point_p1[1],point_p2[1])<=point_q2[1] and max(point_p1[1],point_p2[1])>=point_q2[1]):
                        final_cord_of_intersept.append(list(point_p1))
                        
                if (min(point_q1[0],point_q2[0])<=point_p1[0] and max(point_q1[0],point_q2[0])>=point_p1[0]) and (min(point_q1[1],point_q2[1])<=point_p1[1] and max(point_q1[1],point_q2[1])>=point_p1[1]):
                        final_cord_of_intersept.append(list(point_p1))
                        
                if (min(point_q1[0],point_q2[0])<=point_p2[0] and max(point_q1[0],point_q2[0])>=point_p2[0]) and (min(point_q1[1],point_q2[1])<=point_p2[1] and max(point_q1[1],point_q2[1])>=point_p2[1]):
                        final_cord_of_intersept.append(list(point_p1))

print(final_cord_of_intersept,'-----')

final_cord_of_intersept = []

for cord_index_1 in range(0,len(poly_2)-1):
    for cord_index_2 in range(0,len(poly_1)-1):
        point_p1 = np.array(poly_2[cord_index_1])
        #adding end point of point_p1
        add_end_point = abs(poly_2[cord_index_1][0])
        point_p2 = np.array(poly_2[cord_index_1]) + np.array([add_end_point + (35*2),0])
        
        
        #for ploy_2 line point
        point_q1 = np.array(poly_1[cord_index_2])
        point_q2 = np.array(poly_1[cord_index_2+1])
        
        # print(point_p1,point_p2)
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
                # print(point_q1,point_q2)
                final_cord_of_intersept.append(list(point_p1))
                
        #For colliner
        if not corss_product_of_r_s and (not for_u): 
            t0 = np.dot((point_q2-point_p2),r) / (np.dot(r,r))
            t1 = t0 + (np.dot(s,r) / (np.dot(r,r)))
            # print(t0,t1)
            #for colliner with overlapping
            if (0<=t0 and 1>=t0) or (0<=t1 and 1>= t1):
                # print('yes')
                if (min(point_p1[0],point_p2[0])<=point_q1[0] and max(point_p1[0],point_p2[0])>=point_q1[0]) and (min(point_p1[1],point_p2[1])<=point_q1[1] and max(point_p1[1],point_p2[1])>=point_q1[1]):
                        final_cord_of_intersept.append(list(point_p1))
                        
                if (min(point_p1[0],point_p2[0])<=point_q2[0] and max(point_p1[0],point_p2[0])>=point_q2[0]) and (min(point_p1[1],point_p2[1])<=point_q2[1] and max(point_p1[1],point_p2[1])>=point_q2[1]):
                        final_cord_of_intersept.append(list(point_p1))
                        
                        
                if (min(point_q1[0],point_q2[0])<=point_p1[0] and max(point_q1[0],point_q2[0])>=point_p1[0]) and (min(point_q1[1],point_q2[1])<=point_p1[1] and max(point_q1[1],point_q2[1])>=point_p1[1]):
                        final_cord_of_intersept.append(list(point_p1))
                        
                if (min(point_q1[0],point_q2[0])<=point_p2[0] and max(point_q1[0],point_q2[0])>=point_p2[0]) and (min(point_q1[1],point_q2[1])<=point_p2[1] and max(point_q1[1],point_q2[1])>=point_p2[1]):
                        final_cord_of_intersept.append(list(point_p1))

print(final_cord_of_intersept,'---')

    