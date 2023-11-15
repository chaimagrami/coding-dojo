from character import Character

#     child     
class Barbarian(Character):
    def _ _init_ _(self , name):
        # Character._ _init_ _(name)
        super() _ _init_ _(name)
        self rage = 70 #! Polymorphism
        self power =self power +20 #! Polymorphism
        
    def attack(self enemy): #! polymorphism
        super( attack(enemy)
              enemy health -=(self rage)/2
              return self
              
              
conan  = Barbarian("Conan")