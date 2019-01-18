import random

yearbook_member_list = ['Anna', 'Abigail', 'Beatriz', 'Nicole', 'Andrew', 'Kelley', 'Isabella', 'Matthew']

class mystery_member: #definition of class called yearbook_member
  """yearbook member class"""

  def __init__(mystery_member, name, gender, hobby, birthday, extra):
    """constructor for yearbook member class"""
    mystery_member.name = name
    mystery_member.gender = gender
    mystery_member.hobby = hobby
    mystery_member.birthday = birthday
    mystery_member.extra = extra

Anna = mystery_member('Anna', 'girl', 'reading', 'May 28', 'glasses')
Abigail = mystery_member('Abigail', 'girl', 'volleyball', 'January 11', 'dog lover')
Beatriz = mystery_member('Beatriz', 'girl', 'sleeping', 'March 14', 'art')
Nicole = mystery_member('Nicole', 'girl', 'swimming ', 'July 2', 'polish')
Andrew = mystery_member('Andrew', 'boy', 'football', 'May 19', 'robotics')
Kelley = mystery_member('Kelley', 'girl', 'eating ', 'March 7', 'Asian')
Isabella = mystery_member('Isabella', 'girl', 'skiing ', 'December 22', 'tall')
Matthew = mystery_member('Matthew', 'guy', 'video games', 'July', 'watches football')

mystery_member = random.choice(yearbook_member_list)

print(mystery_member)
print(Isabella.hobby)
