class Diary:
    __user_name: str
    __password: str
    __id: str

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

    def set_user_name(self, user_name):
        self.__user_name = user_name

    def get_user_name(self):
        return self.__user_name

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id
