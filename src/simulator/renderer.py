from time import sleep
from src.simulator.looping_thread import LoopingThread
from threading import Lock

# manages the simulation 
class Renderer(LoopingThread):
    def __init__(self):
        self.lock = Lock()
        self.simulator = None
        super(Renderer, self).__init__(**{"target": self.loop})
        
    def loopBody(self):
        self.lock.acquire()
        self.readSimulator()
        self.simulator.lock.release()
        self.draw()
        
    def readSimulator(self):
        print("read transforms")
        
    def draw(self):
        print("draw")