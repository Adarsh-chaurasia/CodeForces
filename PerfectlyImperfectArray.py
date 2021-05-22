import math
def solve(arr):
    for i in arr:
        a=i**0.5
        if math.ceil(a)!=math.floor(a):
            print("YES")
            return
    print("NO")


for _ in range(int(input())):
    n =int(input())

    a1=list(map(int,input().split()))

    solve(a1)
    
