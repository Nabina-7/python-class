class Mammal:
    def __init__(self, legs, eyes, name):
        self.legs=legs
        self.eyes=eyes
        self.name=name
class HumanBeing(Mammal):
    def __init__(self,brain_capacity,legs,eyes,name):
        self.brain_capacity=brain_capacity
        super(). __init__(legs,eyes,name)

    def print_details(self):
        print(f"Name:{self.name},legs:{self.legs},Eyes:{self.eyes},Brain capacity:{self.brain_capacity}")
    
prakriti_object=HumanBeing("95","2","2","prakriti")
prakriti_object.print_details()
