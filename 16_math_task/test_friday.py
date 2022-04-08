import math
import numpy as np

final_cord = [[10, 20], [0.0, 25.0], [12.307692307692308, 15.384615384615383], [-12.5, 25.0], [-15.333333333333332, 19.333333333333336]]

    
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