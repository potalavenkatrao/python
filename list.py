list1=['a','b','c']
list2=[1,2,3,4,5,6]
d={}
for i in range(len(list1)):
	d[list1[i]]=list2[i]
	if i == len(list1)-1:
		d[list1[i]]=list2[i:]
print(d)