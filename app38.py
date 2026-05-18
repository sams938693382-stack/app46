class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}
        self.users = {}
        self.history = []

    def add_book(self, title, count):
        if title in self.books:
            self.books[title] += count
        else:
            self.books[title] = count
        self.history.append(f"Book added: {title} +{count}")

    def add_user(self, username):
        if username not in self.users:
            self.users[username] = []
            self.history.append(f"User added: {username}")

    def borrow_book(self, username, title):
        if username not in self.users:
            print("User yoq")
            return

        if title not in self.books or self.books[title] == 0:
            print("Kitob yoq")
            return

        self.books[title] -= 1
        self.users[username].append(title)
        self.history.append(f"{username} borrowed {title}")

    def return_book(self, username, title):
        if username in self.users and title in self.users[username]:
            self.users[username].remove(title)
            self.books[title] += 1
            self.history.append(f"{username} returned {title}")

    def show_books(self):
        print("BOOKS:")
        for k, v in self.books.items():
            print(k, ":", v)

    def show_users(self):
        print("USERS:")
        for u, b in self.users.items():
            print(u, "->", b)

    def search_book(self, title):
        if title in self.books:
            print(title, "topildi:", self.books[title])
        else:
            print("Topilmadi")

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            self.history.append(f"Book removed: {title}")

    def clear_history(self):
        self.history = []
        print("History cleared")

    def show_history(self):
        for h in self.history:
            print(h)

    def stats(self):
        total = sum(self.books.values())
        print("Total books:", total)
        print("Users:", len(self.users))

    def borrow_all(self, username):
        for book in list(self.books.keys()):
            if self.books[book] > 0:
                self.borrow_book(username, book)

    def return_all(self, username):
        if username in self.users:
            for book in list(self.users[username]):
                self.return_book(username, book)

    def rename_library(self, new_name):
        self.name = new_name

    def reset(self):
        self.books.clear()
        self.users.clear()
        self.history.clear()
        print("System reset")


# -------- TEST --------
lib = Library("Central Library")

lib.add_book("Python", 5)
lib.add_book("Java", 3)
lib.add_book("C++", 2)

lib.add_user("Ali")
lib.add_user("Vali")

lib.borrow_book("Ali", "Python")
lib.borrow_book("Vali", "Java")

lib.show_books()
lib.show_users()

lib.return_book("Ali", "Python")

lib.search_book("C++")

lib.stats()

lib.show_history()

lib.rename_library("City Library")

lib.reset()