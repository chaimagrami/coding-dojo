from ninja import Ninja 
from pet import Pet
from dog import dog

boyka= Pet("boyka","dog","attack")
sami = Ninja("sami","grami","bechir","meat",boyka)
sami.feed().walk().bathe()
niha=dog("nino","attack")
bechir = Ninja("bechir","grami","cute","makrouna",niha)
bechir.feed().walk().bathe()