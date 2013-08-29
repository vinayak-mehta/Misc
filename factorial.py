factorial=1
number=int(raw_input())
if number<0:
    print "Factorials of negative integers isn't ye possible"
    quit()
while(number>1):
    factorial*=number
    number-=1
print factorial
