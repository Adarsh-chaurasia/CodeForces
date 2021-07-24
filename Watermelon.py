#adarshChaurasia


def main():
    w=int(input())
    if w&1:
        print("NO")
    else:
        if w==2:
            print("NO")
        else:
            
            a=w-2
            if a&1:
                print("NO")
            else:
                print("YES")


main()
    
