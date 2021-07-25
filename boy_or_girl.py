def main():
    hashmap=dict()
    string=input()

    for each in string:
        if each in hashmap:
            hashmap[each]+=1
        else:
            hashmap[each]=1

    if len(hashmap)&1:
        print("IGNORE HIM!")
    else:
        print("CHAT WITH HER!")

main()
