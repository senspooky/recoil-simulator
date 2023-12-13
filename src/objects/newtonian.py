from src.objects.renderable import Renderable

# A newtonian object is a renderable object that is affected by physics by way of applying simple forces to it
# This results in linear and angular acceleration
class Newtonian(Renderable):
    def __init__(self):
        super.__init__(self)
        