from Book import *
from User import *

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}
    
    def create_book(self, title, isbn):
        unique = True
        for book in self.books.keys():
            if book.get_isbn() == isbn:
                print("ISBN {} not unique".format(isbn))
                unique = False
        if unique:
            new_book = Book(title, isbn)
            return new_book

    def create_novel(self, title, author, isbn):
        new_novel = Fiction(title, author, isbn)
        return new_novel

    def create_non_fiction(self, title, subject, level, isbn):
        new_non_fiction = Non_Fiction(title, subject, level, isbn)
        return new_non_fiction

    def add_book_to_user(self, book, email, rating=None):
        if email not in self.users.keys():
            print("No user with email {}".format(email))
        else:
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
        if book not in self.books.keys():
            self.books[book] = 1
        else:
            self.books[book] += 1

    def add_user(self, name, email, user_books=None):
        if email in self.users.keys():
            print("User {} already exists".format(email))
        elif '@' not in email and (
        '.com' not in email or \
        '.edu' not in email or \
        '.org' not in email):
            print("{} is not a valid email address".format(email))    
        else:    
            new_user = User(name, email)
            self.users[email] = new_user
            if user_books:
                for book in user_books:
                    self.add_book_to_user(book, email)
                
    def print_catalog(self):
        for book in self.books.keys():
            print(book)
    
    def print_users(self):
        for user in self.users.values():
            print(user)

    def get_most_read_book(self):
        most_read_book = Book('', '')
        num_times = 0
        for book in self.books.keys():
            if num_times < self.books[book]:
                num_times = self.books[book]
                most_read_book = book
        return most_read_book

    def highest_rated_book(self):
        best_book = Book('', '')
        best_rating = 0
        for book in self.books.keys():
            rating = book.get_average_rating()
            if best_rating < rating:
                best_rating = rating
                best_book = book
        return best_book

    def most_positive_user(self):
        positive_user = User('', '')
        best_rating = 0
        for user in self.users.values():
            rating = user.get_average_rating()
            if best_rating < rating:
                best_rating = rating
                positive_user = user
        return positive_user
    

    def get_n_most_expensive_books(self, n):
        expensive_books = {}
        for book in self.books.keys():
            price = book.get_price()
            if len(expensive_books.keys()) < n:
                expensive_books[book] = book.get_price()
            else:
                for name, value in expensive_books.items():
                    if price < value:
                        continue
                    else:
                        del expensive_books[name]
                        expensive_books[name] = book.get_price()
                    break            
        return expensive_books.keys()
    
    def get_worth_of_user(self, user_email):
        library_worth = 0
        for book in self.users[user_email].books.keys():
            library_worth += book.get_price()
        return '$' + str(library_worth) + '0'