def days_in_month(m,y):                                                             #function which tells total days in a month
    'returns total days in a month, arguments: month number, year'
    a=[1,3,5,7,8,10,12]                                                             #months having 31 days
    b=[4,6,9,11]                                                                    #months having 30 days
    if m==2 and y%4==0:                                                             #checking for february in leap year
        return 29
    elif m==2:                                                                      #checking for february not in leap year
        return 28
    elif m in a:                                                                    #checking for months having 31 days
        return 31
    elif m in b:                                                                    #checking for months having 30 days
        return 30
    else:
        return 'enter valid month number'                                           #if month number is not valid (greater than 12 or less than 1)

def issue_and_due_date():                                                           #function to return issue and due date
    'takes input for issue date, calculates due date, returns issue and due date, no arguments required'
    month=int(input('enter month of issuance: '))
    day=int(input('enter date of issuance: '))
    year=int(input('enter year of issuance: '))    
    duration=int(input('enter total days for keeping the book: '))
    f=days_in_month(month,year)                                                     #checking for total days in the month of issuance
    if 0<day<=f:                                                                    #checking if the date entered is not in the month
        issue_date=str(month)+'-'+str(day)+'-'+str(year)
        d=day+duration                                                              #calculating due date
        if d>f:                                                                     #checking if the due month is different from issue month
            d=d-f
            if month<12:
                due_date=str(month+1)+'-'+str(d)+'-'+str(year)                      #due date for issue months other than december
            elif month==12:
                due_date=str(1)+'-'+str(d)+'-'+str(year+1)                          #due date for issue month december
            else:
                return 'enter valid day'
        else:
            due_date=str(month)+'-'+str(d)+'-'+str(year)                            #due date if issue month and due month are same
    else:                                                                           #error message if the date entered is not in a month
        print('enter valid day')
        issue_date=due_date=None
    return [issue_date,due_date]

book_list=[]
def input_books(book_list):                                                         #function to input books details
    'takes book details as input from the user and appends in a list, argument: any list'
    cont='Y'
    while cont:
        bk=input('enter book name, author, edition, quantity, availablity status separated by \'-\': ')
        bk=bk.split('-')
        book_list.append(bk)
        cont=input('press \'Y\' to add more books: ')

students=[]
def input_std(students):                                                            #function to input student details
    'takes student details as input from the user and appends in a list, argument: any list'
    add='Y'
    while add:
        details=[]
        std=input('enter student name, roll no, dept separated by \',\': ')
        std=std.split(',')
        details.append(std)
        book=input('enter book name, author, edition separated by \',\': ')
        book=book.split(',')
        details.append(book)
        k=issue_and_due_date()                                                      #assigning [issue_date,due_date] pair to variable 'k'
        return_date=input('enter return date (m/d/y), if not returned, put \'-\': ')

        def charges():                                                              #function to calculate late charges
            'calculates extra days and charges on a book'
            charges=int(input('enter fine per day: '))
            d=k[1].split('-')
            r=return_date.split('-')
            if d[2]==r[2] and d[0]==r[0] and d[1]<r[1]:                             #returning in the same month and year but after due date
                extra_days=r[1]-d[1]
            elif d[2]==r[2] and d[0]<r[0]:                                          #returning in the same year but next month
                n=days_in_month(d[0],d[2])
                extra_days=r[1]+n-d[1]
            elif d[2]<r[2]:                                                         #returning in the next year
                extra_days=r[1]+31-d[1]
            else:                                                                   #returning in time
                extra_days=0
            return extra_days*charges
            
        c=charges()
        details.append([k,return_date,c])
        students.append(details)
        add=input('press \'Y\' to add more students: ')

def display(lst):                                                                   #function to display the entries
    'displays the records in a list, argument: any list'
    for record in lst:
        print(record)

def save_record(lst,file_name):                                                     #function to save records in a file
    'saves the records of a list in a file, arguments: any list, file name'
    f=open(file_name,'a')
    for record in lst:
        f.write(str(record))
    f.close()

def load_record(lst,file_name):                                                     #function to load records to the shell
    'reads the content of a file and load it to the shell, arguments: any lsit, file name'
    f=open(file_name)
    lst.append(eval('f.read()'))
    f.close()

def search(file_name):                                                              #function to search a word in a file
    'searches a word in a file, argument: file name'
    word=input('enter word to search: ')
    f=open(file_name)
    file=f.read()
    for i in file:                                                                  #for loop to find every occurence of the word
        if word in file:
            return file.index(word)
        else:
            return 'word not found'
    f.close()

                                                                                    #driver program
while True:
    print('''MENU:
1:input books
2:input student details
3:display book list
4:display student list
5:save book list
6:save student list
7:load book list
8:load student list
9:search books
10:search students
11:exit''')
    opt=int(input('enter option number: '))    
    if opt==1:
        input_books(book_list)
        continue
    elif opt==2:
        input_std(students)
        continue
    elif opt==3:
        display(book_list)
        continue
    elif opt==4:
        display(students)
        continue
    elif opt==5:
        save_record(book_list,'books.txt')
        continue
    elif opt==6:
        save_record(students,'std.txt')
        continue
    elif opt==7:
        load_record(book_list,'books.txt')
        continue
    elif opt==8:
        load_record(students,'std.txt')
        continue
    elif opt==9:
        print(search('books.txt'))
        continue
    elif opt==10:
        print(search('std.txt'))
        continue
    elif opt==11:
        break
    else:
        print('enter valid option number')
        continue
