from time import sleep
import threads
from threading import Lock

# manages the simulation 
class Renderer(threads.StoppableThread):
    def __init__(self):
        self.lock = Lock()
        self.simulator = None
        super(Renderer, self).__init__(**{"target": self.loop})
        
    def loop(self):
        while not self.stopped():
            self.lock.acquire()
            self.readSimulator()
            self.simulator.lock.release()
            self.draw()
        
    def readSimulator(self):
        sleep(0.1)
        print("read transforms")
        
    def draw(self):
        sleep(1)
        print("draw")