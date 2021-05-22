def solve(arr):
    if len(arr)==1:
        return "YES"
        
    visited = [arr[0]]
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1] and arr[i] in visited:
            return "NO"
        if arr[i] not in visited:
            visited.append(arr[i])
            
    return "YES"
            
        

def main():
    for _ in range(int(input())):
        n = int(input())
        
        arr = input()
        
        ans = solve(arr)
        print(ans)

if __name__ == '__main__':
    main()
