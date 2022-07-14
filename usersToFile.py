import csv
import os.path

class UsersToFile():
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__users_list = []
        # self.openFile()

    def getFileName(self): return self.__file_name
    def getUsers(self): return self.__users_list

    def isExists(self, name):
        if len(self.__users_list) > 0:
            for el in self.__users_list:
                if str(el[0]) == str(name):
                    return True
        return False

    def addUser(self, name, password):
        user = [name, password]
        if self.isExists(name) == False:
            self.__users_list.append(user)
            self.append_in_File(name, password)
            return True
        else:
            print('The user is present')
            return False

    def removeUser(self, name):
        if len(self.__users_list) > 0:
            for el in self.__users_list:
                # print(str(el[0]) + '-' + str(name))
                if str(el[0]) == str(name):
                    self.__users_list.remove(el)
                    self.write_in_File()
                    return True
        return False

    def openFile(self):
        if os.path.exists(self.__file_name):
            file = open(self.__file_name, 'r')           
            lines = csv.reader(file)
            for row in lines:
                self.__users_list.append(row)
            file.close()
            return self.__users_list
        else:
            print('File not found!')
            return False
    
    def write_in_File(self):
        if os.path.exists(self.__file_name):
            file = open(self.__file_name, 'w')
            print(self.__users_list)

            for el in self.__users_list:
                file.write(str(el[0]) + ',' + el[1] + '\n')
            file.close()
            return True
        else:
            print('File not found')
            return False
    
    def append_in_File(self, name, password):
        if os.path.exists(self.__file_name):
            file = open(self.__file_name, 'a')
            file.write(str(name) + ',' + str(password) + '\n')
            file.close()
            return True
        else:
            print('File not found')
            return False

 