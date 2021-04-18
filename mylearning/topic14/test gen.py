Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:30:23) [MSC v.1928 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> gen = (x**2 for x in range (1,20))
>>> gen
<generator object <genexpr> at 0x03E57C68>
>>> for item in gen:
	print(item)

	
1
4
9
16
25
36
49
64
81
100
121
144
169
196
225
256
289
324
361
>>> 