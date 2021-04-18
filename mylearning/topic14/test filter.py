Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:30:23) [MSC v.1928 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [-1,-2,-3,-4,-5,-6,-7,-8,-9,10]
>>> def pos(number):
	return number>0

>>> filter(pos,a)
<filter object at 0x04301FD0>
>>> for i in filter(pos,a):
	print(i,(", ",end = '')
	      
SyntaxError: invalid syntax
>>> for i in filter(pos,a):
	print(i,", ",end = '')

	
10 , 
>>> 