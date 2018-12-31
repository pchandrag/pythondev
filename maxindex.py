test=[3,5,4,2];
size=len(test);
max = 0;

print "test",test;
for i in range(0,size):
	for j in range(i+1,size):
		print "comparing ..",test[i],test[size-j];
		if ((test[i]<=test[size-j]) and (max<=(size-j+i))):
			max=size-j+i;
			print "Updating max to ",max,test[i],test[size-j];
print max;
