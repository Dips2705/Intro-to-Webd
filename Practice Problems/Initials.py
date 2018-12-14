def first(s):
	return s[0]
def initial(s):
	a=list(s.split(' '))
	for i in range(len(a)):
		a[i]=first(a[i])
	return a
arr=[]
n=int(input("Enter no of test cases: "))
for i in range(n):
	arr.append(input())
for i in range(n):
	arr[i]=initial(arr[i])
	arr[i]="".join(arr[i])
	print(arr[i])