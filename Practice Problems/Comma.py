def commas(s):
	a=[]
	for i in range(len(s)):
		a.append(s[i])
	for i in range(len(s),0,-3):
		if(i!=len(s)):
			a.insert(i,',')
	return a
x=[]
n=int(input("Enter the no of test cases: "))
for i in range(n):
	x.append(input())
for i in range(n):
	x[i]=commas(x[i])
	x[i]="".join(x[i])
	print(x[i])


