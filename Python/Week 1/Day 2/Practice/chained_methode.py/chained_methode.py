class user :
    def __init__(self,first_name,last_name,email,age,is_rewards_member=False,gold_card_points=0) :
        self.first_name= first_name
        self.last_name= last_name
        self.email=email 
        self.age=age 
        self.is_rewards_member =is_rewards_member 
        self.gold_card_points=gold_card_points

    def display_info(self):
        print(f" first name is {self.first_name} \n last name is {self.last_name}\n age is {self.age}\n reward member {self.is_rewards_member}\n gold card points are {self.gold_card_points}") 
        return self
    def enroll(self) :
        if self.is_rewards_member== True : print("User already a member." )
        else : self.is_rewards_member=True
        self.gold_card_points =200
        return self
    def spend_points(self,amount):
        if amount<=self.gold_card_points :
            self.gold_card_points -=amount
        else : 
            print(f"you can't spend this {amount}ou can amount just {self.gold_card_points} ")  
            self.gold_card_points=0   
        return self
    
chaima = user ("chaima","grami","chaimagrami53@gmail.com", 21)    
ibechir = user ("bechir","grami","bechirgrami@gmail.com", 14)    
sabrina = user ("sabrine","grami","sabrinagrami@gmail.com", 2)   

# chaima.enroll()
# chaima.display_info()
# chaima.spend_points(50)
# bechir.enroll()
# bechir.spend_points(80)
# chaima.display_info
# bechir.display_info()
# sabrina.display_info()
# chaima.enroll()
# sabrina.spend_points(40)

chaima.display_info().enroll().spend_points(50).display_info()
bechir.enroll().spend_points(80).display_info()