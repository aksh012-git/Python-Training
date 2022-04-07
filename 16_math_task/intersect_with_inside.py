class FindIntersect():
    def __init__(self,point_p1,point_p2,point_q1,point_q2):
        self.point_p1 = point_p1
        self.point_p2 = point_p2
        self.point_q1 = point_q1
        self.point_q2 = point_q2
        
    def checkInside(self):
        # print(point_p1,point_p2)
        #find line segment 1 end point like "point_p2" to "point_p2 + r"
        # point_p2 + r = point_p1
        r = self.point_p1 - self.point_p2

        #find line segment 2 end point like "point_q2" to "point_q2 + s"
        # point_q2 + s = self.point_q1
        s =  self.point_q1 - self.point_q2

        # our t = (self.point_q2-point_p2) x s/ (r x s)
        # our u = (self.point_q2-point_p2) x r/ (r x s)

        #corss product of r x s
        corss_product_of_r_s = np.cross(r,s)

        #corss product of (self.point_q2-point_p2) x s
        for_t = np.cross((self.point_q2-self.point_p2),s)

        #corss product of (self.point_q2-self.point_p2) x r
        for_u = np.cross((self.point_q2-self.point_p2),r)

        #For intersection
        if corss_product_of_r_s:
            t = for_t/corss_product_of_r_s
            u = for_u/corss_product_of_r_s
            if (t >= 0 and t <= 1) and (u >=0 and u <= 1) and (self.point_q2 + (u * s))[0]==(self.point_q2 + (u * s))[0] and (self.point_q2 + (u * s))[1]==(self.point_q2 + (u * s))[1]:
                intersect_point = self.point_p2 + (t * r)
                # print(self.point_p2 + (t * r),'Intersect')
                final_cord_of_intersept.append(list(self.point_p1))
                
        #For colliner
        if not corss_product_of_r_s and (not for_u): 
            t0 = np.dot((self.point_q2-self.point_p2),r) / (np.dot(r,r))
            t1 = t0 + (np.dot(s,r) / (np.dot(r,r)))
            
            #for colliner with overlapping
            if (0<=t0 and 1>=t0) or (0<=t1 and 1>= t1):
                # print('yes')
                if (min(self.point_p1[0],self.point_p2[0])<=self.point_q1[0] and max(self.point_p1[0],self.point_p2[0])>=self.point_q1[0]) and (min(self.point_p1[1],self.point_p2[1])<=self.point_q1[1] and max(self.point_p1[1],self.point_p2[1])>=self.point_q1[1]):
                        final_cord_of_intersept.append(list(self.point_p1))
                        
                if (min(self.point_p1[0],self.point_p2[0])<=self.point_q2[0] and max(self.point_p1[0],self.point_p2[0])>=self.point_q2[0]) and (min(self.point_p1[1],self.point_p2[1])<=self.point_q2[1] and max(self.point_p1[1],self.point_p2[1])>=self.point_q2[1]):
                        final_cord_of_intersept.append(list(self.point_p1))
                        
                if (min(self.point_q1[0],self.point_q2[0])<=self.point_p1[0] and max(self.point_q1[0],self.point_q2[0])>=self.point_p1[0]) and (min(self.point_q1[1],self.point_q2[1])<=self.point_p1[1] and max(self.point_q1[1],self.point_q2[1])>=self.point_p1[1]):
                        final_cord_of_intersept.append(list(self.point_p1))
                        
                if (min(self.point_q1[0],self.point_q2[0])<=self.point_p2[0] and max(self.point_q1[0],self.point_q2[0])>=self.point_p2[0]) and (min(self.point_q1[1],self.point_q2[1])<=self.point_p2[1] and max(self.point_q1[1],self.point_q2[1])>=self.point_p2[1]):
                        final_cord_of_intersept.append(list(self.point_p1))
        
        return final_cord_of_intersept
    
    def checkIntersect(self):
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
                if list(intersect_point) not in final_cord:
                    final_cord.append(list(intersect_point))
                
        #For colliner
        if not corss_product_of_r_s and (not for_u): 
            t0 = np.dot((point_q2-point_p2),r) / (np.dot(r,r))
            t1 = t0 + (np.dot(s,r) / (np.dot(r,r)))
            
            #for colliner with overlapping
            if (0<=t0 and 1>=t0) or (0<=t1 and 1>= t1):
                # print('yes')
                if (min(point_p1[0],point_p2[0])<=point_q1[0] and max(point_p1[0],point_p2[0])>=point_q1[0]) and (min(point_p1[1],point_p2[1])<=point_q1[1] and max(point_p1[1],point_p2[1])>=point_q1[1]):
                    if list(point_q1) not in final_cord:
                        final_cord.append(list(point_q1))
                        
                if (min(point_p1[0],point_p2[0])<=point_q2[0] and max(point_p1[0],point_p2[0])>=point_q2[0]) and (min(point_p1[1],point_p2[1])<=point_q2[1] and max(point_p1[1],point_p2[1])>=point_q2[1]):
                    if list(point_q2) not in final_cord:
                        final_cord.append(list(point_q2))
                        
                if (min(point_q1[0],point_q2[0])<=point_p1[0] and max(point_q1[0],point_q2[0])>=point_p1[0]) and (min(point_q1[1],point_q2[1])<=point_p1[1] and max(point_q1[1],point_q2[1])>=point_p1[1]):
                    if list(point_p1) not in final_cord:
                        final_cord.append(list(point_p1))
                        
                if (min(point_q1[0],point_q2[0])<=point_p2[0] and max(point_q1[0],point_q2[0])>=point_p2[0]) and (min(point_q1[1],point_q2[1])<=point_p2[1] and max(point_q1[1],point_q2[1])>=point_p2[1]):
                    if list(point_p2) not in final_cord:
                        final_cord.append(list(point_p2))
    

import numpy as np

final_cord = []

# poly_1 = [[-10,30],[10,20],[13,18],[-20,10],[-10,30]]
# poly_2 = [[-20,30],[15,25],[15,15],[-5,20],[-20,30]]

poly_1 = [[-10,30],[10,20],[15,10],[-20,10],[-10,30]]
poly_2 = [[-20,25],[15,25],[15,15],[-20,20],[-20,25]]

#check poly_1 point inside poly_2--------------------------------------------------------------------------------------------
for cord_index_1 in range(0,len(poly_1)-1):
    flag_left = False
    flag_right = False
    point_p1 = np.array(poly_1[cord_index_1])
    for cord_index_2 in range(0,len(poly_2)-1):
        
        #right side pointing----------------------------------
        
        #adding end point of point_p1
        add_end_point = abs(poly_1[cord_index_1][0])
        point_p2 = np.array(poly_1[cord_index_1]) + np.array([add_end_point + (35*2),0])
        
        #for ploy_2 line point
        point_q1 = np.array(poly_2[cord_index_2])
        point_q2 = np.array(poly_2[cord_index_2+1])
        
        final_cord_of_intersept = []
        obj_of_FindIntersect = FindIntersect(point_p1,point_p2,point_q1,point_q2)
        Final_inside_point_of_poly_1 = obj_of_FindIntersect.checkInside()
        
        if len(Final_inside_point_of_poly_1):
            flag_right = True
        
        
        #left side pointing-----------------------------------

        #adding end point of point_p1
        add_end_point = -abs(poly_1[cord_index_1][0])
        
        point_p2 = np.array(poly_1[cord_index_1]) + np.array([add_end_point + (-(35*2)),0])
        
        #for ploy_2 line point
        point_q1 = np.array(poly_2[cord_index_2])
        point_q2 = np.array(poly_2[cord_index_2+1])
        
        final_cord_of_intersept = []
        obj_of_FindIntersect = FindIntersect(point_p1,point_p2,point_q1,point_q2)
        Final_inside_point_of_poly_1 = obj_of_FindIntersect.checkInside()
        
        if len(Final_inside_point_of_poly_1):
            flag_left = True
    
    if flag_right and flag_left:
        final_cord.append(list(point_p1))    




#check poly_2 point inside poly_1--------------------------------------------------------------------------------------------
for cord_index_1 in range(0,len(poly_2)-1):
    flag_left = False
    flag_right = False
    point_p1 = np.array(poly_2[cord_index_1])
    
    for cord_index_2 in range(0,len(poly_1)-1):
                
        #for right pointing-------------------------------------------
        
        #adding end point of point_p1
        add_end_point = abs(poly_2[cord_index_1][0])
        point_p2 = np.array(poly_2[cord_index_1]) + np.array([add_end_point + (35*2),0])
        
        #for ploy_2 line point
        point_q1 = np.array(poly_1[cord_index_2])
        point_q2 = np.array(poly_1[cord_index_2+1])
        
        final_cord_of_intersept = []
        obj_of_FindIntersect = FindIntersect(point_p1,point_p2,point_q1,point_q2)
        Final_inside_point_of_poly_2 = obj_of_FindIntersect.checkInside()
        
        if len(Final_inside_point_of_poly_2):
            flag_right = True
            
        #for left side pointing--------------------------------------------
        
        add_end_point = -abs(poly_2[cord_index_1][0])
        point_p2 = np.array(poly_2[cord_index_1]) + np.array([add_end_point + (-(35*2)),0])
        
        #for ploy_2 line point
        point_q1 = np.array(poly_1[cord_index_2])
        point_q2 = np.array(poly_1[cord_index_2+1])
        
        final_cord_of_intersept = []
        obj_of_FindIntersect = FindIntersect(point_p1,point_p2,point_q1,point_q2)
        Final_inside_point_of_poly_2 = obj_of_FindIntersect.checkInside()
        
        if len(Final_inside_point_of_poly_2):
            flag_left = True
        
    if flag_right and flag_left:
        final_cord.append(list(point_p1))     


#check point is intersect--------------------------------------------------------------------------------------------------
for ploy_1_index in range(0,len(poly_1)-1):
    for poly_2_index in range(0,len(poly_2)-1):

        #line segment 1
        point_p1 = np.array(poly_1[ploy_1_index])
        point_p2 = np.array(poly_1[ploy_1_index+1])
        
        #line segment 2
        point_q1 = np.array(poly_2[poly_2_index])
        point_q2 = np.array(poly_2[poly_2_index+1])
        
        obj_of_FindIntersect = FindIntersect(point_p1,point_p2,point_q1,point_q2)
        obj_of_FindIntersect.checkIntersect()
        


print(final_cord)

     
        