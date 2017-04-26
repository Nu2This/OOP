# # # class Book:
# # #     def __init__(self, title, author):
# # #         self.title = title
# # #         self.author = author
# # #     def __str__(self):
# # #         return '<Book:{} by {}>'.format(self.title, self.author)
# # #
# # # class TextBook(Book):
# # #     def __init__(self, title, author, edition):
# # #         super().__init__(title, author)
# # #         self.edition = edition
# # #
# # #
# # # textbook = TextBook(title = 'Physics', author = 'PHD', edition= '5')
# # # book = Book(title='All the Light', author='some person')
# # # print(book)
# # # print(textbook)
# #
# #
# #
# #
# #
# # class A:
# #     def say_my_name(self):
# #         print('A')
# #
# #
# # class B:
# #     def say_my_name(self):
# #         print('B')
# #
# # class C:
# #     def say_my_name(self):
# #         print('C')
# # class D(B,C):
# #     pass
# #
# # a = A()
# # b = B()
# # c = C()
# # d = D()
# #
# # a.say_my_name()
# # b.say_my_name()
# # c.say_my_name()
# # d.say_my_name()
#
#
# class Writeable:
#     def write(self, data):
#         with open(self.filepath, 'w') as f:
#             f.write(data)
#
# class JSONSerial:
#     def to_json(self):
#         import json
#         print(json.dumps(self.__dict__))
#
# class Readable:
#     def read(self):
#         with open(self.filepath, 'r') as f:
#             print(f.read())
#
# class Book(Writeable, Readable, JSONSerial):
#     def __init__(self, title, author, filepath):
#         self.title = title
#         self.author = author
#         self.filepath = filepath

import json

class Reader:
    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):
        with open(self.filepath, 'r') as f:
            print(f.read())

class Writer:
    def __init__(self, filepath):
        self.filepath = filepath

    def write(self, data):
        with open(self.filepath, 'w') as f:
            f.write(data)

class JSONSerial:
    def to_json(self, obj):
        print(json.dumps(obj))

class Book:
    def __init__(self, title, author, filepath):
        self.title = title
        self.filepath = filepath
        self.author = author
        self.reader = Reader(filepath)
        self.writer = Writer(filepath)
        self.serial = JSONSerial()

    def to_json(self):
        self.serial.to_json(dict(title=self.title,
                                 filepath=self.filepath,
                                 author=self.author))

    def read(self):
        self.reader.read()

    def write(self, data):
        self.writer.write(data)

book = Book(title='somethin', author = 'someone', filepath= './book.txt')
book.write('here is the first line')
book.read()
book.write('more things')
book.read()
book.to_json()
