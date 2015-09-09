import random

def sort(x):
	index = 0
	while index+1 < len(x):
		if x[index] > x[index+1]:
			temp = x[index+1]
			x[index+1] = x[index]
			x[index] = temp
			index = 0
		else:
			index += 1
	print x

randoms=[]
for i in range(101):
	randoms.append(random.randrange(1,100000,1))
print randoms

sort(randoms)