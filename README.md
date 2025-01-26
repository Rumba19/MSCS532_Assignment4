# Heapsort and Priority Queue Implementation


## **Overview**
This project is part of the MSCS532 course assignment to analyze and compare the efficiency and scalability of two algorithms:
1. **Heapsort Algorithm**: A sorting algorithm based on a binary heap data structure.
2. **Priority Queue Implementation**: A data structure that allows for efficient management of tasks based on priority.

**Heapsort**:
- Sorts an array in ascending order
- Utilizies a max-heap repeatedly to extract the maximum element from the heap.

**Priority**:
Supports operations to manage tasks with different priorities.

- Insert(task): Adds a new task while maintaining the heap property.

- Extract-Max: Removes and returns the task with the highest priority.

- Change Priority: Updates the priority of an existing task and repositions it in the heap.


---

### **Prerequisites to run the script**
1. **Python**: Ensure Python 3.x is installed. You can download it from [python.org](https://www.python.org/).
2. **Install Dependencies**: Run the following command to install the required library (`numpy`):
   ```bash
   pip3 install numpy

## **How to Run*
  ```bash
git clone https://github.com/Rumba19/MSCS532_Assignment4
cd MSCS532_ASSIGNMENT4
python3 heapsort.py
python3 priority_queue.py