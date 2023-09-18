import threading
class Thread: 
    def __init__(self, thread_num, process_id):
        super().__init__()
        self.instructions = []
        self.thread_num = thread_num
        self.state = ""
        self.process_id = process_id
        
    def __str__(self):
        return f"State: {self.state}\nInstructions: {self.instructions}\nStack: {self.stack}"
        