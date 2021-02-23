a = ['Jan','Feb','March','April','May','June']
i = 0
print(a)
while i < len(a):
    print(a[i])
    i += 1
    if a[i] == "March":
        break
else:
    print('not found in list.')