def main():
    k,n,w=map(int,input().split())

    total=(w*(w+1))//2

    totalCost=k*total

    if n>=totalCost:
        print(0)
    else:
        money=totalCost-n


        print(money)


main()
