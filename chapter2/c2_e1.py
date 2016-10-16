# -*- coding: UTF-8 -*-
def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
	res = ''
	for i in text:
		if i in chars:
			res += i
	return res

print valid('Barking!')
print valid('KL754', '0123456789')
print valid('BEAN', 'abcdefghijklmnopqrstuvwxyz')
