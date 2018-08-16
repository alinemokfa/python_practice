list = [2, 4, 6, 8, 10]
list2 = [12, 14, 16]
list3 = [1, 'hi', [3,4,5]]

print(len(list))

print(list[4])

print(list + list2)

print(list3[2][1])

print(list2)

# remove function removes the first occurence of a value (not index)
# if you know the index, use del
del(list[1])
