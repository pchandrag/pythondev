a = 2
n = 10000

def power(x,y):
	if (y==0):
		return 1;
	elif (y==1):
		return x;
	else:
		return power(x,y/2)*power(x, (y-y/2));
print a**n

#print power(a,n)
