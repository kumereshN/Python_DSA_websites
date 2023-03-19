from datetime import date
MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __init__(self):
        self.record = {}
       

    def __setitem__(self, name, birthday):
        self.record[name] = birthday
        print('test', name, birthday)

    def __getitem__(self, name):
        return self.record.get(name)
    
    
bday_dict = BirthdayDict()
bday_dict['bob'] = date(1987, 6, 15)
print(bday_dict.get('bob'))