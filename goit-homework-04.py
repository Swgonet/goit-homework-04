from collections import UserDict

class AdressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    

class Record:
    def __init__(self, name=None, *phones):
        self.name = name
        self.phones = list(phones)
        if phone:
            self.phones.append(phone)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        if old_phone in self.phones:
            index = self.phones.index(old_phone)
            self.phones[index] = Phone(new_phone)
            
    def get_phones(self):
        return [phone.get_value() for phone in self.phones]
# здесь логика добавления/удаления/редактирования необязательных полей и хранения обязательного поля Name.
    

class Field:
    def __init__(self, value):
        self.value = value
# который будет родительским для всех полей, в нем потом реализуем логику общую для всех полей.

class Name(Field):
    pass

class Phone(Field):
    pass

if __name__ == "__main__":
     name = Name('bob')
     phone = Phone('1234567890')
     rec = Record(name, phone)
     ab = AdressBook()
     ab.add_record(rec)
     assert isinstance(ab['bob'], Record)
     assert isinstance(ab['bob'].name, Name)
     assert isinstance(ab['bob'].phones, list)
     assert isinstance(ab['bob'].phones[0], Phone)
     assert ab['bob'].phones[0].value == '1234567890'
     print('All Ok)')
     