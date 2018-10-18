class User(object):
    """
    A class for user objects
    """
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address

    def __repr__(self):
        result = "User "
        result += self.name
        result += ', email: '
        result += self.email
        result += ', books read: '
        result += str(len(self.books.keys()))
        return result

    def __eq__(self, other_user):
        if self.name == other_user.name and \
        self.email == other_user.email:
            return True
        return False

    def read_book(self, book, rating='None'):
        self.books[book] = rating

    def get_average_rating(self):
        num = 0
        rating_sum = 0
        for rating in self.books.values():
            if rating is not None:
                rating_sum += rating
                num += 1
        return rating_sum / num

    

