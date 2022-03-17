
for i in range(500):
	div=[]
	n=i+1
	for j in range(n):
		if (n)%(j+1)==0:
			div.append(j+1)
	if len(div) <= 2:
		if n in div:
			print(n)


