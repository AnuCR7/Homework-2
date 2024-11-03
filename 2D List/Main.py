list_54353=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(list_54353)
print(list_54353[1][1])

#no of rows
print(len(list_54353))

#no of columns
print(len(list_54353[0]))

#looping through values
for r in range(0,len(list_54353)):
    for c in range(0,len(list_54353[0])):
        print(list_54353[r][c],end=' ')
    print('\n')