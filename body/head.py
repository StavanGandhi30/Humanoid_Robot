from utils import *
from .eyes import *
from .eyelids import *
from .eyebrows import *
from .mouth import *
from .neck import *

class Head:
    def __init__(self):
        self.eyes = safe_init(Eyes, "Eyes")
        self.eyelids = safe_init(Eyelids, "Eyelids")
        self.eyebrows = safe_init(Eyebrows, "Eyebrows")
        self.mouth = safe_init(Mouth, "Mouth")
        self.neck = safe_init(Neck, "Neck")

    def loadVar(self):
        return self.eyes, self.eyelids, self.eyebrows, self.mouth, self.neck

    def __str__(self):
        return f"Face: {'-'*100}\n\n{self.eyes}\n{self.eyelids}\n{self.eyebrows}\n{self.mouth}\n{self.neck}\n"