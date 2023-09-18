#class definition
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

