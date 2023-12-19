from time import sleep
from src.simulator.simulation import Simulator
from src.simulator.renderer import Renderer

def syncThreads():
    sim = Simulator()
    renderer = Renderer()
    renderer.lock.acquire() # lock this guy
    sim.renderer = renderer
    renderer.simulator = sim
    return sim, renderer

if __name__ == "__main__":
    sim, engine = syncThreads()
    sim.start()
    engine.start()
    sleep(5)
    sim.stop()
    engine.stop()
    sim.join()
    engine.join()
