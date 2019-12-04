import re

def main():
    start = 271973
    end = 785961
    c = 0
    # Part 1
    for pswd in range(start, end):
        s = [int(d) for d in str(pswd)]
        if (s[0]<=s[1]<=s[2]<=s[3]<=s[4]<=s[5]) and (s[0]==s[1] or s[1]==s[2] or s[2]==s[3] or s[3]==s[4] or s[4]==s[5]):
            c+=1
            print(pswd)
    print(c)

if __name__ == '__main__':
    main()