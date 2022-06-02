class book:
    bName = ""
    bID = 00000
    bBorrowed  = False

    def __init__(self, name, ID, borrowed):
        bName = name
        bID = ID
        bBorrowed = False
    def setBookName(self, name):
        bName = name
    def setBookID(self, ID):
        bID = ID
    def setBookBorrowedStatus(self, borrowed):
        bBorrowed = borrowed
