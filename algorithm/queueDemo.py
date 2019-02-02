import queue
my_queue = queue.Queue()
my_queue.put('first')
my_queue.put(2)
my_queue.put('third')
print(my_queue.get())
print(my_queue.get())
print(my_queue.get())
