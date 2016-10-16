# -*- coding: UTF-8 -*-
def leapyears(yearlist):
	for i in yearlist:
		if (i % 400 == 0) or (i % 4 == 0 and i % 100 != 0):
			yield i
gen = leapyears([1600, 1604, 1700, 1704, 1800, 1900, 1996, 2000, 2004])