from time import sleep
from src.simulator.looping_thread import LoopingThread
from threading import Lock

# manages the simulation 
class Simulator(LoopingThread):
    def __init__(self):
        self.lock = Lock()
        self.renderer = None
        super(Simulator, self).__init__(**{"target": self.loop})
        
    def loopBody(self):
        self.lock.acquire()
        self.step()
        self.renderer.lock.release()
        
    # step updates the simulation by one frame
    def step(self):
        print("simulate")
    
