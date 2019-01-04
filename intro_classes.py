user_name = input("Hello human, what is your characters name that will travel with you on your quest? ")
print(f"{user_name} welcome! You will be playing an adventure game, and if you succeed, at the game you will know the identity of the mysterious person.")
user_readiness = input("Are you ready to begin, if so we will start off with some basic instructions ")
print("Well whatever you said, you're still here to now we shall begin.")


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



Alex = Player('Alex', 34, 23, 45, 21)
Blob = Opponent('Andrew', 56, 19, 23, 43)
Ace = Opponent('Ace', 88, 17, 5, 0)
Zuboomafu = Opponent('Zuboomafu', 123, 56, 87, 13)
Momo = Opponent('Momo', 84, 72, 36, 57)

Alex.fight(Ace)