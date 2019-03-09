import time
import random



while True:
	time.sleep(random.randint(1, 5))
	print('Go')
	start = time.time()
	x = input()
	print(time.time() - start)