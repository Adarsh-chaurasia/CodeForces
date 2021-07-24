#adarshChaurasia

def main():
    n=int(input())
    while n:
        string=input()
        x=len(string)
        if x<11:
            print(string)
        else:

            s=" "
            s+=string[0]
            count=x-2
            s+=str(count)
            s+=string[x-1]

            print(s)
            






        n-=1

main()
