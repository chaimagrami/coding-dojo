
class character
    def _ _init_ _(self , name) :
        self name = name 
        self power = 50
        self health = 50
        self defense = 30
        self ability = 10
        
    def attack(self , enemy):
        enemy health-=self power/2
        enemy defense -= 20
        enemy defend(self power)
        print(f"[attack] {self name} attacked {enemy name} and caused a damage of {self power}")
        return self
    def_ _repr_ _(self):
        return f"[NAME] : {self name}\n[POWER] : {self power}\n[HEALTH] : {self health}\n[DEFENSE] : {self 
        defense}\n[ABILITY] : {self ability}"
    def defend(self , damage):
        self health-=(damage-(self defense))
        print(f"[DEFEND] {self name} defend an Attack and reduced the damage by {self defense}")
        return self
        
bob = Character("Bob")
mad_max = Character("Mad Max")

print("BEFORE ATTACK : \n" , bob)
