a=list(map(int,input().split(' ')))
a.sort()
d={}
for x in a: 
	if x not in d:
		d[x]=1
	else:
		d[x]+=1
for x in d:
	print(x,":",d[x])