class Students():
    greet=("welcome to the new semester")
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greeting(self):
        print(f'{self.greet},{self.name},age:{self.age}')
    
neezu_object= Students("Neezu",18)
suza_object=Students("Suza",19)
prakriti_object= Students("prakriti",25)
srishti_object= Students("srishti",24)
suza_object.greeting()
srishti_object.greeting() # calling method of class students in object
neezu_object.greeting()
prakriti_object.greeting()
