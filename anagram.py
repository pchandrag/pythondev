#read file
import random

loc='/usr/share/dict/words'
with open(loc) as f:
	content=f.read().split('\n')
	f.close()

l=len(content)
words=[]
for i in range(0,l):
	if '\'' in content[i] or len(content[i])<5:
		continue
	words.append(content[i])

words=words[1:]
d=len(words)
words=words[:d]

#shuffle the word
word=words[random.randint(0,d)]
shuffle=list(word)
random.shuffle(shuffle)

#print word;
print "The anagram is ",''.join(shuffle);

#set number of chances
if len(word)>7:
	chances=7
else:
	chances=5

tries=0
entry=''
hints=[];
while (tries<chances):
	print '\nWhat\'s your guess #',tries+1;
	entry = raw_input('-->');

	if (entry==word):
		print 'Congratulations!';
		break;

	#generate hints
	hints.append(random.randint(0,len(word)-1));
	hints.append(random.randint(0,len(word)-1));

	tries+=1;
	hint=""
	for i in range(0,len(word)):
		if i in hints:
			hint=hint+word[i]
		else:
			hint=hint+"_"
	print "Hint #%d is %s" % (tries,hint)

if tries==chances:
    print "Sorry, the answer was "+word
