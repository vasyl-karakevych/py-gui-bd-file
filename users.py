from usersToFile import UsersToFile

class User():
    def __init__(self, name, password):
        self.__name = name
        self.__password = password

    def getName(self): return self.__name
    def getPassword(self): return self.__password

    def save(self):
        pass
    def remove(self):
        pass



# print(file.getUsers())
