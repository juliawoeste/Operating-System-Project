#class definition
import random
import time
import numpy as np
from thread import Thread
class Process: 
    #constuctor function
    def __init__(self, thread, state = "", input = "", output = "", priority = "", memory = []):
        self.thread = thread
        self.state = state
        self.input = input
        self.output = output
        self.priority = priority
        self.memory = memory
    
    def __str__(self):
        return f"Thread: {self.thread}\nState: {self.state}\nInput: {self.input}\nOutput: {self.output}\nPriority: {self.priority}\nMemory: {self.memory}"
class scheduleProcess: 
    def __init__(self, process_id):
        self.process_id = process_id
      
#CREATE CPU OBJECT WITH 1 ATTRIBUTE  
class CPU: 
    def __init__(self):
        self.cpu_process_id = None

#CREATE SCHEDULING ALGORITHM 
def round_robin(cpu, process):
    #checks if the length of the process is 0, then does nothing
    if len(process) == 0:
        pass
    #round robin needs a quantum (block of time given to each process)
    quantum = 3
    time.sleep(quantum)
    #gets current id from the cpu 
    current_process_id = cpu.cpu_process_id
    #gets the current and next process from process array with the process id
    current_process = next_process = process[current_process_id]
    #checks if the process and process if is not empty
    if process and current_process_id is not None: 
            #sets the current id state to running 
            #CHANGE STATE OF PROCESS TO RUNNING
            current_process.state = "Running"
            print(f"Process ID: {cpu.cpu_process_id} is Running")
            #update cpu process id (adding by 1 and goes back to beginning if goes past the length of the process array)
            #SWITCH PROCESSES
            cpu.cpu_process_id = (cpu.cpu_process_id + 1) if current_process_id + 1 < len(process) else 0
            #sets next process to ready
            #CHANGE THE STATE 
            next_process = process[cpu.cpu_process_id]
            next_process.state = "Ready"
            print(f"Process ID: {cpu.cpu_process_id} is Ready")

def schedule():
    cpu = CPU()
    cpu.cpu_process_id = 0
    #RANDOMLY CREATE AT LEAST 5 PROCESSES
    #store processes in array
    process = []
    #number of processes ran are random between 5 and 20
    num_process = random.randint(5,20)
    for process_id in range(num_process):
        #create an instance of schedule process and pass in process id
        p = scheduleProcess(process_id)
        #EACH PROCESS CREATES A RANDOM NUMBER OF THREADS (BETWEEN 3 AND 40)
        p.num_threads = random.randint(3,40)
        process.append(p)
        #PRINT THE ID OF THE PROCESS AND NUMBER OF THREADS EACH PROCESS CREATED
        print(f"Process ID: {p.process_id} and Number of Threads: {p.num_threads}")
    
    #RANDOMLY TERMINATE PROCESS
    if process: 
        #randomly selects a process from the process array
        terminate = np.random.choice(process)
        while terminate not in process: 
            terminate = np.random.choice(process)
            #removes the process from the array 
            process.remove(terminate)
            print(f"Terminating Process ID: {terminate.process_id}")
    #RUN PROGRAM FOR 10 MINUTES
    duration = 600 #since time.time() gets the time in seconds, 600 seconds is 10 minutes
    start_time = time.time()
    end_time = start_time + duration
    #while the start time is less than or equal to 10 minutes, run through the while loop
    while time.time() <= end_time:
        #RANDOMLY CREATE PROCESSES
        random_process = random.choice([True, False])
        if random_process:
            new_process = scheduleProcess(len(process))
            new_process.num_threads= random.randint(3,40)
            process.append(new_process)
            print(f"New Process ID: {new_process.process_id} and Number of Threads: {new_process.num_threads}")
        #RANDOMLY TERMINATE PROCESSES
        if process: 
            terminate =np.random.choice(process)
            process.remove(terminate)
            print(f"Terminating Process ID: {terminate.process_id}")
            
        #calls round robin 
        round_robin(cpu, process)
        #runs the while loop every 5 seconds  
        time.sleep(5)
    print(process)
if __name__ == "__main__":
    schedule()
