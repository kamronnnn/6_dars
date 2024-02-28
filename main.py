# class Color:
#     def __init__(self, text):
#         self.text = text
#
#     def get_red(self):
#         return "\033[31m{}".format(self.text) + '\033[0m'
#
#     def get_green(self):
#         return '\033[32m{}'.format(self.text) + '\033[0m'
#
#     def get_yellow(self):
#         return '\033[33m{}'.format(self.text) + '\033[0m'
#
#
# print(Color('salom').get_red())
# print(Color('salom').get_green())
# print(Color('salom').get_yellow())

#============================================================

# class Color:
#     @staticmethod
#     def get_red(text):
#         return "\033[31m{}".format(text) + '\033[0m'
#
#     @staticmethod
#     def get_green(text):
#         return '\033[32m{}'.format(text) + '\033[0m'
#
#     @staticmethod
#     def get_yellow(text):
#         return '\033[33m{}'.format(text) + '\033[0m'
#
# print(Color.get_red('salom'))
# print(Color.get_green('salom'))
# print(Color.get_yellow('salom'))

#============================================================

# class Computer:
#     def __init__(self, name, processor, memory, price):
#         self.__name = name
#         self.__processor = processor
#         self.__memory = memory
#         self.__price = price
#
#     @property
#     def processor(self):
#         return self.__processor
#
#     @processor.setter
#     def processor(self, new_processor):
#         self.__processor = new_processor
#
#     @processor.deleter
#     def processor(self):
#         del self.__processor
#
# acer = Computer('Acer', 'Intel', 500, 700)
# print(acer.processor)
# acer.processor = 'AMD'
# print(acer.processor)
# del acer.processor

#============================================
#for memory


# class Computer:
#     def __init__(self, name, processor, memory, price):
#         self.__name = name
#         self.__processor = processor
#         self.__memory = memory
#         self.__price = price
#     @property
#     def memory(self):
#         return self.__memory
#
#     @memory.setter
#     def memory(self, new_memory):
#         self.__memory = new_memory
#
#     @memory.deleter
#     def memory(self):
#         del self.__memory
#
# acer = Computer('Acer', 'Intel', 500, 700)
# print(acer.memory)
# acer.memory = 1024
# print(acer.memory)
# del acer.memory

#============================================
#for price


# class Computer:
#     def __init__(self, name, processor, memory, price):
#         self.__name = name
#         self.__processor = processor
#         self.__memory = memory
#         self.__price = price
#
#     @property
#     def price(self):
#         return self.__price
#
#     @price.setter
#     def price(self, new_price):
#         self.__price = new_price
#
#     @price.deleter
#     def price(self):
#         del self.__price
#
# acer = Computer('Acer', 'Intel', 500, 700)
# print(acer.price)
# acer.price = 500
# print(acer.price)
# del acer.price

#============================================

# class OS:
#     def __init__(self, os_name, version, year_issue):
#         self.os_name = os_name
#         self.versoin = version
#         self.year_issue = year_issue
#
#     def get_os_name(self):
#         pass
#
#     def get_version(self):
#         pass
#
#     def get_year_issue(self):
#         pass
# class Linux(OS):
#     def __init__(self, os_name, version, year_issue):
#         super().__init__(os_name, version, year_issue)
#
#     def get_os_name(self):
#         return self.os_name
#
#     def get_version(self):
#         return self.versoin
#
#     def get_year_isuue(self):
#         return self.year_issue
#
# linux_xp = Linux('Linux', 'Acer', 2019)
# print(linux_xp.os_name)

#=====================================================


# class OS:
#     def __init__(self, os_name, version, year_issue):
#         self.os_name = os_name
#         self.versoin = version
#         self.year_issue = year_issue
#
#     def get_os_name(self):
#         pass
#
#     def get_version(self):
#         pass
#
#     def get_year_issue(self):
#         pass

# class Mac(OS):
#     def __init__(self, os_name, version, year_issue):
#         super().__init__(os_name, version, year_issue)
#
#     def get_os_name(self):
#         return self.os_name
#
#     def get_version(self):
#         return self.versoin
#
#     def get_year_issue(self):
#         return self.year_issue
#
# mac_xp = Mac('Mac', 'IOS17', 2022)
# print(mac_xp.versoin)

#====================================================

class OS:
    def __init__(self, os_name, version, year_issue):
        self.os_name = os_name
        self.versoin = version
        self.year_issue = year_issue

    def get_os_name(self):
        pass

    def get_version(self):
        pass

    def get_year_issue(self):
        pass
class Win(OS):
    def __init__(self, os_name, version, year_issue):
        super().__init__(os_name, version, year_issue)

    def get_os_name(self):
        return self.os_name

    def get_version(self):
        return self.versoin

    def get_year_issue(self):
        return self.year_issue

windows_xp = Win('Windows', '10', 2020)
print(windows_xp.year_issue)












