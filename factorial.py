factorial=1
number=int(raw_input())
if number<0:
    print "Factorial of a negative integer isn't yet possible"
    quit()
while(number>1):
    factorial*=number
    number-=1
print factorial
