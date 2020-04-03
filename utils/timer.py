import time


class Timer:
    def __init__(self):
        super().__init__()
        self.timers = {} # Dictionary of timers
    
    def start(self, name):
        startTime = time.time()
        self.timers[name] = startTime
        return startTime
    
    # Duration in seconds
    def end(self, name):
        endTime = time.time()
        return endTime - self.timers[name]
