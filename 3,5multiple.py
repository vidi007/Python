#itrates 1 too 50 for multiples of 3, print "fiss" instrad of no, for multiples of 5, print "buzz", for both, "fiss buzz"

for i in range(1,50):
    if i%3==0 and i%5==0:
        print(i," fiss buzz")
    elif i%3==0:
        print(i," fiss")
    elif i%5==0:
        print(i," buzz")
