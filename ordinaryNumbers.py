import math
def solve(L, R):
  
    tmp = 0
    ans = 0

    n = int(math.log10(R) + 1)
  
    for i in range(n):
        tmp = tmp * 10 + 1
        for j in range(1, 10):
            if (1 <= (tmp * j) and (tmp * j) <= R):
                ans += 1
              
    return ans
    
def main():
    for _ in range(int(input())):
        n = int(input())
    
        res = solve(1,n)
        print(res)
    
if __name__ == '__main__':
    main()
