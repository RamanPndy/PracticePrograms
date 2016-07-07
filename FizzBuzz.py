N = int(input())
lst = []
for i in range(0,N):
    lst.append(i+1)
for j in lst:
    if j%15 == 0:
        print "FizzBuzz"
    elif j%3 == 0:
        print "Fizz"
    elif j%5 == 0:
        print "Buzz"

    else:
        print j