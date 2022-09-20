class User():
    # def __init__(self,email):
    #     self.email = email
    def sign_in(self):
        print("Logging in ")




class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
        # User.__init__(self,email)
        # super().__init__(email)

    def attack(self):

        print(f' attacking the power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrow):
        self.name = name
        self.num_arrow = num_arrow

    def lol(self):
        print(f' arrow left: {self.num_arrow}')
    def run(self):
        print('run really fast!')
# class SuperList(list):
#     def __len__(self):
#         return  1000


class HibridBorg(Wizard,Archer):
    def __init__(self,name ,power,num_arrow):
        Archer.__init__(self,name,num_arrow)
        Wizard.__init__(self,name,power)

# print(isinstance(wizard1,User))
# wizard1 = Wizard('Merlin', 50,'monirulcr@gmail.com')

# wizard1.attack()
# print(wizard1.email)
# print(dir(wizard1))

# super_List1 =SuperList()
#
# print(len(super_List1))
# super_List1.append(5)
# super_List1.append(10)
# print(len(super_List1))
# print(super_List1[1])
# print(super_List1[:])

hb1 =HibridBorg('Tim',50,100)
print(hb1.run())
print(hb1.attack())
print(hb1.lol())
print(hb1.sign_in())
