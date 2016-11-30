def memorizer(func):
    memo={}
    def wrapper(*args):
        if args[1] in memo:
            return memo[args[1]]
        memo[args[1]] = func(*args)
        return memo[args[1]]

    return wrapper



@memorizer
def rodcutting(p,n,s):
    if n==0:
        return 0,0 
    val = p[n-1]
    s0 = n
    for i in range(1,n):
        # val = max(val,p[i-1]+rodcutting(p,n-i))
        val1,s1 = rodcutting(p,n-i,s)
        val1 += p[i-1]
        if val < val1:
            val = val1
            s0 = s1

    s[n] = s0
    return val,s0


def constructcutting(s,n):
    l=[]
    while n!=0:
       l.append(s[n]) 
       n = n-s[n]
    return l
p=[1, 5, 8, 9, 10, 17, 17, 20, 24, 30,34,49,78,99,102,103,120,154,165,178,190,193,234,289,356]

s={}
r,_ = rodcutting(p,5,s)
print(r)
l = constructcutting(s,5)

print(l[::-1])
