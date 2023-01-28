books = [["introduction to computing using python" , "ljubomir" , "programming" , 4 , "available"],
         ["data structures and algorithms in python" , "michael" , "data structures" , 2 , "available"],
         ["digital design" , "moris mano" , "digital logic design" , 5 , "available"],
         ["advanced engineering mathematics" , "erwin kreyszig" , "complex variables" , 3 , "available"],
         ["calculus and analytical geometry" , "howard anton" , "calculus" , 1 , "available"],
         ["fundamentals of electric circuits" , "alexander" , "circuit theory" , 5 , "available"],
         ["microelectronic circuits" , "sedra and smith" , "electrical engineering" , 6 , "available"],
         ["discrete mathematics and its applications" , "kenneth rosen" , "discrete structures" , 0, "not available"],
         ["mathematical structures for computer science" , "judith gersting" , "discrete structures" , 4 , "available"],
         ["electronic devices" , "floyd" , "electrical engineering" , 2 , "available"],
         ["fundamentals of physics" , "halliday resnick" , "physics" , 6 , "available"],
         ["vector analysis" , "schaum series" , "physics" , 0 , "not available"],
         ["the sealed nectar" , "safi ur rehman" , "islamiat" , 6 , "available"],
         ["python 3 object oriented programming" , "dusty philips" , "programming" , 4 , "available"],
         ["learning python" , "mark lutz" , "programming" , 3 , "available"]]

##name , dept , batch , book , status
members = [["aleena" , "mech" , 2021 , "learning python" , "renewed"],
           ["sunyah" , "cis" , 2019 , "None" , "None"],
           ["mubashir" , "software" , 2020 , "digital design" , "checked out"],
           ["safia" , "EE" , 2020 , "None" , "None"]]         

def display_books(bks):
    
    print("TITLE                                             AUTHOR                        SUBJECT                       QUANTITY  STATUS")
    print()
    for i in bks:        
        print(f"{i[0]:50}{i[1]:30}{i[2]:30}{str(i[3]):10}{i[4]}")


def display_members(mem):
    
    print("NAME           DEPARTMENT     BATCH          BOOK                                              STATUS")
    print()
    for i in mem:        
        print(f"{i[0]:15}{i[1]:15}{str(i[2]):15}{i[3]:50}{i[4]}")


def add_book(tit , auth , subj , quant , status):
    
    books.append([tit , auth , subj , quant , status])


def edit_book(field , bk , data):
    
    for i in range(len(books)):
        if bk == books[i][0]:
            if field == "title":
                books[i][0] = data
            if field == "author":
                books[i][1] = data
            if field == "subject":
                books[i][2] = data
            if field == "quantity":
                books[i][3] = data


def remove_book(bk):
    
    for i in books:
        if bk in i:
            books.remove(i)


def search(lst , item):

    for i in range(len(lst)):
        if item in lst[i]:
            print(lst[i])


def register(name , dept , batch , book , status):

    members.append([name , dept , batch , book , status])


def cancelMembership(name , dept , batch):

    for i in members:
        if name == i[0] and dept == i[1] and batch == i[2]:
            members.remove(i)


def checkOut(name , dept , batch , bk):
    
    for i in members:
        if name == i[0] and dept == i[1] and batch == i[2]:
            i[3] = bk
            i[4] = "checked out"
            
    for i in books:
        if bk in i:
            
            if i[3] > 0:
                i[3] = i[3] - 1
                if i[3] == 0:
                    i[4] = "not available"
                    
            elif i[3] == 0:
                
                if i[4] == "not available":
                    reserve(name , dept , batch , bk)
                elif i[4] == "reserved":
                    print("Book not available to check out or reserve")

    print(f"{bk} checked out by {name} of dept {dept} batch {batch}")

def reserve(name , dept , batch , bk):
    
    for i in books:
        if bk in i and i[3] == 0 and i[4] == "not available":
            i[4] = "reserved"
            
    for i in members:
        if name == i[0] and dept == i[1] and batch == i[2]:
            i[3] = bk
            i[4] = "reserved"

    print(f"{bk} reserved by {name} of dept {dept} batch {batch}")

def renew(name , dept , batch , bk):
    
    for i in members:
        if name == i[0] and dept == i[1] and batch == i[2] and i[3] == bk:
            i[4] = "renewed"

    print(f"{bk} renewed by {name} of dept {dept} batch {batch}")
            
def Return(name , dept , batch , bk):
    
    for i in members:
        if name == i[0] and dept == i[1] and batch == i[2] and i[3] == bk:
            i[3] = "None"
            i[4] = "None"
            
        for i in books:
            if bk in i:
                i[3] = i[3] + 1
                i[4] = "available"

    print(f"{bk} returned by {name} of dept {dept} batch {batch}")


def bubbleSort(bk):
    length = len(bk)
    for i in range(length-1):
        for j in range(length-i-1):
            if bk[j] > bk[j+1]:
                bk[j], bk[j+1] = bk[j+1], bk[j]


while True:
    
    print('''MENU:
1 : display books
2 : display members
3 : add books
4 : edit books
5 : remove books
6 : sort books
7 : search books
8 : create account
9 : cancel membership
10 : check out book
11 : reserve book
12 : renew book
13 : return book
14 : exit''')

    print()
    opt=int(input('enter option number: '))
    print()
    
    if opt == 1:
        
        display_books(books)
        print("\n"+"*"*130+"\n")
        continue
    
    elif opt == 2:
        
        display_members(members)
        print("\n"+"*"*130+"\n")
        continue
    
    elif opt == 3:
        
        title = input("Enter title of the book: ")
        author = input("Enter author of the book: ")
        subject = input("Enter subject of the book: ")
        quantity = input("Enter quantity of the book available: ")
        status = input("Enter status of the book, \"available\" or \" not available\": ")
        
        add_book(title , author , subject , quantity , status)
        print()
        print("\t\tUPDATED BOOK LIST")
        print()
        display_books(books)
        print("\n"+"*"*130+"\n")
        continue
    
    elif opt == 4:
        field = input("Enter field of the book to edit: ")
        title = input("Enter title of the book: ")
        data = input("Enter new data for the book: ")
        
        edit_book(field , title , data)
        print()
        print("\t\tUPDATED BOOK LIST")
        print()
        display_books(books)
        print("\n"+"*"*130+"\n")
        continue
    
    elif opt == 5:
        book = input("enter title or author or subject of the book to remove: ")
        
        remove_book(book)
        print()
        print("\t\tUPDATED BOOK LIST")
        print()
        display_books(books)
        print("\n"+"*"*130+"\n")
        continue
    
    elif opt == 6:
        
        bubbleSort(books)
        print()
        print("\t\tUPDATED BOOK LIST")
        print()
        display_books(books)
        print("\n"+"*"*130+"\n")
        continue
    
    elif opt == 7:
        
        item = input("enter title of the book to search: ")
        
        search(books , item)
        print("\n"+"*"*130+"\n")
        continue
    
    elif opt == 8:
        
        name = input("Enter name of the student: ")
        dept = input("Enter department of the student: ")
        batch = input("Enter batch of the student: ")
        book = input("Enter book issued or reserved or renewed by the student, otherwise enter \"None\": ")
        status = input("Enter status of the book, \"checked out\" or \"reserved\" or \"renewed\" or \"None\": ")
        
        register(name , dept , batch , book , status)
        print()
        print("\t\tUPDATED MEMBERS LIST")
        print()
        display_members(members)
        print("\n"+"*"*130+"\n")
        continue
    
    elif opt == 9:
        
        name = input("Enter name of the student: ")
        dept = input("Enter department of the student: ")
        batch = input("Enter batch of the student: ")
        
        cancelMembership(name , dept , batch)
        print()
        print("\t\tUPDATED MEMBERS LIST")
        print()
        display_members(members)
        print("\n"+"*"*130+"\n")
        continue
    
    elif opt == 10:
        
        name = input("Enter name of the student: ")
        dept = input("Enter department of the student: ")
        batch = input("Enter batch of the student: ")
        book = input("Enter book issued by the student: ")
        
        checkOut(name , dept , batch , book)
        print()
        print("\t\tUPDATED BOOK LIST")
        print()
        display_books(books)
        print("\n"+"*"*130+"\n")
        continue
    
    elif opt == 11:
        
        name = input("Enter name of the student: ")
        dept = input("Enter department of the student: ")
        batch = input("Enter batch of the student: ")
        book = input("Enter book reserved by the student: ")
        
        reserve(name , dept , batch , book)
        print()
        print("\t\tUPDATED BOOK LIST")
        print()
        display_books(books)
        print("\n"+"*"*130+"\n")
        continue
    
    elif opt == 12:

        name = input("Enter name of the student: ")
        dept = input("Enter department of the student: ")
        batch = input("Enter batch of the student: ")
        book = input("Enter book renewed by the student: ")
        
        renew(name , dept , batch , book)
        print("\n"+"*"*130+"\n")
        continue
    
    elif opt == 13:
        
        name = input("Enter name of the student: ")
        dept = input("Enter department of the student: ")
        batch = input("Enter batch of the student: ")
        book = input("Enter book returned by the student: ")

        Return(name , dept , batch , book)
        print()
        print("\t\tUPDATED BOOK LIST")
        print()
        display_books(books)
        print("\n","*"*130,"\n")
        continue
    
    elif opt == 14:
        print("Exiting....")
        break
    
    else:
        
        print('enter valid option number')
        continue
