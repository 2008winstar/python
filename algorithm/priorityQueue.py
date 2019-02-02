from queue import PriorityQueue

priority_queue = PriorityQueue()
priority_queue.put((10, "Issue 1: Medium Priority"))
priority_queue.put((5, "Issue 2: Low Priority"))
priority_queue.put((25, "Issue 3: High Priority"))
priority_queue.put((50, "Issue 4: Very High Priority"))

while not priority_queue.empty():
    (priority, value) = priority_queue.get()
    print("{} Priority, {} Value".format(priority, value))

