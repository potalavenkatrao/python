import threading
import datetime
list1 = [1,2,3,4,5,6,7,8,9]
odd_list=[]
even_list=[]
def odd(list1):
	for i in list1:
		if (i%2)!=0:
			odd_list.append(i)

def even(list1):
	for i in list1:
		if (i%2)==0:
			even_list.append(i)

if __name__ == "__main__":
	begin_time = datetime.datetime.now()
	#odd(list1)
	#even(list1)
	t1 = threading.Thread(target=odd, args=[list1])
	t2 = threading.Thread(target=even, args=[list1])
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print("Done")
	execution_time = datetime.datetime.now()-begin_time
	print(execution_time)
