matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
visited = []
left, right = 0, len(matrix[0])
top, bottom = 0, len(matrix)

while top< bottom and left< right:
    for i in range(left, right):
        visited.append(matrix[top][i])
    top += 1

    for i in range(top, bottom):
        visited.append(matrix[i][right-1])
    right -= 1

    if not (left< right and top < bottom) :
        break
        
    for i in range(right-1, left-1, -1):
        visited.append(matrix[bottom-1][i])
    bottom -= 1

    for i in range(bottom-1, top-1, -1):
        visited.append(matrix[i][left])
    left += 1





# i = 0
# j = 0
# while i < len(matrix):
#     if matrix[i][j] not in visited:
#         visited.append(matrix[i][j])
#         if matrix[i][j] == matrix[i][-1]:
#             i += 1
#         else:
#             j += 1
#     else:
#         i += 1
#         j += 1
#
# # k = len(matrix)-1
# s = 0
# while s < len(matrix):
#     if visited[-1] == matrix[s][-1]:
#         for x in range(len(matrix[s])-1, -1, -1):
#             if matrix[s][x] not in visited:
#                 visited.append(matrix[s][x])
#     else:
#         s += 1
#
# z= len(matrix)-1
# while z < len(matrix):
#     if visited[-1] == matrix[z][0]:
#         for p in range(len(matrix)-1, -1, -1):
#             if matrix[p][0] not in visited:
#                 visited.append(matrix[p][0])
#     else:
#         z += 1








    # if matrix[i][j] == mar
    # j+= 1
    # i += 1
print(visited)