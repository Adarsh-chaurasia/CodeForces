def spy(arr,n):
    val=0
    if (arr[0] !=arr[1] and arr[0]==arr[2]) or (arr[0]==arr[1] and arr[0]!=arr[2]):
        val=arr[0]
    else:
        val=arr[1]
        j=0

    for i in range(n):
        if arr[i]!=val:
            j=i
    return j+1
        
def main():
    for _ in range(int(input())):
        n=int(input())
        Array=list(map(int,input().split()))
        result= spy(Array , n)
        print(result)

main()
    
