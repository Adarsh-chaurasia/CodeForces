#adarshChaurasia

def main():
    n=int(input())
    count=0
    while n:
        
        array=list(map(int,input().split()))
        x=array.count(1)
        if x>1:
            count+=1
        else:
            pass



        n-=1
    print(count)


main()
