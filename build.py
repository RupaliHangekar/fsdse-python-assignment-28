import collections
def solution(dic):
    l=[]
    dic = collections.OrderedDict(sorted(dic.items()))
    for key,value in dic.items():
        l.append(key)
    return l
print (solution({1: 10, 4: 40, 2: 20, 3: 30}))
