# -*- coding: UTF-8 -*-
one =  [9, 36, 16, 25, 4, 1]
two = dict(india=9, golf=17, juliet=5, foxtrot=61, hotel=8)
three = {11:'lima', 13:'kilo', 12:'mike'}
def print_func(w):
	try:
	    print len(w), max(w), min(w), sum(w)
	except:
		print 'error'

print_func(one)
print_func(two)
print_func(three)
#实验得出，dict没有sum函数，max，min都是指键值