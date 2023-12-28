from typing import Dict, Any
import dearpygui.dearpygui as dpg

class GUI():
    def __init__(self, config:Dict[str, Any] = dict()):
        self.__config = config
        
    def start(self):
        dpg.create_context()
        with dpg.window(label="Firearm Configuration") as firearm_window:
            dpg.add_text("Firearm")
            dpg.add_input_text(label="Name", default_value="Colt M4A1")
            
            dpg.add_text("Specifications")
            dpg.add_input_float(label="Barrel Length", default_value=0.368, 
                                 max_value=2)
            dpg.add_input_float(label="Weight", default_value=2.92, 
                                 max_value=20)
            
            dpg.add_text("Firing")
            dpg.add_input_float(label="Rate of Fire", default_value=700, 
                                 max_value=6000)
            dpg.add_input_float(label="Muzzle Velocity", default_value=910, 
                                max_value=2000)
            
        with dpg.window(label="Loading Configuration") as loading_window:
            dpg.add_text("Projectile")
            dpg.add_input_text(label="Name", default_value="5.56x45mm NATO")
            dpg.add_input_float(label="Caliber", default_value=0.00556, 
                                 max_value=0.0254)
            dpg.add_input_float(label="Weight", default_value=0.004, 
                                 max_value=0.01)
            
            dpg.add_text("Charge")
            dpg.add_input_float(label="Weight", default_value=0.002, 
                                 max_value=0.01)
            
        with dpg.window(label="Settings") as settings_window:
            dpg.add_text("Personalization")
            dpg.add_listbox(label="Units of Measurement", 
                            items=["Imperial","Metric", "SI"], 
                            default_value="Imperial")

        dpg.create_viewport(title='Firearm Simulator')
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()