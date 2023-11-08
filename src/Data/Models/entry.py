import datetime


class Entry:
    __id: str
    __title: str
    __body: str
    __owner_name: str
    date = datetime.datetime.now()

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_body(self, body):
        self.__body = body

    def get_body(self):
        return self.__body

    def set_owner_name(self, ownername):
        self.__owner_name = ownername

    def get_owner_name(self):
        return self.__owner_name

    def set_created_date(self, date):
        self.date = datetime

    def get_created_date(self):
        return datetime

    

