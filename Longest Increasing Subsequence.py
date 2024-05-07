# nums = [1,2,4,3]
nums = [0,1,0,3,2,3]
lis = [1]* len(nums)
lis[len(nums)-1] = 1

for i in range(len(nums)-2, -1, -1):
    for k in range(i+1, len(nums)):
        if nums[i]< nums[k]:
            lis[i] = max(lis[i], lis[k]+1)


print(max(lis))