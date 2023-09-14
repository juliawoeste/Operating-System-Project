class Thread: 
    def __init__(self, state = "", instructions = "", stack = []):
        self.state = state
        self.instructions = instructions
        self.stack = stack
        
    def __str__(self):
        return f"State: {self.state}\nInstructions: {self.instructions}\nStack: {self.stack}"
        