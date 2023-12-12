from time import sleep
import threads
from threading import Lock

# manages the simulation 
class Simulation(threads.StoppableThread):
    def __init__(self):
        self.lock = Lock()
        self.renderer = None
        super(Simulation, self).__init__(**{"target": self.loop})
        
    def loop(self):
        while not self.stopped():
            self.lock.acquire()
            self.step()
            self.renderer.lock.release()
        
    # step updates the simulation by one frame
    def step(self):
        sleep(0.3)
        print("simulate")
    
