def bubblesort(A):
    for i in range (len (A)):
        for k in range (len (A)-1,i,-1):
            if (A[k]< A[k-1]):
                swap (A,k,k-1)

def swap (A,x,y):
    A[x], A[y] = A[y], A[x]

count = int(input("Enter entries for sorting"))
sort_list = []
for i in range(count):
    sort_list.append(int(input("Enter No.")))
bubblesort(sort_list)
 
print(sort_list)
print(count)
