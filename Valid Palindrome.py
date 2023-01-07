s = "A man, a plan, a canal: Panama"
s = s.lower()
s = s.replace(" ", "")
q = " "
# print(ord(,))
# w = ''.join(ch for ch in s if s.isalnum())
s = ''.join(filter(str.isalnum, s))
print(s)
# s = s.strip(",")
for i in range(len(s)-1, -1, -1):
    q += s[i]
print(q)
#
if s == q:
    print(True)
else:
    print(False)

