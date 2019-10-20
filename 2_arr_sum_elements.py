#comprehention to find pair with given sum of 2 arrays

#123456, 4-567 disp pairs sum n

a1=[1,2,3,4,5,6]
a2=[4,-5,6,7,3]

n=int(input("enter num"))

for i in range(1,len(a1)):
    for j in range(1,len(a2)):
        if a1[i]+a2[j]==n:
            print(a1[i],",",a2[j])
