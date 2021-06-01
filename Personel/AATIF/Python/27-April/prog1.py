import time 

def timing(fun) :
	def wrapper(*args, **kwargs) :
		print("stats")
		t1 = time.time()
		fun(*args, **kwargs)
		t2 = time.time()
		print("End")
		return str(t2-t1)
	return wrapper
@timing
def printf(s) :
	time.sleep(2)
	print(s)