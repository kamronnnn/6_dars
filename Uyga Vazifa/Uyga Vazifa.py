# # 1 - Masala
#
# # class Country:
# #     def __init__(self, name, area, population, borders: list):
# #         self.__name = name
# #         self.__area = area
# #         self.__population = population
# #         # self.__borders - borders
# #
# #     @property
# #     def get_name(self):
# #         return self.__name
# #
# #     @get_name.setter
# #     def get_name(self, new_area):
# #         self.__area = new_area
# #
# #     @get_name.deleter
# #     def  get_del(self):
# #         del self.__population
# #
# #
# #
# # Uzbekistan = Country('Uzbekistan', 450, 35)
# # print(Uzbekistan.get_name)
#
#
#
#
#
#
#
#
#
# #============================================
# # 2 - Masala
#
# from abc import ABC, abstractmethod
#
# class OS(ABC):
#     os_name = os
#     @abstractmethod
#     def get_os_name(self):
#         pass
#
#    @abstractmethod
#     def get_version(self):
#         pass
#
#     @abstractmethod
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
#
# #=====================================================
#
#
# # class OS:
# #     def __init__(self, os_name, version, year_issue):
# #         self.os_name = os_name
# #         self.versoin = version
# #         self.year_issue = year_issue
# #
# #     def get_os_name(self):
# #         pass
# #
# #     def get_version(self):
# #         pass
# #
# #     def get_year_issue(self):
# #         pass
# #
# # class Mac(OS):
# #     def __init__(self, os_name, version, year_issue):
# #         super().__init__(os_name, version, year_issue)
# #
# #     def get_os_name(self):
# #         return self.os_name
# #
# #     def get_version(self):
# #         return self.versoin
# #
# #     def get_year_issue(self):
# #         return self.year_issue
# #
# # mac_xp = Mac('Mac', 'IOS17', 2022)
# # print(mac_xp.versoin)
#
# #====================================================
#
# # class OS:
# #     def __init__(self, os_name, version, year_issue):
# #         self.os_name = os_name
# #         self.versoin = version
# #         self.year_issue = year_issue
# #
# #     def get_os_name(self):
# #         pass
# #
# #     def get_version(self):
# #         pass
# #
# #     def get_year_issue(self):
# #         pass
# # class Win(OS):
# #     def __init__(self, os_name, version, year_issue):
# #         super().__init__(os_name, version, year_issue)
# #
# #     def get_os_name(self):
# #         return self.os_name
# #
# #     def get_version(self):
# #         return self.versoin
# #
# #     def get_year_issue(self):
# #         return self.year_issue
# #
# # windows_xp = Win('Windows', '10', 2020)
# # print(windows_xp.year_issue)
#
#
#
#
#
#
#
#
#
#
#
#
