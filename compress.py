from itertools import groupby
loop = int(input())
for i in range(loop):
    input_val = input()
    b = input_val
    if any(char.isdigit() for char in input_val):
        j = 0
        s = ""
        while True:
            if b[j].isdigit():
                if j+1 != len(b)-1:
                    if b[j+1].isdigit():
                        s += b[j+2]*(int(b[j:j+2]))
                        j = j+3
                    else:
                        s+= b[j+1]*(int(b[j:j+1]))
                        j = j+2
                else:
                    s+= b[j+1]*(int(b[j:j+1]))
                    j = j+2
            else:
                s+=b[j]
                j = j+1
            if j == len(b):
                break
        print(s)
    else:
        c = groupby(input_val)
        s =""
        for j,k in c:
            m = list(k)
            if len(m) == 1:
                s+=j
            else:
                s+="{}".format(len(m))
                s+=j
        print(s)
