import json
import threading
from queue import Queue


# Task 1: JSON file parsing with separate threads

def parse_json_file(file_name):
    with open(file_name, 'r+') as file:
        data = json.load(file)
        print(f"Data from {file_name}: {json.dumps(data, indent=4)}")


# Define the list of JSON file names
json_files = ["file1.json", "file2.json", "file3.json"]

# Create a thread for each JSON file
threads = []
for file in json_files:
    thread = threading.Thread(target=parse_json_file, args=(file,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()


# Task 2: Function to process queue and print results

def process_queue(queue, name):
    while not queue.empty():
        value = queue.get()
        print(f"Stream: {name}, Value: {value}, Even: {value % 2 == 0}")


# Create a queue and fill it with numbers
number_queue = Queue()
for i in range(1, 11):
    number_queue.put(i)

# Create three threads to process the queue
threads = []
for i in range(3):
    thread = threading.Thread(target=process_queue, args=(number_queue, f"Stream {i+1}"))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All tasks are done.")
