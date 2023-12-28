from time import sleep
import src.config.config as config
import src.gui.gui as gui

# def syncThreads():
#     sim = Simulator()
#     renderer = Renderer()
#     renderer.lock.acquire() # lock this guy
#     sim.renderer = renderer
#     renderer.simulator = sim
#     return sim, renderer

if __name__ == "__main__":
    conf = config.Configuration("config.toml")
    conf.load()
    
    gui = gui.GUI(conf.get("GUI"))
    gui.start()