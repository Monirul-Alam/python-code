class PlayerCharacter:
    memberShip = True

    def __init__(self, name, age):
        if(PlayerCharacter.memberShip):
          self.name = name
          self.age = age

    def run(self):
        print(f'my name is {self.name}')
        return 'done'


player1 = PlayerCharacter('Monirul', 20)

player2 = PlayerCharacter('Tim', 19)
player2.attack = 369

print(player1.name)
print(player1.age)
print(player2.name)
print(player2.run())
print(player1.run())

print(player2.attack)

