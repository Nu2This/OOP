# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#     def __str__(self):
#         return '<Book:{} by {}>'.format(self.title, self.author)
#
# class TextBook(Book):
#     def __init__(self, title, author, edition):
#         super().__init__(title, author)
#         self.edition = edition
#
#
# textbook = TextBook(title = 'Physics', author = 'PHD', edition= '5')
# book = Book(title='All the Light', author='some person')
# print(book)
# print(textbook)





class A:
    def say_my_name(self):
        print('A')


class B:
    def say_my_name(self):
        print('B')

class C:
    def say_my_name(self):
        print('C')
class D(B,C):
    pass

a = A()
b = B()
c = C()
d = D()

a.say_my_name()
b.say_my_name()
c.say_my_name()
d.say_my_name()
