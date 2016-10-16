# -*- coding: UTF-8 -*-
def integer(number):
	try:
		return int(float(number))
	except ValueError:
		return 0

print integer(4.5),integer(32),integer('23'),integer('-15.1'),integer('str')