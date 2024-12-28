# Threads: The code creates multiple threads, each running a separate instance of the task function. Threads allow the program to run multiple tasks concurrently, which means that while one task is sleeping (simulating work), another task can be running at the same time.

# Types of concurrency being used here:

# Multithreading: The program runs tasks in parallel using multiple threads. Each thread executes the task function independently.
# Cooperative Concurrency: Each thread "cooperates" by yielding control when it sleeps (i.e., calls time.sleep). While one thread is sleeping, others can run.

import threading
import time

# Function to simulate a task
def task(name, delay):
    print(f"Task {name} started")
    time.sleep(delay)  # Simulating work by sleeping for 'delay' seconds
    print(f"Task {name} completed after {delay} seconds")

# Main function to manage concurrency
def main():
    # Creating threads to run tasks concurrently
    thread1 = threading.Thread(target=task, args=("A", 2))
    thread2 = threading.Thread(target=task, args=("B", 3))
    thread3 = threading.Thread(target=task, args=("C", 1))

    # Starting all threads
    thread1.start()
    thread2.start()
    thread3.start()

    # Wait for all threads to complete
    thread1.join()
    thread2.join()
    thread3.join()

    print("All tasks are completed.")

# Run the main function
if __name__ == "__main__":
    main()
