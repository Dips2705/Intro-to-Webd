s=input()
i=1
a=[]
c=1
while(i<len(s)):
	if s[i]==s[i-1]:
		c+=1
		i+=1
	else:
		a.append((c,int(s[i-1])))
		i+=1
		c+=1
a.append((c,int(s[i-1])))
for i in a:
	print(i,end=' ')