# reference - https://stackoverflow.com/questions/563198/how-do-you-detect-where-two-line-segments-intersect


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
    
    
class find_end_point_form_x():

    def __init__(self,poly_1,poly_2):
        self.poly_1 = poly_1
        self.poly_2 = poly_2
        
    def find_end_point_of_inside_point(self):
        max_x = 0
        for cord_index_1 in range(0,len(self.poly_1)-1):
            for cord_index_2 in range(cord_index_1+1,len(self.poly_1)-1):
                #print(abs(poly_1[cord_index_1][0] - poly_1[cord_index_2][0]))
                distance_of_abs_x_point = abs(self.poly_1[cord_index_1][0] - self.poly_1[cord_index_2][0])
                if max_x < distance_of_abs_x_point:
                    max_x = distance_of_abs_x_point
            
        for cord_index_1 in range(0,len(self.poly_2)-1):
            for cord_index_2 in range(cord_index_1+1,len(self.poly_2)-1):
                #print(abs(poly_2[cord_index_1][0] - poly_2[cord_index_2][0]))
                distance_of_abs_x_point = abs(self.poly_2[cord_index_1][0] - self.poly_2[cord_index_2][0])
                if max_x < distance_of_abs_x_point:
                    max_x = distance_of_abs_x_point
        
        return max_x
        
import math
import numpy as np

final_cord = []

# poly_1 = [[-10,30],[10,20],[13,18],[-20,10],[-10,30]]
# poly_2 = [[-20,30],[15,25],[15,15],[-5,20],[-20,30]]

poly_1 = [[-10,30],[10,20],[15,10],[-20,10],[-10,30]]
poly_2 = [[-20,25],[15,25],[15,15],[-20,20],[-20,25]]


#find end point of point
obj_of_find_end_point = find_end_point_form_x(poly_1,poly_2)
max_x = obj_of_find_end_point.find_end_point_of_inside_point()

#check poly_1 point inside poly_2--------------------------------------------------------------------------------------------
for cord_index_1 in range(0,len(poly_1)-1):
    flag_left = False
    flag_right = False
    point_p1 = np.array(poly_1[cord_index_1])
    for cord_index_2 in range(0,len(poly_2)-1):
        
        #right side pointing----------------------------------
        
        #adding end point of point_p1
        add_end_point = abs(poly_1[cord_index_1][0])
        point_p2 = np.array(poly_1[cord_index_1]) + np.array([add_end_point + (max_x*2),0])
        
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
        
        point_p2 = np.array(poly_1[cord_index_1]) + np.array([add_end_point + (-(max_x*2)),0])
        
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
        point_p2 = np.array(poly_2[cord_index_1]) + np.array([add_end_point + (max_x*2),0])
        
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
        point_p2 = np.array(poly_2[cord_index_1]) + np.array([add_end_point + (-(max_x*2)),0])
        
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

     
max_y = final_cord[0][1]
bottom_max = final_cord[0]

for cord in final_cord:
    if max_y > cord[1]:
        bottom_max = cord   
        max_y = cord[1]
    elif max_y == cord[1] and bottom_max[0] > cord[0]:
        bottom_max = cord
        
# print(bottom_max)
final_cord.remove(bottom_max)

arranged_coordinates= []
angle_with_respect_to_cord = []
for cord in final_cord:
        angle = math.degrees(math.atan2((cord[1]-bottom_max[1]),(cord[0]-bottom_max[0])));
        # print(angle,cord,(bottom_max[1]-cord[1]),(bottom_max[0]-cord[0]))
        arranged_coordinates.append(cord)
        angle_with_respect_to_cord.append(angle)
        
        
# print(angle_with_respect_to_cord,arranged_coordinates)


for index,angle in enumerate(angle_with_respect_to_cord):
    for index_1,angle_1 in enumerate(angle_with_respect_to_cord):
        if(angle<=angle_1):
                if(angle<angle_1):
                    arranged_coordinates[index],arranged_coordinates[index_1] = arranged_coordinates[index_1],arranged_coordinates[index]
                    angle_with_respect_to_cord[index],angle_with_respect_to_cord[index_1] = angle_with_respect_to_cord[index_1],angle_with_respect_to_cord[index]
                elif(angle==angle_1 and angle_1 == float(0) and arranged_coordinates[index][0]<arranged_coordinates[index_1][0]):
                    arranged_coordinates[index],arranged_coordinates[index_1] = arranged_coordinates[index_1],arranged_coordinates[index]
                    angle_with_respect_to_cord[index],angle_with_respect_to_cord[index_1] = angle_with_respect_to_cord[index_1],angle_with_respect_to_cord[index]
                elif(angle==angle_1 and angle_1 == float(90) and arranged_coordinates[index][1]>arranged_coordinates[index_1][1]):
                    arranged_coordinates[index],arranged_coordinates[index_1] = arranged_coordinates[index_1],arranged_coordinates[index]
                    angle_with_respect_to_cord[index],angle_with_respect_to_cord[index_1] = angle_with_respect_to_cord[index_1],angle_with_respect_to_cord[index]       
      
arranged_coordinates.insert(0,bottom_max)   
arranged_coordinates.append(arranged_coordinates[0])   
print(arranged_coordinates)


#find area
area_of_overlapping_polygon = 0
for cord_index in range(0,len(arranged_coordinates)-1):
    area_of_overlapping_polygon += np.linalg.det(np.array([arranged_coordinates[cord_index],arranged_coordinates[cord_index+1]]))
    
print(area_of_overlapping_polygon/2)