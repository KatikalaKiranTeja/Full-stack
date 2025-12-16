password="Kiran"
attempts=["kir","kiraan","Kiran"]
max_attemps=3
access_granted=False
for i in range(max_attemps):
    if attempts[i]==password:
        access_granted=True
        print("Access granted")
        break
if not access_granted:
    print("Too many attempts try again later")




dict={"name":"Sravan","age":45,"addr":"jeedimetla"}
swap_dict={value: keys for keys,value in dict.items() }
print(swap_dict)


num=[1,2,3,4,5,6,7,8]
chunk_size=2
chunks=[]
for i in range(0,len(num),chunk_size):
    chunks.append(num[i:i + chunk_size])
print(chunks)

def diagonal_sums(matrix):
    n=len(matrix)
    first_diag=0
    second_diag=0
    for i in range(n):
        first_diag += matrix[i][i]
        second_diag +=matrix[i][n-1-i]
    total = first_diag + second_diag
    return total
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(diagonal_sums(matrix))





