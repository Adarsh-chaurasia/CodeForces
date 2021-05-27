
def main():
    t=int(input())
    while t:
        n=int(input())
        x=0
        while 1<<x <=n:
            x+=1
        x=x-1
        print((2**x)-1)
        t-=1

        




main()
