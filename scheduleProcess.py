import random
import time

class scheduleProcess:
    def __init__(self, process_id):
        self.process_id = process_id
        
def schedule():
    #RANDOMLY CREATE AT LEAST 5 PROCESSES
    #store processes in array
    process = []
    #number of processes ran are random between 5 and 15
    num_process = random.randint(5,15)
    for process_id in range(num_process):
        p = scheduleProcess(process_id)
        #each process creates a random number of threads (between 3 and 40)
        p.num_threads = random.randint(3,40)
        process.append(p)
        #print the ID of the process and num of threads each process created 
        print(f"Process id: {process_id} and number of threads: {p.num_threads}")
    #randomly terminate processes 
    if process: 
        terminate = random.choice(process)
        process.remove(terminate)
        print(f"Terminating Process id: {terminate.process_id}")
    #run program for 10 mins
    duration = 600
    start_time = time.time()
    end_time = start_time + duration
    while time.time() < end_time:
        #randomly create process
        random_process = random.choice([True, False])
        if random_process:
            new_process = scheduleProcess(len(process))
            new_process.num_threads= random.randint(3,40)
            process.append(new_process)
            print(f"New process id: {new_process.process_id} and number of threads: {new_process.num_threads}")
        #randomly terminate process
        if process: 
            terminate = random.choice(process)
            process.remove(terminate)
            print(f"Terminating Process id: {terminate.process_id}")
        time.sleep(5)
    print(process)
if __name__ == "__main__":
    schedule()


class CPU:
    def __init__(self, process_id):
        self.process_id = process_id