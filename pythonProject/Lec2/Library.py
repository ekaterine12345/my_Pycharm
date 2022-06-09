class LibraryItem:
    def __init__(self, status, title=None, subject=None):
        if title is not None:
            self.title = title
        if subject is not None:
            self.subject = subject
        self.status = status

    def booking(self):
        if self.status == "available" and not(isinstance(self, CD)):
            self.status = "occupied"
            return "booking with success"
        else:
            return "You Can't Book This"


class Book(LibraryItem):
    def __init__(self, ISBN, authors, title, subject, status):
        super().__init__(status, title, subject)
        self.ISBN = ISBN
        self.authors = authors

    def booking(self):
        if self.status == "available":
            self.status = "occupied"
            return "booking this book with success"
        else:
            return "This book is already booked"


class Magazine(LibraryItem):
    def __init__(self, journalName, volume, status):
        LibraryItem.__init__(self, status)  # ??????????????????????????????
        # print(self.status)
        self.journalName = journalName
        self.volume = volume

    def booking(self):
        if self.status == "available":
            self.status = "occupied"
            return "booking this magazine with success"
        else:
            return "This magazine is already booked"


class CD(LibraryItem):
    def __init__(self, title, status):
        super().__init__(status, title)


b1 = Book("isbn", "rowling", "harry potter", "fantasy", "available")
print(b1.booking())

m1 = Magazine("journalName", "vol1", "available")
print(m1.booking())

c1 = CD("cd1", "available")
print(c1.booking())
