class Book(object):
    """
    A class for book objects
    """
    def __init__(self, title, isbn, price=0.00):
        self.title = title
        self.isbn = isbn 
        self.ratings = []
        self.price = price

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def get_price(self):
        return self.price

    def set_isbn(self, isbn):
            self.isbn = isbn
            print('{}\'s ISBN has been updated to {}'.format(self.title, self.isbn))

    def add_rating(self, rating):
        if rating == None or (rating <= 4 and rating >= 0):
            self.ratings.append(rating)
        else:
            print('Invalid Rating')

    def get_average_rating(self):
        sum_ratings = 0
        num_ratings = 0
        for rating in self.ratings:
            if rating is not None:
                num_ratings += 1
                sum_ratings += rating
        return sum_ratings / num_ratings

    def add_price(self, price):
        self.price = price
        print('{}\'s price has been updated to {}'.format(self.title, self.price))

    def __eq__(self, other_book):
        if self.title == other_book.title and \
        self.isbn == other_book.isbn:
            return True
        return False

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    """
    A class for fiction book objects
    """
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return self.title + ' by ' + self.author

class Non_Fiction(Book):
    """
    A class for non fiction book objects
    """
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return self.title + ', a(n) ' + self.level + ' manual on ' + self.subject