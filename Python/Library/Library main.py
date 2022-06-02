class book:
    bName = ""
    bID = 0
    bBorrowed  = False
    
    def setBookName(self, name):
        bName = name
    def setBookID(self, ID):
        bID = ID
    def setBookBorrowedStatus(self, borrowed):
        bBorrowed = borrowed

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

class member:
    mName = ""
    mID = 0
    mPhNo = 0000000000
    mBook1  = ""
    mBook2  = ""
    mBook3  = ""

    def setMemberName(self, name):
        bName = name
    def setMemberID(self, ID):
        mID = ID
    def setMemberPhNo(self, PhNo):
        mPhNo = PhNo
    def setMemberBook1Name(self, Book1):
        mBook1 = Book1
    def setMemberBook2Name(self, Book2):
        mBook2 = Book3
    def setMemberBook3Name(self, Book3):
        mBook3 = Book3

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
book1 = book()
book1.setBookName("Percy Jackson")
book1.setBookID(0)
book1.setBookBorrowedStatus(False)

book2 = book()
book2.setBookName("Harry Potter")
book2.setBookID(1)
book2.setBookBorrowedStatus(False)

book3 = book()
book3.setBookName("Alex Rider")
book3.setBookID(2)
book3.setBookBorrowedStatus(False)

book4 = book()
book4.setBookName("Inheritance Cycle")
book4.setBookID(3)
book4.setBookBorrowedStatus(False)

book5 = book()
book5.setBookName("Trials Of Apollo")
book5.setBookID(4)
book5.setBookBorrowedStatus(False)

bookList = [book1, book2, book3, book4, book5]
bookNameList = [book1.bName, book2.bName, book3.bName, book4.bName, book5.bName]

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

member1 = member()
member1.setMemberName("Siddhant")
member1.setMemberID(1)
member1.setMemberPhNo(0000000001)

member2 = member()
member2.setMemberName("Advait")
member2.setMemberID(2)
member2.setMemberPhNo(0000000002)

member3 = member()
member3.setMemberName("Kavita")
member3.setMemberID(3)
member3.setMemberPhNo(0000000003)

member4 = member()
member4.setMemberName("Abhijit")
member4.setMemberID(4)
member4.setMemberPhNo(0000000004)

member5 = member()
member5.setMemberName("Manas")
member5.setMemberID(5)
member5.setMemberPhNo(0000000005)

memberList = [member1, member2, member3, member4, member5]
memberNameList = [member1.mName, member2.mName, member3.mName, member4.mName, member5.mName, ]

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Operation = raw_input("Do you want to Borrow: (B) or Return: (R) a book: ")
Member = raw_input("Enter your name: ")
whichBook = raw_input("Enter the name of the book: ")

if (Operation == "B"):
    for i in memberNameList:
        if i == Member
        
    



