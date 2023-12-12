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
    # simulate M4A1
    # gun = wt.M4A1()
    
    # print("momentum: " + str(gun.calcFirearmMomentum()) + " kg m/s")
    # print("time in barrel: " + str(gun.calcTimeInBarrel()) + " s")
    # print("force: " + str(gun.calcRecoilForce()) + " N")
    # print("torque: " + str(gun.calcTorque()) + " N m")
    sim, engine = syncThreads()
    sim.start()
    engine.start()
    sleep(5)
    sim.stop()
    engine.stop()
    sim.join()
    engine.join()
