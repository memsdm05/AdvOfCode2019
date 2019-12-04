import re

def main():
    start = 271973
    end = 785961
    c = 0
    # Part 1
    for pswd in range(start, end):
        s = [int(d) for d in str(pswd)]
        group = 1;
        isValid = False;
        lastDigit = 0;
        if (s[0]<=s[1]<=s[2]<=s[3]<=s[4]<=s[5]) and (s[0]==s[1] or s[1]==s[2] or s[2]==s[3] or s[3]==s[4] or s[4]==s[5]):
            for i in s:
                if i == lastDigit:
                    group+=1
                else:
                    if group == 2:
                        isValid=True
                    group = 1

                lastDigit = i

            if group == 2:
                isValid = True

            if isValid:
                c+= 1
                print(pswd)



    print(c)

if __name__ == '__main__':
    main()