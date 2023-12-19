from src.objects.newtonian import Newtonian
from src.objects.renderable import Renderable

class Firearm(Newtonian, Renderable):
    def __init__(self):
        super(Newtonian, self).__init__()
        super(Renderable, self).__init__()
