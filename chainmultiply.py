
def memorizer(func):
    result = {}
    def wrapper(*args):
        if args[1:] not in result:
            result[args[1:]] = func(*args)
        return result[args[1:]]

    return wrapper

@memorizer
def chainMult(m,s,e):
    if e-s<=1:
        return 0
    cost = float("inf")  
    for k in range(s+1,e):
        cost = min(cost,chainMult(m,s,k)+chainMult(m,k,e)+m[s]*m[k]*m[e])
    return cost

m = [2,3,40,5,2,3,4,5,6,188,99,198,12,3,4,67,82,123,45,12,46]
print(chainMult(m,0,len(m)-1))
