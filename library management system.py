import pandas as pd
import csv
import matplotlib.pyplot as plt
from datetime import date, timedelta

print("---------------------------------------------- WELCOME TO NATIONAL DIGITAL LIBRARY ASSOCIATION ------------------------------------------")

def addNewBook():
    bookid=int(input("Enter a book id: "))
    title=input("Enter book title: ")
    author=input("Enter author of the book: ")
    publisher=input("Enter book publisher: ")
    edition=input("Enter edition of book: ")
    cost=int(input("Enter cost of the book: "))
    category=input("Enter category of book: ")
    bdf=pd.read_csv ("book.csv")
    n=bdf["bookid"].count()
    bdf.loc[n]=[bookid,title,author,publisher,edition,cost,category]
    bdf.to_csv("book.csv", index=False)
    print ("Book Added Successfully")
    print(bdf)

def searchBook():
    title=input("Enter a book name : ")
    bdf=pd.read_csv("book.csv")
    df=bdf.loc[bdf["title"]==title]
    if df.empty:
        print ("No book found with given code")
    else:
        print("Books details are: ")
        print(df)

def deleteBook():
    bookid=float(input("Enter a bookid: "))
    bdf=pd.read_csv("book.csv")
    bdf=bdf.drop(bdf[bdf["bookid"]==bookid].index)
    bdf.to_csv("book.csv", index=False)
    print("Book Deleted Successfully")
    print(bdf)

from texttable import Texttable
from rich.console import Console
from rich.table import Table
'''def showBooks():
    df=pd.read_csv("book.csv")
    #t=Texttable()
    table=Table(title="Books Catalog")
    rows=df.values.tolist()
    rows=[[str(el) for el in row] for row in rows]
    columns=df.columns.tolist()
    for column in columns:
        table.add_column(column)
    for row in rows:
        table.add_row(*row)
    console=Console()
    console.print(table)
    #print(t.draw())'''

from tabulate import tabulate
'''def showBooks():
    df = pd.read_csv("book.csv")
    
    # Display all columns and rows without truncation
    with pd.option_context('display.max_columns', None, 'display.max_rows', None, 'display.expand_frame_repr', False):
        print(tabulate(df, headers='keys', tablefmt='fancy_grid'))'''

from prettytable import  PrettyTable
def showBooks():
    with open("book.csv",'r') as f:
        r=csv.reader(f)
        l=list(r)
        t=PrettyTable(["BookID", "Title", "Author", "Publisher", "Edition", "Cost", "Category"])
        for i in range(1,len(l)):
            t.add_row(l[i])
        print(t)

def showMembers():
    with open("member.csv",'r') as f:
        r=csv.reader(f)
        l=list(r)
        t=PrettyTable(["MemberID", "Name", "Phone", "BooksIssued"])
        for i in range(1,len(l)):
            t.add_row(l[i])
        print(t)

def showissuedBooks():
    with open("issuebooks.csv",'r') as f:
        r=csv.reader(f)
        l=list(r)
        t=PrettyTable(["Book Name", "Member Name", "Date of Issue", "Books Issued", "Return Date"])
        for i in range(1,len(l)):
            t.add_row(l[i])
        print(t)

'''def showBooks():
    bdf=pd.read_csv("book.csv")
    print(bdf)'''

'''def showBooks():
    bdf = pd.read_csv("book.csv")
    print("\nAll Books:")
    print("{:<10} {:<50} {:<30} {:<20} {:<10} {:<10} {:<15}".format(
        "BookID", "Title", "Author", "Publisher", "Edition", "Cost", "Category"))
    print("="*105)
    for index, row in bdf.iterrows():
        print("{:<10} {:<50} {:<30} {:<20} {:<10} {:<10} {:<15}".format(
            row['bookid'], row['title'], row['author'], row['publisher'], row['edition'], row['cost'], row['category']))
    print("\n")

def showMembers():
    mdf = pd.read_csv("member.csv")
    print("\nAll Members:")
    print("{:<10} {:<20} {:<15} {:<10}".format("MemberID", "Name", "Phone", "BooksIssued"))
    print("="*60)
    for index, row in mdf.iterrows():
        print("{:<10} {:<20} {:<15} {:<10}".format(
            row['mid'], row['mname'], row['phoneno'], row['numberofbooksissued']))
    print("\n")

def showissuedBooks():
    idf = pd.read_csv("issuebooks.csv")
    print("\nAll Issued Books:")
    print("{:<20} {:<20} {:<15} {:<15} {:<15}".format(
        "Book Name", "Member Name", "Date of Issue", "Books Issued", "Return Status"))
    print("="*85)
    for index, row in idf.iterrows():
        print("{:<20} {:<20} {:<15} {:<15} {:<15}".format(
            row['book_name'], row['m_name'], row['dateofissue'], row['numberofbookissued'], row['returnstatus']))
    print("\n")'''

'''def showBooks():
    bdf = pd.read_csv("book.csv")
    print("--------------------------------------------------------------------")
    print("                         Books Catalog                               ")
    print("--------------------------------------------------------------------")
    print(bdf.to_string(index=False))

def showMembers():
    mdf = pd.read_csv("member.csv")
    print("--------------------------------------------------------------------")
    print("                       Members List                                  ")
    print("--------------------------------------------------------------------")
    print(mdf.to_string(index=False))

def showissuedBooks():
    idf = pd.read_csv("issuebooks.csv")
    print("--------------------------------------------------------------------")
    print("                 Issued Books List                                  ")
    print("--------------------------------------------------------------------")
    print(idf.to_string(index=False))'''

'''def showBooks():
    bdf = pd.read_csv("book.csv")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                                                                            Books Catalog                                                                                                                            ")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    col_width = max(len(str(col)) for col in bdf.columns) + 2  # Compute the maximum column width
    for col in bdf.columns:
        print(f"{col.center(col_width)}", end=" | ")
    print("\n" + "-" * (col_width * len(bdf.columns) + (len(bdf.columns) - 1) * 3))  # Separator line
    for index, row in bdf.iterrows():
        for col in bdf.columns:
            print(f"{str(row[col]).center(col_width)}", end=" | ")
        print()
    print()'''

'''def showMembers():
    mdf = pd.read_csv("member.csv")
    print("--------------------------------------------------------------------")
    print("                         Members List                               ")
    print("--------------------------------------------------------------------")
    col_width = max(len(str(col)) for col in mdf.columns) + 2
    for col in mdf.columns:
        print(f"{col.center(col_width)}", end=" | ")
    print("\n" + "-" * (col_width * len(mdf.columns) + (len(mdf.columns) - 1) * 3))
    for index, row in mdf.iterrows():
        for col in mdf.columns:
            print(f"{str(row[col]).center(col_width)}", end=" | ")
        print()
    print()

def showissuedBooks():
    idf = pd.read_csv("issuebooks.csv")
    print("--------------------------------------------------------------------")
    print("                      Issued Books List                             ")
    print("--------------------------------------------------------------------")
    col_width = max(len(str(col)) for col in idf.columns) + 2
    for col in idf.columns:
        print(f"{col.center(col_width)}", end=" | ")
    print("\n" + "-" * (col_width * len(idf.columns) + (len(idf.columns) - 1) * 3))
    for index, row in idf.iterrows():
        for col in idf.columns:
            print(f"{str(row[col]).center(col_width)}", end=" | ")
        print()
    print()'''



def addNewMember():
    mid=int(input("Enter a member id: "))
    mname=input("Enter member name: ")
    phoneno=int(input("Enter phone number: "))
    numberofbooksissued=0
    mdf=pd.read_csv("member.csv")
    n=mdf["mid"].count()
    mdf.loc[n]=[mid,mname,phoneno,numberofbooksissued]
    mdf.to_csv("member.csv",index=False)
    print ("New Member Added Successfully")
    print(mdf)

def searchMember():
    m_name=input("Enter a member name: ")
    bdf=pd.read_csv("member.csv")
    df=bdf.loc[bdf["m_name"]==m_name]
    if df.empty:
        print ("No member found with given name")
    else:
        print ("Members details are: ")
        print(df)

def deleteMember():
    mid=float(input("Enter a member id: "))
    bdf=pd.read_csv("member.csv")
    bdf=bdf.drop(bdf[bdf["mid"]==mid].index)
    bdf.to_csv("member.csv",index=False)
    print("Member Deleted Successfully")
    print(bdf)

'''def showMembers():
    bdf=pd.read_csv("member.csv")
    print(bdf)'''

'''def issueBooks():
    m_name=input("Enter member name: ")
    mdf=pd.read_csv("member.csv")
    mdf=mdf.loc[mdf["m_name"]==m_name]
    if mdf.empty:
        print("No such Member Found")
        return
    
    book_name=input("Enter book name: ")
    bdf=pd.read_csv("book.csv")
    bdf=bdf.loc[bdf["title"]==book_name]
    if bdf.empty:
        print("No Book Found in the Library")
        return

    #dateofissue=int(input("Enter date of issue: "))
    numberofbookissued=int(input("Enter number of book issued: "))
    if numberofbookissued <= 0:
        print("Invalid number of books issued. Please enter a positive number.")
        return
    mdf_index = mdf.index[0]
    mdf.loc[mdf_index, "numberofbookissued"] += numberofbookissued
    mdf.to_csv("member.csv", index=False)
    bdf=pd.read_csv("issuebooks.csv")
    n=bdf["book_name"].count()
    bdf.loc[n]=[book_name,m_name,date.today(),numberofbookissued,""]
    bdf.to_csv("issuebooks.csv",index=False)
    print("Book Issued Successfully")
    print(bdf)'''

def issueBooks():
    m_name=input("Enter member name: ")
    mdf=pd.read_csv("member.csv")
    mdf=mdf.loc[mdf["m_name"]==m_name]
    if mdf.empty:
        print("No such Member Found")
        return
    
    # Assuming a count of 1 when issuing a new book
    numberofbookissued = 1
    
    mdf_index = mdf.index[0]
    mdf.loc[mdf_index, "numberofbookissued"] += numberofbookissued
    mdf.to_csv("member.csv", index=False)
    
    book_name = input("Enter book name: ")
    bdf = pd.read_csv("book.csv")
    bdf = bdf.loc[bdf["title"] == book_name]
    
    if bdf.empty:
        print("No Book Found in the Library")
        return
    
    bdf = pd.read_csv("issuebooks.csv")
    n = bdf["book_name"].count()
    bdf.loc[n] = [book_name, m_name, date.today(), numberofbookissued, date.today()+timedelta(days=15)]
    bdf.to_csv("issuebooks.csv", index=False)
    
    print("Book Issued Successfully")
    showissuedBooks()

def returnBook():
    m_name=input("Enter a member name: ")
    book_name=input("Enter book name: ")
    idf=pd.read_csv("issuebooks.csv")
    idf=idf.loc[idf["book_name"]==book_name]
    if idf.empty:
        print ("The Book is not issued in records")
    else:
        idf=idf.loc[idf["m_name"]==m_name]
        if idf.empty:
            print("The book is not issued to the member")
        else:
            print("Book can be returned")
            ans=input("Are you sure you want to return the book: ")
            if ans.lower()=="yes":
                idf=pd.read_csv("issuebooks.csv")
                idf=idf.drop(idf[idf["book_name"]==book_name].index)
                idf.to_csv("issuebooks.csv",index=False)
                mdf=pd.read_csv("member.csv")
                mdf_index = mdf.index[0]
                mdf.loc[mdf_index, "numberofbookissued"] -= 1
                mdf.to_csv("member.csv", index=False)
                print("Book Returned Successfully")
            else:
                print("Return operation cancelled")

'''def showissuedBooks ():
    idf=pd.read_csv("issuebooks.csv")
    print(idf)'''

def showCharts():
    print("Press 1 - Books and their Category")
    print("Press 2 - Books and their Publishers")
    print("Press 3 - Books and their Authors")
    ch = int(input("Enter your choice: "))
    
    df = pd.read_csv("book.csv")

    if ch == 1:
        df_plot = df["category"].value_counts()
        df_plot.plot(kind='bar', color="blue")
        plt.xlabel('Category')
        plt.ylabel('Count')
        plt.title('Books Count in Each Category')
        plt.show()

    elif ch == 2:
        df_plot = df["publisher"].value_counts()
        df_plot.plot(kind='bar', color="red")
        plt.xlabel('Publisher')
        plt.ylabel('Count')
        plt.title('Books Count for Each Publisher')
        plt.show()

    elif ch == 3:
        df_plot = df["author"].value_counts()
        df_plot.plot(kind='bar', color="green")
        plt.xlabel('Author')
        plt.ylabel('Count')
        plt.title('Books Count for Each Author')
        plt.show()

    else:
        print("Invalid Option Selected")

def login():
    uname=input("Enter Username: ")
    pwd=input("Enter Password: ")
    df=pd.read_csv("users.csv")
    df=df.loc[df["username"]==uname]
    if df.empty:
        print("Invalid Username given")
        return False
    else:
        df=df.loc[df["password"]==pwd]
        if df.empty:
            print("Invalid Password")
            return False
        else:
            print("Username and Password matched successfully")
            return True
        
def showMenu():
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                                           NATIONAL DIGITAL LIBRARY ASSOCIATION                                                                                         ")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Press 1 - Add a New Book")
    print("Press 2 - Search for a Book")
    print("Press 3 - Delete a Book")
    print("Press 4 - Show All Books")
    print("Press 5 - Add a New Member")
    print("Press 6 - Search for a Member")
    print("Press 7 - Delete a Member")
    print("Press 8 - Show All Members")
    print("Press 9 - Issue a Book")
    print("Press 10 - Return a Book")
    print("Press 11 - Show All Issued Books")
    print("Press 12 - To view Charts")
    print("Press 13 - To exit")
    choice=int(input("Enter your choice: "))
    return choice

if login():
    while True:
        ch=showMenu()
        if ch==1:
            addNewBook()
        elif ch==2:
            searchBook()
        elif ch==3:
            deleteBook()
        elif ch==4:
            showBooks()
        elif ch==5:
            addNewMember()
        elif ch==6:
            searchMember()
        elif ch==7:
            deleteMember()
        elif ch==8:
            showMembers()
        elif ch==9:
            issueBooks()
        elif ch==10:
            returnBook()
        elif ch==11:
            showissuedBooks()
        elif ch==12:
            showCharts()
        elif ch==13:
            break
        else:
            print("Invalid Option Selected")

print("THANK YOU FOR VISITING THE LIBRARY")
