def solve(a,b):
    if a==b:
        print(1)
        return
    else:
        count=0
        while a<=b:
            count+=1
            a=a*3
            b=b*2


        print(count)

    return
def main():
    bear,bob=map(int,input().split())

    solve(bear,bob)

main()
