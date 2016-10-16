# -*- coding: UTF-8 -*-
#有些问题，没有0的概念，需要核对答案
def incrementString(text='AAAA'):
    arr = list(text.upper())
    l = len(arr)
    sum = 0
    res = []
    for i in range(l):
    	sum += (ord(arr[i]) - 65) * (26 ** (l - 1 - i))
    sum += 1
    c = sum
    while c != 0:  	
    	if c > 26:
            r = c % 26
            res.insert(0,r)
    	    c = c / 26
    	elif c == 26:
            res.insert(0,0)
            res.insert(0,1)
            break
    	else:
    		res.insert(0,c)
    		break
    res = map(lambda x: chr(x + 65), res)
    print res
    if len(res) > l: res[0] = 'A'
    return reduce(lambda x,y:x+y,res)

print incrementString('AAAA')



        