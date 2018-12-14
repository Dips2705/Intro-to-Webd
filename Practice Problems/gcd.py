from math import *
def gcd(a,b):
	c=min(a,b)
	if(c==b):
		b=a
		a=c
	r=100
	while(r>0):
		r=b%a
		b=a
		a=r
	return b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=gcd(a,b)
print(c)