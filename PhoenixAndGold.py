def solveWeight(arr,val):
    a1=[]
    a1.append(max(arr))
    arr.remove(max(arr))
    print(arr)
    for i in range(len(arr)-1):
        a1[i+1]=a1[i]+arr[i]

    if val not in a1:
        return 1,a1
    else:
        return 0,a1
    
    
    


if __name__=="__main__":

    n= int(input())
    for _ in range(n):
        size,e_value= map(int,input().split())
        arr1=list(map(int,input().split()))
        result,array=solveWeight(arr1,e_value)
        if result:
            print("YES")
            print(*array)
        else:
            print("NO")
