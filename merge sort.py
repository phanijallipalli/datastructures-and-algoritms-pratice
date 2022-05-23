def merge(A,B):
    (m,n) = (len(A),len(B))
    (c,i,j) = ([],0,0)
    while i<m and j<n:
        if A[i] < B[j]:
            c.append(A[i])
            i+=1
        else:
            c.append(B[j])
            j+=1
    while i < m :
        c.append(A[i])
        i += 1

    while j<n:
        c.append(B[j])
        j += 1
    return c

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        l = mergesort(arr[:mid])
        m = mergesort(arr[mid:])
        b = merge(l,m)
        return b
    return arr

print(mergesort([1,5,8,7,9,21,56,14]))





