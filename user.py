class User:
    def __init__(self, first_name, last_name, email, age, is_reward_member = False, gold_card_points = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = is_reward_member
        self.gold_card_points = gold_card_points


    def display_info(self):
        print(f"First Name : {self.first_name}\n Last Name : {self.last_name}\n Email : {self.email}\n Age : {self.age}\n Reward Member Status : {self.is_reward_member}\n Gold Card Points : {self.gold_card_points}\n")

    def enroll(self):
        if self.is_reward_member == True:
            print("User already a member.")
        else:
            self.is_reward_member = True

        if self.is_reward_member == True:
            self.gold_card_points += 200

    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
        else:
            print("Transaction Failed : Insufficient Funds")

John = User("John", "Lee", "johnlee011500@gmail.com", 23)
User1 = User("User1", "user1", "User1@gmail.com", 11)
User2 = User("User2", "user2", "User2@gmail.com", 22)




John.enroll()

User1.spend_points(50)

User2.enroll()

User2.spend_points(80)

John.display_info()

User1.display_info()

User2.display_info()




