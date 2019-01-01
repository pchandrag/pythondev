a = 2
n = -3

def power(x,y):
	if (y==0):
		return 1;
	elif (y==1):
		return x;
	elif (y<0):
		return 1/power(x,-y);
	else:
		return power(x,y/2)*power(x, (y-y/2));
print a**n

#print power(a,n)
