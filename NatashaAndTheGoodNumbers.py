def solve(a,b):
    if b==1:
        print ("NO")
    else:
        print("YES")

        if b==2:
            print(a*1,a*3,a*b*2)
        else:
            print(a*1,a*(b-1),a*b)


solve(13,2)
