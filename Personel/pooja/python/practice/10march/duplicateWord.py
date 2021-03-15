

# Initializing list
test_list = ['pooja,my,pooja', 'I, am, I', 'two, two, three']

# printing original list
print("The original list is : " + str(test_list))

# Remove duplicate words from Strings<code></code> in List
# using loop + set() + split()
res = []
for strs in test_list:
    res.append(set(strs.split(", ")))

# printing result
print("The list after duplicate words removal is : " + str(res))
