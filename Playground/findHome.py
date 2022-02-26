dictionary = [
                [0,1,0],
                [1,0,0],
                [1,1,0],
                [0,1,0],
                [0,1,1]
             ]

input = [0,1,2]

final_array = []

max_dist = 15

for k in range(len(dictionary)):
            dist_gym = 5
            dist_school = 5
            dist_store = 5

            for l in range(len(input)):
                count = 0
                count1 = 0
                
                for i in range(k,-1,-1):
                    if dictionary[i][input[l]] == 1 and input[l] == 0:
                        if count < dist_gym:
                            dist_gym = count
                    elif dictionary[i][input[l]] == 1 and input[l] == 1:
                        if count < dist_school:
                            dist_school = count
                    elif dictionary[i][input[l]] == 1 and input[l] == 2:
                        if count < dist_store:
                            dist_store = count
                    count+=1
                                    
                
                for j in range(k,len(dictionary)):
                    if dictionary[j][input[l]] == 1 and input[l] == 0:
                        if count1 < dist_gym:
                            dist_gym = count1
                    elif dictionary[j][input[l]] == 1 and input[l] == 1:
                        if count1 < dist_school:
                            dist_school = count1
                    elif dictionary[j][input[l]] == 1 and input[l] == 2:
                        if count1 < dist_store:
                            dist_store = count1
                    count1+=1
                    
            if dist_gym+dist_school+dist_store < max_dist:
                max_dist = dist_gym+dist_school+dist_store
                final_array=[]
                final_array.append(k+1)
            elif dist_gym+dist_school+dist_store == max_dist:
                max_dist = dist_gym+dist_school+dist_store
                final_array.append(k+1)
                
            # print('building number',k+1)   
            # print(dist_gym,dist_school,dist_store)
                
print(final_array)       



















      
                
# dist_gym = 5
# dist_school = 5
# dist_store = 5
# for l in range(len(input)):
#                 count = 0
#                 count1 = 0
                
#                 for i in range(0,-1,-1):
#                     if dictionary[i][input[l]] == 1 and input[l] == 0:
#                         if count < dist_gym:
#                             dist_gym = count
#                     elif dictionary[i][input[l]] == 1 and input[l] == 1:
#                         if count < dist_school:
#                             dist_school = count
#                     elif dictionary[i][input[l]] == 1 and input[l] == 2:
#                         if count < dist_store:
#                             dist_store = count
#                     count+=1
                                    
                
#                 for j in range(0,len(dictionary)):
#                     print(dictionary[j][l] == 1 and input[l] == 2,j,l,input[l] == 2)
#                     if dictionary[j][input[l]] == 1 and input[l] == 0:
#                         if count1 < dist_gym:
#                             dist_gym = count1
#                     elif dictionary[j][input[l]] == 1 and input[l] == 1:
#                         if count1 < dist_school:
#                             dist_school = count1
#                     elif dictionary[j][input[l]] == 1 and input[l] == 2:
#                         if count1 < dist_store:
#                             dist_store = count1
#                     count1+=1
                    
# if dist_gym+dist_school+dist_store < min_dist:
#     min_dist = dist_gym+dist_school+dist_store
#     final_array=[]
#     final_array.append(0+1)
# elif dist_gym+dist_school+dist_store == min_dist:
#     min_dist = dist_gym+dist_school+dist_store
#     final_array.append(0+1)
    
# print('building number',0+1)   
# print(dist_gym,dist_school,dist_store)     
                
                
                
                
                
                
                
                
                
                
                
                
                
            # count = 0
            # count1 = 0
            
            # for i in range(k,-1,-1):
            #     if dictionary[i][0] == 1:
            #         if count < dist_gym:
            #             dist_gym = count
            #     count+=1
                                
            
            # for j in range(k,len(dictionary)):
            #     if dictionary[j][0] == 1:
            #         if count1 < dist_gym:
            #             dist_gym = count1
            #     count1+=1



            # count = 0
            # count1 = 0

            # for i in range(k,-1,-1):
            #     if dictionary[i][1] == 1:
            #         if count < dist_school:
            #             dist_school = count
            #     count+=1
            
            # for j in range(k,len(dictionary)):
            #     if dictionary[j][1] == 1:
            #         if count1 < dist_school:
            #             dist_school = count1
            #     count1+=1
                    

            # count = 0
            # count1 = 0

            # for i in range(k,-1,-1):
            #     if dictionary[i][2] == 1:
            #         if count < dist_store:
            #             dist_store = count
            #     count+=1
            
            # for j in range(k,len(dictionary)):
            #     if dictionary[j][2] == 1:
            #         if count1 < dist_store:
            #             dist_store = count1
            #     count1+=1
                 
            # print('building number',k+1)   
            # print(dist_gym,dist_school,dist_store)








# for k in range(len(dictionary)):
#             dist_gym = 5
#             dist_school = 5
#             dist_store = 5

#             count = 0
#             count1 = 0
            
#             for i in range(k,-1,-1):
#                 if dictionary[i][0] == 1:
#                     if count < dist_gym:
#                         dist_gym = count
#                 count+=1
                                
            
#             for j in range(k,len(dictionary)):
#                 if dictionary[j][0] == 1:
#                     if count1 < dist_gym:
#                         dist_gym = count1
#                 count1+=1



#             count = 0
#             count1 = 0

#             for i in range(k,-1,-1):
#                 if dictionary[i][1] == 1:
#                     if count < dist_school:
#                         dist_school = count
#                 count+=1
            
#             for j in range(k,len(dictionary)):
#                 if dictionary[j][1] == 1:
#                     if count1 < dist_school:
#                         dist_school = count1
#                 count1+=1
                    

#             count = 0
#             count1 = 0

#             for i in range(k,-1,-1):
#                 if dictionary[i][2] == 1:
#                     if count < dist_store:
#                         dist_store = count
#                 count+=1
            
#             for j in range(k,len(dictionary)):
#                 if dictionary[j][2] == 1:
#                     if count1 < dist_store:
#                         dist_store = count1
#                 count1+=1
                 
#             print('building number',k+1)   
#             print(dist_gym,dist_school,dist_store)
            
    
    
    
            
            
            
            
            
            
            
            
            
            
# if dictionary[i][j] == 1 and input[j]==0:
#                 print('gym',dictionary[i],i+1,input[j])
#             elif dictionary[i][j] == 1 and input[j]==1:
#                  print('school',dictionary[i],i+1,input[j])
#             elif dictionary[i][j] == 1 and input[j]==2:
#                  print('store',dictionary[i],i+1,input[j])     
            
                
                
            
            
            
            
        


    
        
        
        
    
        
    
    
    

        
    
    
    
    