import collections 

node = collections.namedtuple('node','d r m')

a = []
a.append(node('b','c',150))
a.append(node('c','c',150))
a.append(node('d','d',100))
a.append(node('e','c',150))
a.append(node('f','c',150))

b = []
b.append(node('a','c',150))
b.append(node('c','c',150))
b.append(node('d','c',150))
b.append(node('e','c',150))
b.append(node('f','c',150))

c = []
c.append(node('a','a',150))
c.append(node('b','b',150))
c.append(node('d','d',60))
c.append(node('e','f',70))
c.append(node('f','f',70))

d = []
d.append(node('a','a',100))
d.append(node('b','c',60))
d.append(node('c','c',60))
d.append(node('e','e',75))
d.append(node('f','e',75))

e = []
e.append(node('a','d',75))
e.append(node('b','f',80))
e.append(node('c','f',80))
e.append(node('d','d',75))
e.append(node('f','f',80))

f = []
f.append(node('a','c',70))
f.append(node('b','c',70))
f.append(node('c','c',70))
f.append(node('d','e',80))
f.append(node('e','e',80))

print("Client 1-A\nClient 2-B\nClient 3-E\nClient 4-F\n")
src = int(input("Enter SRC: "))
dst = int(input("Enter DST: "))
seg = int(input("Enter SEG SIZE: "))

if src == 1:
	source = 'a'
elif src == 2:
	source = 'b'
elif src == 3:
	source = 'e'
elif src == 4:
	source = 'f'
else:
	print("ENTER VALID SOURCE")

if dst == 1:
    destn = 'a'
elif dst == 2:
    destn = 'b'
elif dst == 3:
    destn = 'e'
elif dst == 4:
    destn = 'f'
else:
    print("ENTER VALID DESTINATION")

mtu = seg
traversal = []
print("PREPARE AND READY FOR PACKET TRANSFER ###############")
traversal.append(source)

while source!=destn:
	
	if source == 'a':
		for i in range(0,5):
			if a[i].d == destn:
				index = i
		traversal.append(a[index].r)
		if a[index].m < mtu:
			mtu = a[index].m
		source = a[index].r


	elif source == 'b':
		for i in range(0,5):
			if b[i].d == destn:
				index = i
		traversal.append(b[index].r)
		if b[index].m < mtu:
			mtu = b[index]
		source = b[index].r


	elif source == 'c':
		for i in range(0,5):
			if c[i].d == destn:
				index = i
		traversal.append(c[index].r)
		if c[index].m < mtu:
			mtu = c[index]
		source = c[index].r


	elif source == 'd':
		for i in range(0,5):
			if d[i].d == destn:
				index = i 
		traversal.append(d[index].r)
		if d[index].m < mtu:
			mtu = d[index].m
		source = d[index].r


	elif source == 'e':
		for i in range(0,5):
			if e[i].d == destn:
				index = i
		traversal.append(e[index].r)
		if e[index].m < mtu:
			mtu = e[index].m
		source = e[index].r 


	elif source == 'f':
		for i in range(0,5):
			if f[i].d == destn:
				index = i
		traversal.append(f[index].r)
		if f[index].m < mtu:
			mtu = f[index].m
		source = f[index].r


mtu=mtu/8
mtu=mtu*8

segment = seg//mtu
total = segment*mtu

bal = seg-total

for i in range(1,segment+1):
	print(i,mtu)
if(bal!=0):
	print(i+1,bal)

print("ROUTE TAKEN: ",traversal)








