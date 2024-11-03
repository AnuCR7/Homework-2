rows=int(input('Enter the number of rows: '))
column=int(input('Enter the number of columns: '))

matrix=[]
for r in range(rows):
    row=[]
    for c in range(column):
        element=int(input(f"enter element at ({r},{c}):"))
        row.append(element)
    matrix.append(row)
for i in matrix:
    print(i)

