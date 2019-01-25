import random
import sys
#this will allow you to choose a random player later on and use the system exit function to exit the game

user_name = input("Hello human, what is your characters name that will travel with you on your quest? ").title()
print(f"{user_name} welcome! You will be playing an adventure game, and if you succeed, at the game you will know the identity of the mysterious person.")
user_readiness = input("Are you ready to begin, if so we will start off with some basic instructions ")
print("Well whatever you said, you're still here so now we shall begin.")
print(" ")
print("So, the computer will randomly generate a person from the magnet 2020 junior class")
print("Well, that seems like a lot of work, so I'll narrow it down, you will have to find the identity of a yearbook member in the mhs 2020 junior class")
print("As you go through the game you will have opportunities to battle opponents and earn extra clues.")
print("The goal is to figure out the person before you die or make it to the end.")
print(" ")


class Character:
  """Generic character class"""
# what both classes (opponent and the main player) have in common
  def __init__(self, name, Hp, atk, defense):
    self.name = name
    self.Hp = Hp
    self.atk = atk
    self.defense = defense
  def stats(self):
    print(f"""{self.name}'s stats:
    - HP: {self.Hp}
    - Attack: {self.atk}
    - Defense: {self.defense}\n""")
#this will clearly label the atk, defense, and Hp of each player/opponent so you do not have to keep track and it looks cleaner


class Player(Character):
  """Class for a player character"""
# this is who you will play as
  def __init__(self, name, Hp, atk, defense, weapon_strength):
    Character.__init__(self, name, Hp, atk, defense)
    self.weapon_strength = weapon_strength
#weapon strength is only for the main player so it is an extension of the generic class

  def fight(self, Opponent):
    self.atk = self.atk + self.weapon_strength
    print(f"{self.name} attacks with their weapon, which raises their attack to {self.atk}")
    old_hp = Opponent.Hp
    dmg = self.atk - Opponent.defense
    if dmg <= 0:
      print(f"hardly any damage was done")
      dmg = .1
    Opponent.Hp -= dmg
    print(f"{Opponent.name} dropped from {old_hp} to {Opponent.Hp} HP\n")


class Opponent(Character):
  """Class for opponents"""
# thesse are the people you will be fighting throughout the game in order to obtain clues

  def __init__(self, name, Hp, atk, defense, heal):
    Character.__init__(self, name, Hp, atk, defense)
    self.heal = heal
# this is an addition to the generic class because only opponents have the heal option

  def fight(self, Player):
    print(f"{self.name} uses their heal")
    old_hp = Player.Hp
    dmg = self.atk - Player.defense + self.heal
    if dmg <= 0:
      print(f"hardly any damage was done!")
      dmg = .1
    Player.Hp -= dmg
    print(f"{Player.name} dropped from {old_hp} to {Player.Hp} HP\n")



def fight(self, Opponent):
  while Opponent.Hp >= 1:
     Opponent.Hp = Opponent.Hp - self.atk
  while self.Hp >= 1:
     self.Hp = self.Hp - Opponent.atk
     print(f"After the attack by {Opponent.name}, the attacker, {self.name}, now has {self.Hp} health")
     print(f"After the attack by {self.name}, the opponent, {Opponent.name}, now has {Opponent.Hp} health")

#these are the yearbook members... one will be randomly chosen by the computer and it is your job to try and figure out who
members = {
  1: {'name': 'Anna','gender': 'female', 'hobby': 'reading', 'birthday': 'May 28', 'extra': 'glasses'},
  2: {'name': 'Abigail','gender': 'female', 'hobby': 'volleyball', 'birthday': 'January 11', 'extra': 'dog lover'},
  3: {'name': 'Beatriz','gender': 'female', 'hobby': 'art', 'birthday': 'March 14', 'extra': 'sleeping'},
  4: {'name': 'Nicole', 'gender': 'female', 'hobby': 'swimming', 'birthday': 'July 2', 'extra': 'Polish'},
  5: {'name': 'Andrew', 'gender': 'male', 'hobby': 'football', 'birthday': 'May 19', 'extra': 'robotics'},
  6: {'name': 'Kelley', 'gender': 'female', 'hobby': 'eating', 'birthday': 'March 7', 'extra': 'Asian'},
  7: {'name': 'Isabella', 'gender': 'female', 'hobby': 'skiing', 'birthday': 'December 22', 'extra': 'tall'},
  8: {'name': 'Matthew', 'gender': 'male', 'hobby': 'video games', 'birthday': 'July', 'extra': 'watches football'},
  9: {'name': 'Dexter', 'gender': 'male', 'hobby': 'drawing', 'birthday': 'June 30', 'extra': 'plays saxophone'}
}



#choosing a random member
person = random.choice(list(members))

#use this for whenever you reveal information:
#print(members[person]['name'])

member = (members[person]['name'])
#print(member)

# these are the stats for the main player and opponent
main_character = Player(user_name, 101, 23, 45, 21)
Blob = Opponent('Blob', 56, 19, 23, 43)
Ace = Opponent('Ace', 44, 17, 5, 0)
Zuboomafu = Opponent('Zuboomafu', 123, 56, 87, 13)
Momo = Opponent('Momo', 55, 21, 36, 37)

print("Bell, Bell, Bell, signals across all the clocks on campus. It's 2:50, time to go home. You're last class was in UCTech and you are walking back to magnet to grab you something from your locker. You are about to leave when")
print("")
print("... you remmeber it is Wednesday, there is yearbook today. You decide you don't want to go, but you told your friend you would drop something off to one of the members, you just can't remmeber who.")
print("")
print("only one way to find out, get to magnet and gather clues along the way in order to find the mystery member")

challenge_one = input("You have come across your first opponent in the cafeteria, if you win you will be rewarded with a hobby of the mystery person. Do you want to challenge the opponent ... yes or no? ").lower()
if challenge_one == 'yes':
  while Blob.Hp >= 0:
    # this is where the actual fighting happens
    main_character.stats()
    Blob.stats()
    main_character.fight(Blob)
    Blob.stats()
    Blob.fight(main_character)
    if Blob.Hp <= 0:
      print("Woohoo you earned your first advantage")
      #this reveals the gender of the mystery yearbook member
      print(members[person]['gender'])
    else:
      print("I don't know how you didn't win yet")
else:
  print("hmm, i guess you weren't as daring as I thought")
  #this allows you to continue with the game even if you choose not to fight
  pass

Guess = input("What is your guess for the mystery member? ").title()
#this will ensure that not matter what capitalization you use, as long as the spelling is correct, it will tell you if you have the right person
if Guess == member:
  print("WOW... i do not appreciate that, you got it on the first try :(")
  print("")
  print("But i mean congrats... good for you!")
  sys.exit()
else:
  print("Ummmmmmm no, guess you have to keep going")

print("")

challenge_two = input("You slow down now because of all the students running to the busses and as soon as you get outside of UCTech you meet your second opponent. Will you challenge them in a battle to the death? Yes or no? ")
if challenge_two == 'yes':
  while Ace.Hp >= 0:
    main_character.stats()
    Ace.stats()
    main_character.fight(Ace)
    Ace.stats()
    Ace.fight(main_character)
    if Ace.Hp <= 0:
      print("Woohoo you earned another advantage")
      print(members[person]['hobby'])
    else:
      print("I don't know how you managed to go to another round")
else:
  print("hmm, i guess you weren't as daring as I thought")
  pass

Guess = input("What is your guess for the mystery member? ").title()



if Guess == member:
  print("WOW... i still had more to my story but it looks like you figured it out. Sucks for you. You don;t get to hear the rest of my story")
  print("")
  print("But i mean congrats... good for you!")
  sys.exit()
else:
  print("Ummmmmmm no, guess you have to try again")

print("")

challenge_three = input("You are strolling past AIT on your way to the yearbook meeting WHEN all of a sudden Zuboomafu jumbs out from underneath one of the picnic tables!!! How dare they scare you like that, are you going to challenge them? yes or no? ").lower()
if challenge_three == 'yes':
  while main_character.Hp >= 0:
    main_character.stats()
    Zuboomafu.stats()
    main_character.fight(Zuboomafu)
    Zuboomafu.stats()
    Zuboomafu.fight(main_character)
    if main_character.Hp <= 0:
        print("You died, way to go")
        sys.exit()
    else:
        print("Woohoo you earned your first advantage")
        print(members[person]['birthday'])
else:
  print("hmm, i guess you weren't as daring as I thought")
  pass

if main_character.Hp >= 0:
    pass
else:
    exit

Guess = input("What is your guess for the mystery member? ").title()

if Guess == member:
  print("Good for you, you got it. BUT you don't get to enjoy my wonderful storytelling skills any longer")
  print("")
  print("But i mean congrats... good for you!")
  sys.exit()
else:
  print("Ummmmmmm no, guess you have to keep trying")


challenge_four = input("You finally make it to magnet when you are distracted by the food being sold at the island. Someone is trying to buy the last slice of pizza as you are walking to the island. Do you challenge them? yes or no ").lower()
if challenge_four == 'yes':
  while Momo.Hp >= 0:
    main_character.stats()
    Momo.stats()
    main_character.fight(Momo)
    Momo.stats()
    Momo.fight(main_character)
    if Momo.Hp <= 0:
      print("Woohoo you earned another advantage")
      print(members[person]['extra'])
    else:
      print("I don't know how you managed to go to another round")
else:
  print("hmm, i guess you weren't as daring as I thought")
  pass

  print("you are outside the yearbook meeting it is your last chance to guess the member otherwise you will just go home and be a disappointment")

Guess = input("What is your guess for the mystery member? ").title()

if Guess == member:
  print("Wow, that was pulling it a little close don't you think")
  print("")
  print("But i mean congrats... good for you!")
  sys.exit()
else:
  print("What a shame even after all those guesses you still couldn't guess the right person")
  sys.exit()



