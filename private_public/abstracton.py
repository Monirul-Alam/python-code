class PlayerCharacter:


    def __init__(self, name, age):
          self._name = name
          self._age = age

    def run(self):
        print(f'my name is {self._name} and {self._age}')
        return 'done'


player1 = PlayerCharacter('Monirul', 20)

player1.name = 'tim'

player1.run ='booo'
print(player1.run)


