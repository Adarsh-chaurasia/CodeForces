#Adi_2810
import math
for _ in range(int(input())):
    n = int(input())
    t = n/2
    d = n/4
    if math.ceil(math.sqrt(t)) == math.floor(math.sqrt(t)) or math.ceil(math.sqrt(d)) == math.floor(math.sqrt(d)):
        print("YES")
    else:
        print("NO")
