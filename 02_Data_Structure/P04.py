#  Find the intersection (common) of two sets and remove those elements from the first set.
# Sample: {23, 42, 65, 57, 78, 83, 29}
#         {57, 83, 29, 67, 73, 43, 48}
# Result: {57, 83, 29}, {65, 42, 78, 23}

set1 = {23, 42, 65, 57, 78, 83, 29}
set2 = {57, 83, 29, 67, 73, 43, 48}
print(set1 & set2,(set1 | set2) - (set2))
