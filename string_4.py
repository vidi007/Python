#wap to get a string of first 2 nd last 2 chars from a given string
#if len<2 return message else if len=2 repeat it

a=input("enter a string")

if len(a)<2:
    print("too short")
elif len(a)==2:
    print(a*2)
else:
    print(a[:2]+a[len(a)-2:])
