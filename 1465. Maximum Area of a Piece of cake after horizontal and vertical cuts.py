# h = 5
# w = 4
# Hc = [3]
# Vc = [3]
h = 1000000000
w = 1000000000
Hc = [2]
Vc = [2]
Hc.sort()
Vc.sort()
Hc = [0]+Hc+[h]
Vc = [0]+Vc+[w]
print(Hc, Vc)
arr1 = []
for i in range(1,len(Hc)):
    val = abs(Hc[i] - Hc[i-1])
    arr1.append(val)
arr2  = []

for j in range(1, len(Vc)):
    v = abs(Vc[j] - Vc[j-1])
    arr2.append(v)
print(max(arr1) * max(arr2))
print(arr1)
print(arr2)
