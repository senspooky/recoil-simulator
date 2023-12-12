from src.simulator.stoppable_thread import StoppableThread
from datetime import datetime
from time import sleep

# a thread that loops until stopped. 
class LoopingThread(StoppableThread):
    def __init__(self, *args, **kwargs):
        super(LoopingThread, self).__init__(*args, **kwargs)
        
        # managing delta time
        self.CONST_MAX_UPDATE_RATE = 30
        self.lastUpdate = datetime.now()
        self.deltaTime = 0

    def loop(self):
        self.lastUpdate = datetime.now()
        while not self.stopped():
            self.deltaTime = (datetime.now() - self.lastUpdate).total_seconds()
            sleepTime = 1 / self.CONST_MAX_UPDATE_RATE - self.deltaTime
            # sleep to maintain constant update rate
            if sleepTime > 0:
                sleep(sleepTime)
                self.deltaTime = 1 / self.CONST_MAX_UPDATE_RATE
            self.lastUpdate = datetime.now()
            self.loopBody()

             
    def loopBody(self): # this is called every loop
        raise NotImplementedError("loopBody not implemented by subclass")