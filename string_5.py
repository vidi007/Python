#wap to geta a string from 2 given strings seperated bty a space and swap the
# first 2 chars of the string eg. abc xyz -> xyc_abz

a=input("enter string 1")
b=input("enter string 2")

c=a[:2]
d=b[:2]

a=a.replace(c,d,1)
b=b.replace(d,c,1)

print(a+"_"+b)





























"""

c=a[:2]+b[2:]
d=b[:2]+a[2:]

print(c,d)

"""
