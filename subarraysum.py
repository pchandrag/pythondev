sum=[];
input_lists=[];
def read_input():
	f=open("inputs.txt","r");
	if (f.mode == "r"):
		contents=f.read();
	f.close();
	n = int(contents[0]);
	print n;
	for i in range(1,n):
		tmp=contents[i];
		print tmp;

#read input
#read_input();
sum=15;
test=[1,2,3,4,5,6,7,8,9,10];
size=len(test);
s=[0]*size;

print "test",test;
for i in range(0,size):
	print "at ... ",i,test[i];
	for j in range(0,i+1):
		s[j]+=test[i];
		print "sum ..",j,i,test[i],s[j];
		if (s[j] == sum):
			print "Found It!",j,i,":",test[j:i+1];
