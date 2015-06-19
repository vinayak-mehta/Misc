f = open('in.txt', 'r')
o = open('out.txt', 'w')

for i in f:
    o.write("%s" % i.split(':', 2)[2].lstrip())
