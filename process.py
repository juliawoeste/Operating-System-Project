#class definition
class Process: 
    #constuctor function
    def __init__(self, instructions = "", state = "", input = "", output = "", priority = "", memory = []):
        self.instructions = instructions
        self.state = state
        self.input = input
        self.output = output
        self.priority = priority
        self.memory = memory
        
    def __str__(self):
        return f"Process: {self.instructions}\nState: {self.state}\nInput: {self.input}\nOutput: {self.output}\nPriority: {self.priority}\nMemory: {self.memory}"