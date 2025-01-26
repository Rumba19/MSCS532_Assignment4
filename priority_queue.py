class Task:
    #Represents a task with an ID, priority, arrival time, and deadline.

    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __repr__(self):
        return f"Task(ID={self.task_id}, Priority={self.priority})"

class PriorityQueue:

    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0


    # Insert a task while maintaining the heap property
    def insert(self, task):
        self.heap.append(task)
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index].priority > self.heap[parent].priority:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def extract_max(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")

        # Swap root with the last element
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max_task = self.heap.pop()
        self._sift_down(0)
        return max_task
    
    def _sift_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left].priority > self.heap[largest].priority:
            largest = left

        if right < len(self.heap) and self.heap[right].priority > self.heap[largest].priority:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._sift_down(largest)

    # Increase or decrease the priority of a task and adjust its position
    def change_priority(self, index, new_priority):
        old_priority = self.heap[index].priority
        self.heap[index].priority = new_priority

        if new_priority > old_priority:
            self._sift_up(index)
        else:
            self._sift_down(index)

  #invoke priority queue instance s
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert(Task(3, 10, "10:00", "12:00"))
    pq.insert(Task(2, 10, "10:05", "12:30"))
    pq.insert(Task(5, 8, "10:10", "13:00"))
   
    print("Tasks in priority queue:", pq.heap)
    print("Extracted max:", pq.extract_max())
    print("Remaining tasks:", pq.heap)
