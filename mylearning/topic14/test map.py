Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:30:23) [MSC v.1928 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> v_new = [-1,-2,-3,-4,-5,-6,-7]
>>> v_map = map(abs,v_new)
>>> v_map
<map object at 0x031D1418>
>>> for item in v_amp:
	print(item,end = '')

	
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    for item in v_amp:
NameError: name 'v_amp' is not defined
>>> for item in v_map:
	print(item,end = '')

	
1234567
>>> 