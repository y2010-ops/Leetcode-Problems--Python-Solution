text1 = "ezupkr"
text2 = "ubmrapg"
arr = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
print(arr)

for r in range(len(text1)-1, -1, -1):
    for c in range(len(text2)-1, -1, -1):
        if text1[r] == text2[c]:
            arr[r][c] = 1 + arr[r+1][c+1]
        else:
            arr[r][c] = max(arr[r+1][c], arr[r][c+1])
print(arr)
print(arr[0][0])

