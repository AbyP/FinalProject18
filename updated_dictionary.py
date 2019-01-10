yearbook_member_list = ['Anna', 'Abigail', 'Beatriz', 'Nicole', 'Andrew', 'Sara', 'Julia', 'Dexter', 'Kelley', 'Isabella', 'Matthew']

class yearbook_member : #definition of class called human
  """yearbook member class"""

def __init__(self, name, age, gender, hobby, birthday, extra):
    """constructor for yearbook member class"""
    self.name = name
    self.age = age
    self.gender = gender
    self.hobby = hobby
    self.birthday = birthday
    self.extra = extra

Anna = yearbook_member('Anna', '16', 'girl', 'reading', 'May 28', 'glasses')
Abigail = yearbook_member('Abigail', '17', 'girl', 'volleyball', 'January 11', 'dog lover')
Beatriz = yearbook_member('Beatriz', '16', 'girl', 'sleeping', 'March 14', 'marvel movies')
Nicole = yearbook_member('Nicole', '16', 'girl', 'swimming ', 'July 2', 'polish')
Sara = yearbook_member('Sara', '16', 'girl', ' ', ' ')
Andrew = yearbook_member('Andrew', '16', 'boy', ' ', ' ', 'robotics')
Julia = yearbook_member('Julia', '16', 'girl', ' ', ' ')
Dexter = yearbook_member('Dexter', '16', 'guy', ' ', ' ')
Kelley = yearbook_member('Kelley', '16', 'girl', 'eating ', 'March 7', 'Asian')
Isabella = yearbook_member('Isabella', '17', 'girl', 'skiing ', 'December 22', 'tall')
Matthew = yearbook_member('Matthew', '16', 'guy', '')
