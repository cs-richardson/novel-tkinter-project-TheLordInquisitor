"""
This program takes the database novel.db and give the users options to either
display all the novel names in the database, add a novel to the database,
or exit the program.
---Program template courtesy of Ms. Richardson---
---Program written by Son Nguyen---
"""
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3 as sq

# identify location of database
con = sq.connect("/Users/imperium/Documents/GitHub/novel-console-application-TheLordInquisitor/novel.db")
c = con.cursor()

def get_data(column):
    """
    Getting data from the database as specified in the parameter above
    """
    if column == 'novelName':
        sql = c.execute("SELECT Name FROM Novels")
    elif column == 'authorName':
        sql = c.execute("SELECT Name FROM Authors")
    elif column == 'authorID':
        sql = c.execute("SELECT AuthorID FROM Authors")
    elif column == 'novelID':
        sql = c.execute("SELECT NovelID FROM Novels")
    data = c.fetchall()
    return data


def insert_novels(nName, nGenre, nID, aID):
    """
    Inserting the novel into the database"
    """
    insertion = ('INSERT INTO Novels (Name, Genre, NovelID, AuthorID) Values ("' + str(nName) + '", "' + str(nGenre) + '", ' + str(nID) + ', ' + str(aID) + ')');
    sql = c.execute(insertion)
    con.commit()


def render_menu():
    """
    This function is used to create the menu
    """
    window = Tk()
    window.title("Novel Main Menu")
    window.geometry("200x100")

    res = Button(window, text="Display Novels", command = display('novels'))
    res.pack()

    rpt = Button(window, text="Add Novels", command = add_novels())
    rpt.pack()

    ext = Button(window, text="Exit", command = lambda:end_program(window))
    ext.pack()
    window.mainloop()

    print("\n----------------\n")
    print("1. Display Novels\n")
    print("2. Add Novels\n")
    print("3. Exit\n")
    print("----------------\n")
    choice = int(input("Choose an option (1/2/3): "))

    #Move on to the next phase based on the choice
    if choice == 1:
        display('novels')
    elif choice == 2:
        add_novels()
    elif choice == 3:
        end_program()
        return False;

    return True;



def end_program():
    """
    This function closes the database and end the program
    """
    print("\nQuitting now. Thank you for using this application\n")
    con.close()


def display(table):
    """
    This function display a list in a neat way as specified in the paramater
    """
    
    # Select which data to display based on the parameter
    if table == 'novels':
        table = get_data('novelName')
    elif table == 'authors':
        table = get_data('authorName')
 
    # Code from Ms. Richardson - This display the list in a neat way
    tbl = "|---------------------------\n\n"
    for eName in table:
        for field in eName:
            tbl += str(field)
        tbl += "\n\n"

    tbl += "---------------------------|"

    print("\n\nList: \n\n" + tbl)
    

def add_novels():
    """
    This function ask the user for info about the novel and add it to the
    database accordingly. It also tells the user the moment they enters
    an error, explain the error, and let them try again immediately.
    """

    

    # Get data
    display('authors')

    # Get data from database
    authorList = get_data('authorName')
    idListAuthor = get_data('authorID')
    idListNovel = get_data('novelID')

    #Check if the name is correct and match the author ID from the id List with that author using indexes
    authorUnknown = True
    numAuthor = len(get_data('authorID'))
    while authorUnknown: 
        author = input("Please input the author's name exactly as put above: ")
        for i in range(0, numAuthor):
            if author == authorList[i][0]:
                authorUnknown = False
        if authorUnknown:
            print("Invalid name. You need to enter the author's name correctly for the ID to match")
    authorID = idListAuthor[i][0]


    # Get the name and the genre from the user   
    novelName = input("Enter novel name: ")
    novelGenre = input("Enter novel genre: ")

    # Get the new ID and check if it's taken or not
    needID = True
    while needID:
        novelID = int(input("Enter novel ID: "))
        needID = False
        for ID in idListNovel:
            if novelID == ID[0]:
                needID = True
                print("The ID you've entered is already taken.")

    # Insert the novel
    insert_novels(novelName, novelGenre, novelID, authorID)

# The menu
while(render_menu()):
    print("\n\nWelcome to our library system")

