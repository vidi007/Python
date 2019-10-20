Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def h():
	print("hello")

>>> h()
hello
>>> h
<function h at 0x00000190B76BC1E0>
>>> def j():
	print("hello")
	return

>>> j()
hello
>>> def hh():
	print("hello")
	x=1
	return x

>>> p=hh()
hello
>>> p
1
>>> o=h()
hello
>>> o
>>> print(o)
None
>>> #if no return in function, it returns none
>>> def hh():
	print("hello")
	x=1
	y=2
	return x
	return y

>>> hh()
hello
1
>>> t=hh()
hello
>>> t
1
>>> def g(i):
	if i>5:
		print("greater")
	else:
		print("less")

>>> s=input()

>>> g(6)
greater
>>> g(2)
less
>>> g(input())
9
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    g(input())
  File "<pyshell#31>", line 2, in g
    if i>5:
TypeError: '>' not supported between instances of 'str' and 'int'
>>> g(int(input()))
