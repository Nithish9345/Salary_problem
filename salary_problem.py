def salary(n):
    s = 0
    if(sum(n) > 40):
        s += (sum(n)-40) * 25
    for i in range(7):
        if i == 0:
            s += (n[i]*100) + ((n[i]*100)//2)
            if(n[i] > 8):
                s+= (n[i]-8)*15
        elif i == 6:
            s += ((n[i]*100) + ((n[i]*100)//4))
            if(n[i] > 8):
                s+= (n[i]-8)*15
        else:
            s += n[i]*100
            if (n[i] > 8):
                s += (n[i] - 8) * 15


    return s

n = list(map(int, input().split()))
print(salary(n))

