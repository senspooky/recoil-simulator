from src.simulator.looping_thread import LoopingThread
from src.simulator.simulation import Simulator
from threading import Lock

# manages the simulation 
class Renderer(LoopingThread):
    def __init__(self):
        self.lock = Lock()
        self.simulator:Simulator | None = None
        super(Renderer, self).__init__(**{"target": self.loop})
        
    def loopBody(self):
        if not self.simulator:
            raise Exception("Renderer has no linked simulator")
        self.lock.acquire()
        self.readSimulator()
        self.simulator.lock.release()
        self.draw()
        
    def readSimulator(self):
        print("read transforms")
        
    def draw(self):
        print("draw")