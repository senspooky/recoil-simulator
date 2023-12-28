from typing import Dict, Any
import dearpygui.dearpygui as dpg

class GUI():
    def __init__(self, config:Dict[str, Any] = dict()):
        self.__config = config
        
    def start(self):
        dpg.create_context()
        with dpg.window(label="Firearm Configuration"):
            dpg.add_text("Firearm")
            fa_name_input = dpg.add_input_text(label="Name", 
                                               default_value="Colt M4A1")
            
            dpg.add_text("Specifications")
            fa_barrel_length_input = dpg.add_slider_float(label="Barrel Length", 
                                                          default_value=0.368, 
                                                          max_value=2)
            fa_weight_input = dpg.add_slider_float(label="Weight", 
                                                   default_value=2.92, 
                                                   max_value=20)
            
            dpg.add_text("Firing")
            fa_rof_input = dpg.add_slider_float(label="Rate of Fire", 
                                                default_value=700, 
                                                max_value=6000)
            fa_muzzle_velocity_input = dpg.add_slider_float(
                label="Muzzle Velocity", 
                default_value=910, 
                max_value=2000)
            
        with dpg.window(label="Loading Configuration"):
            dpg.add_text("Projectile")
            proj_name_input = dpg.add_input_text(label="Name", 
                                                 default_value="5.56x45mm NATO")
            proj_caliber_input = dpg.add_slider_float(label="Caliber", 
                                                      default_value=0.00556, 
                                                      max_value=0.0254)
            proj_weight_input = dpg.add_slider_float(label="Weight", 
                                                     default_value=0.004, 
                                                     max_value=0.01)
            
            dpg.add_text("Charge")
            proj_charge_weight_input = dpg.add_slider_float(label="Weight", 
                                                            default_value=0.002, 
                                                            max_value=0.01)

        dpg.create_viewport(title='Firearm Simulator')
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()