from time import sleep
import src.config.config as config
import src.gui.gui as gui
import dearpygui.demo as demo
import dearpygui.dearpygui as dpg

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
    # gui.start()
    
    # dpg.create_context()
    # dpg.create_viewport(title='Custom Title', width=600, height=600)

    # demo.show_demo()

    # dpg.setup_dearpygui()
    # dpg.show_viewport()
    # dpg.start_dearpygui()
    # dpg.destroy_context()