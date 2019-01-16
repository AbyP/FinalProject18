user_name = input("Hello human, what is your characters name that will travel with you on your quest? ")
print(f"{user_name} welcome! You will be playing an adventure game, and if you succeed, at the game you will know the identity of the mysterious person.")
user_readiness = input("Are you ready to begin, if so we will start off with some basic instructions ")
print("Well whatever you said, you're still here to now we shall begin.")
print(" ")
print("So, the computer will randomly generate a person from the magnet 2020 junior class")
print("Well, that seems like a lot of work, so I'll narrow it down, you will have to find the identity of a yearbook member in the mhs 2020 junior class")
print("As you go through the game you will have opportunities to battle opponents and earn extra clues.")
print("The goal is to figure out the person before you die.")
print(" ")

class Character:
  """Generic character class"""

  def __init__(self, name, Hp, atk, defense):
    self.name = name
    self.Hp = Hp
    self.atk = atk
    self.defense = defense

  def introduce(self):
    print(f"Hi, I'm {self.name}, I have {self.Hp} health, {self.atk} attack, and {self.defense} defense.")


  def fight(self, Opponent):
    while Opponent.Hp >= 1:
      Opponent.Hp = Opponent.Hp - self.atk
    while self.Hp >= 1:
      self.Hp = self.Hp - Opponent.atk
      print(f"After the attack by {Opponent.name}, the attacker, {self.name}, now has {self.Hp} health")
      print(f"After the attack by {self.name}, the opponent, {Opponent.name}, now has {Opponent.Hp} health")


class Player(Character):
  """Class for a player character"""

  def __init__(self, name, Hp, atk, defense, weapon_strength):
    Character.__init__(self, name, Hp, atk, defense)
    self.weapon_strength = weapon_strength


class Opponent(Character):
  """Class for opponents"""

  def __init__(self, name, Hp, atk, defense, heal):
    Character.__init__(self, name, Hp, atk, defense)
    self.heal = heal



Alex = Player('Alex', 84, 23, 45, 21)
Blob = Opponent('Andrew', 56, 19, 23, 43)
Ace = Opponent('Ace', 88, 17, 5, 0)
Zuboomafu = Opponent('Zuboomafu', 123, 56, 87, 13)
Momo = Opponent('Momo', 84, 72, 36, 57)

challenge_one = input("You have come across your first opponent, if you win you will be rewarded with the gender of the mystery person. Do you want to challenge the opponent ... yes or no?")
if challenge_one == 'yes':
    Alex.fight(Ace)
    if Opponent.Hp <= self.Hp:
      print("You won")
    else:
      print("Oh you lost, better luck next time")
else:
  print("hmm, i guess you weren't as daring as I thought")

challenge_one = input("You have come across your first opponent, if you win you will be rewarded with the gender of the mystery person.")
if challenge_one == 'yes':
    Alex.fight(Ace)