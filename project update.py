import tkinter.ttk
from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
import sqlite3

conn = sqlite3.connect('database project1.db')
DDL = '''CREATE TABLE if not exists CANDIDATE(
         Candidateid INTEGER PRIMARY KEY,
         forename  VARCHAR(15),
         surname   VARCHAR(15),
         DOB       TEXT,
         EmailAddress TEXT,
         PhoneNo TEXT,
         Salary INTEGER,
         Location TEXT)'''
##         RoleWanted  TEXT)
        
try:
    print(DDL)
    conn.execute(DDL)
    print("Candidate table created/exists")
except sqlite3.Error as err:
    print("An error occured",err)

DDL2 = '''CREATE TABLE if not exists CLIENT(
          Clientid INTEGER PRIMARY KEY,
          forename VARCHAR(15),
          surname VARCHAR(15),
          Email VARCHAR(15),
          CompanyName VARCHAR(15),
          PhoneNo TEXT)'''
try:
    print(DDL2)
    conn.execute(DDL2)
    print("client table created/exists")
except sqlite3.Error as err:
    print("An error occured",err)

DDL3 = '''CREATE TABLE if not exists ROLES(
          RoleOfJob TEXT PRIMARY KEY,
          salary TEXT,
          Location TEXT)'''
try:
    conn.execute(DDL3)
    print("Roles table created/exists")
except sqlite3.Error as err:
    print("An error occured",err)

DDL4 = '''CREATE TABLE if not exists MATCH(
          Match TEXT PRIMARY KEY,
          candidateID INTEGER REFERENCES CANDIDATE (Candidateid),
          clientID INTEGER REFERENCES CLIENT(Clientid)'''

try:
    conn.execute(DDL4)
    print("Match table created/exists")
except sqlite3.Error as err:
    print("An error occured",err)

            
class ProjectMenu:
    def __init__(self,root):
        self.MenuPage = Frame(root,bg="lightblue", padx = 200, pady=200)           #make a frame for the menu page
        self.CandidatePage = Frame(root,bg="lightblue", padx = 200, pady = 200)               #make a frame for the customer page
        self.ClientPage = Frame(root,bg="lightblue", padx = 200, pady = 200)
        self.RolePage = Frame(root,bg="lightblue", padx = 200, pady = 200)
        self.RolePage2 = Frame(root,bg="lightblue", padx = 200, pady = 200)
        self.MatchPage = Frame(root,bg="lightblue", padx = 200, pady = 200)
        self.CreateMenuWidgets()          #place all the widgets on the menu page
        self.CreateCandidatePage()         #place all the widgets on the Customer page
        self.MenuPage.grid()              #grid the menu page so the user can see it.
        self.CreateClientPage()
        self.CreateRolePage()
        self.CreateRolePage2()
        self.CreateMatchPage()
        self.Populate_comboBox()
        self.listbox.bind("<<ListboxSelect>>" ,lambda e: self.show_selected_data())
    
    def CreateMenuWidgets(self):
        #creating the widgets for the menu page
        TitleLabel = Label(self.MenuPage, text = "Main Menu", font = ("Arial", 60), bg = "white")
        TitleLabel.grid(row = 0, column = 0,padx = 10, pady = 10)
        
        self.searchEntry =Entry(self.MenuPage)
        self.searchEntry.grid(row = 1, column = 5)
        self.searchLabel = Label(self.MenuPage, text = "Search", font = ("Arial", 15), bg = "white")
        self.searchLabel.grid(row = 1, column = 2)
        #  CandidateButton = Button(self.MenuPage, text = "Candidate", command = lambda: self.SwitchPage(self.CandidatePage,self.MenuPage))
        #  ClientButton = Button(self.MenuPage, text = "Client", command = lambda: self.SwitchPage(self.ClientPage,self.MenuPage))
        #  RoleButton = Button(self.MenuPage, text = "Role", command = lambda: self.SwitchPage(self.RolePage,self.MenuPage))
        #  MatchButton = Button(self.MenuPage, text = "Match",command = lambda: self.SwitchPage(self.MatchPage,self.MenuPage))
        #  CandidateButton.grid(row = 2, column = 0)
        #  ClientButton.grid(row = 1, column = 0)
        #  RoleButton.grid(row = 3, column = 0)
        #  MatchButton.grid(row =4, column = 0)
        logo = PhotoImage (file="recruitment.gif")
        logoLabel=Label(self.MenuPage,image=logo)
        logoLabel.photo = logo
        logoLabel.grid(row = 0, column = 10)

    def CreateCandidatePage(self):       
        TitleLabel = Label(self.CandidatePage, text = "Candidate Page", font = ("Arial", 40), bg = "white")
        MenuButton = Button(self.CandidatePage, text = "Back",bg="red",fg="white",command = lambda: self.SwitchPage(self.MenuPage,self.CandidatePage))

        self.CandidateIdEntry = Entry(self.CandidatePage)
        candidateidlabel = Label(self.CandidatePage, text = "Candidate ID", font = ("Arial", 15), bg = "white")
        candidateidlabel.grid(row = 5, column = 1)
        self.CandidateIdEntry.grid(row = 5, column = 5)

        self.ForenameEntry = Entry(self.CandidatePage)
        ForenameLabel = Label(self.CandidatePage, text = "Forename", font = ("Arial", 15), bg = "white")
        ForenameLabel.grid(row = 6, column = 1)
        self.ForenameEntry.grid(row = 6, column = 5)

        self.SurnameEntry = Entry(self.CandidatePage)
        SurnameLabel = Label(self.CandidatePage, text = "Surname", font = ("Arial", 15), bg = "white")
        SurnameLabel.grid(row = 7, column = 1)
        self.SurnameEntry.grid(row = 7, column = 5)

        self.DOBEntry = Entry(self.CandidatePage)
        DOBLabel = Label(self.CandidatePage, text = "Date of Birth", font = ("Arial", 15), bg = "white")
        DOBLabel.grid(row = 8, column = 1)
        self.DOBEntry.grid(row = 8, column = 5)

        self.EmailEntry = Entry(self.CandidatePage)
        EmailLabel = Label(self.CandidatePage, text = "Email Address", font = ("Arial", 15), bg = "white")
        EmailLabel.grid(row = 9, column = 1)
        self.EmailEntry.grid(row = 9, column = 5)

        self.PhoneNoEntry = Entry(self.CandidatePage)
        PhoneNoLabel = Label(self.CandidatePage, text = "Phone Number", font = ("Arial", 15), bg = "white")
        PhoneNoLabel.grid(row = 10, column = 1)
        self.PhoneNoEntry.grid(row = 10, column = 5)

##        self.RoleEntry = Entry(self.CandidatePage)
##        RoleLabel = Label(self.CandidatePage, text = "Role", font = ("Arial", 15), bg = "white")
##        RoleLabel.grid(row = 11, column = 1)
##        self.RoleEntry.grid(row = 11, column = 5)

        self.SalaryEntry = Entry(self.CandidatePage)
        SalaryLabel = Label(self.CandidatePage, text = "Salary", font = ("Arial", 15), bg = "white")
        SalaryLabel.grid(row = 12, column = 1)
        self.SalaryEntry.grid(row = 12, column = 5)

        
        logo1 = PhotoImage (file="recruitment.gif")
        logoLabel2 = Label(self.CandidatePage,image=logo1)
        logoLabel2.photo = logo1
        logoLabel2.grid(row = 0, column = 1)
##        Entry = self.CandidateIdEntry, self.ForenameEntry, self.SurnameEntry, self.DOBEntry, self.EmailEntry, self.PhoneNoEntry, self.SalaryEntry

        InsertButton = Button(self.CandidatePage, text = "Insert Data",bg="red",fg="white",command = lambda: self.InsertData())
        InsertButton.grid(row = 13, column = 5)

        DisplayButton = Button(self.CandidatePage, text = "Display Data",bg="red",fg="white",command = lambda: self.DisplayData(sqlview))
        DisplayButton.grid(row = 14, column = 5)

##        ClearCandidateButton = Button(self.CandidatePage, text = "Clear Entries",bg="red",fg="white",command = lambda: self.ClearEntry(Entry))
##        ClearCandidateButton.grid(row = 15, column = 5)

        
        TitleLabel.grid(row = 1, column = 0,padx = 10, pady = 10)
        MenuButton.grid(row = 0, column = 0)
        

##        root = Tk()
##        root.title("recruitment")
##        root.config(bg = "lightgreen",height = 800, width = 800)
##        TitleLabel = Label(root,text = "Candidate Data screen",font=("Ariel",24,"bold"), bg="lightgreen")

      
        sqlview = tkinter.ttk.Treeview(self.CandidatePage)
        sqlview["columns"] = ("c1","c2","c3","c4","c5","c6","c7","c8","c9","c10")
        sqlview.heading("c1",text = "CandidateId")
        sqlview.heading("c2",text = "forename")
        sqlview.heading("c3",text = "surname")
        sqlview.heading("c4",text = "DOB")
        sqlview.heading("c5",text = "Email Address")
        sqlview.heading("c6",text = "phone number")
        sqlview.heading("c7",text = "Salary")
##        sqlview.heading("c8",text = "role Wanted")

        sqlview.column("c1",width = "100")
        sqlview.column("c2",width = "100")
        sqlview.column("c3",width = "100")
        sqlview.column("c4",width = "100")
        sqlview.column("c5",width = "100")
        sqlview.column("c6",width = "100")
        sqlview.column("c7",width = "100")
##        sqlview.column("c8",width = "100")
        
        sqlview.column("#0",width = 0, stretch = "no")
        sqlview.column("#9",width = 0, stretch = "no")
        sqlview.column("#10",width = 0, stretch = "no")

        sqlview.config(height = 20)
        sqlview.grid(row=50,column=0,pady=10,padx=10)

        self.ForenameEntry.bind("<FocusOut>",lambda e:self.validateName(self.ForenameEntry))
        self.SurnameEntry.bind("<FocusOut>",lambda e:self.validateName(self.SurnameEntry))
##        self.RoleEntry.bind("<FocusOut>",lambda e:self.validateName(self.RoleEntry))

    def InsertData(self):
        CandidateIdEntry = self.CandidateIdEntry.get()
        ForenameEntry = self.ForenameEntry.get()
        SurnameEntry = self.SurnameEntry.get()
        DOBEntry = self.DOBEntry.get()
        EmailEntry = self.EmailEntry.get()
        PhoneNoEntry = self.PhoneNoEntry.get()
##        RoleEntry = self.RoleEntry.get()
        SalaryEntry = self.SalaryEntry.get()

        conn = sqlite3.connect('database project1.db')
##        DDL = '''CREATE TABLE if not exists CANDIDATE(
##                 Candidateid INTEGER PRIMARY KEY,
##                 forename  VARCHAR(15),
##                 surname   VARCHAR(15),
##                 age       INTEGER,
##                 EmailAddress TEXT,
##                 Salary INTEGER,
##                 Salary TEXT,
##                 RoleWanted  TEXT REFERENCES [Roles]([Role of job]))'''
##        
##        try:
##            conn.execute(DDL)
##            print("Candidate table created/exists")
##        except sqlite3.Error as err:
##            print("An error occured",err)

        CandidateData = (CandidateIdEntry, ForenameEntry, SurnameEntry, DOBEntry, EmailEntry, PhoneNoEntry, SalaryEntry)
        DML = "INSERT INTO CANDIDATE(Candidateid, forename, surname, DOB, EmailAddress, PhoneNo, Salary)"
        DML += "VALUES" + str(CandidateData)
        
        try:
            conn.execute(DML)
            conn.commit()
            print("Data added")
        except sqlite3.Error as err:
            print("An error occured",err)

##    def ClearEntry(self, Entry):
##        for entry in Entry:
##            entry.delete(0,END)

        
    def DisplayData(self, sqlview):
        conn = sqlite3.connect('database project1.db')
        sqlstr = "SELECT * FROM CANDIDATE"
        print(sqlstr)
        result = conn.execute(sqlstr).fetchall()
     
        #result = conn.fetchall()
        print(result)
        count = 0
        for row in result:
            sqlview.insert("",count,text="",values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
            count+=1

    def validateName(self, entry):
        valid = True
        name = entry.get()
        for ch in name:
            if ch.upper() not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                valid = False
        if not valid:
            entry.config(bg = "red")
            showerror("ERROR!!!! Must be letters only!")
            entry.delete(0,END)
            entry.focus_set()
            entry.config(bg = "white")

    def Populate_comboBox(self):
        self.listbox = Listbox(self.RolePage, height = 5, width = 20)
        self.listbox.grid(row=7, column =5)

        conn = sqlite3.connect('database project1.db')
        curs = conn.cursor()
        curs.execute("SELECT Clientid FROM CLIENT")
        tableData = curs.fetchall()
        print(tableData)

        for Clientid in tableData:
            self.listbox.insert(END,(Clientid[0]))

    def show_selected_data(self):
        try:
            index = int(self.listbox.curselection()[0])
            print(index)
            value = self.listbox.get(index)
            print(value)

            conn = sqlite3.connect('database project1.db')  
            curs = conn.cursor()  

            sql = "SELECT * FROM CLIENT WHERE Clientid = ?"
            curs.execute(sql, (value,))

            result = curs.fetchone()
            print(result)

            conn.close()

        except IndexError:
            print("No item selected.")

    def CreateClientPage(self): 
        TitleLabel = Label(self.ClientPage, text = "Client Page", font = ("Arial", 40), bg = "white")
        MenuButton = Button(self.ClientPage, text = "Back",bg="red",fg="white",command = lambda: self.SwitchPage(self.MenuPage,self.ClientPage))

        self.ClientIdEntry = Entry(self.ClientPage)
        ClientIdLabel = Label(self.ClientPage, text = "Client Id", font = ("Arial", 15), bg = "white")
        ClientIdLabel.grid(row = 1, column = 1)
        self.ClientIdEntry.grid(row = 1, column = 5)

        self.forenameEntry = Entry(self.ClientPage)
        forenameLabel = Label(self.ClientPage, text = "Forename", font = ("Arial", 15), bg = "white")
        forenameLabel.grid(row = 2, column = 1)
        self.forenameEntry.grid(row = 2, column = 5)

        self.surnameEntry = Entry(self.ClientPage)
        surnameLabel = Label(self.ClientPage, text = "Surname", font = ("Arial", 15), bg = "white")
        surnameLabel.grid(row = 3, column = 1)
        self.surnameEntry.grid(row = 3, column = 5)

        self.emailEntry = Entry(self.ClientPage)
        emailLabel = Label(self.ClientPage, text = "Email", font = ("Arial", 15), bg = "white")
        emailLabel.grid(row = 4, column = 1)
        self.emailEntry.grid(row = 4, column = 5)

        self.CompanyNameEntry = Entry(self.ClientPage)
        CompanyNameLabel = Label(self.ClientPage, text = "Company Name", font = ("Arial", 15), bg = "white")
        CompanyNameLabel.grid(row = 5, column = 1)
        self.CompanyNameEntry.grid(row = 5, column = 5)

        self.PhoneNumberEntry = Entry(self.ClientPage)
        PhoneNumberLabel = Label(self.ClientPage, text = "Phone Number", font = ("Arial", 15), bg = "white")
        PhoneNumberLabel.grid(row = 6, column = 1)
        self.PhoneNumberEntry.grid(row = 6, column = 5)

        logo3 = PhotoImage (file="recruitment.gif")
        logoLabel3 = Label(self.ClientPage,image=logo3)
        logoLabel3.photo = logo3
        logoLabel3.grid(row = 0, column = 10)

##        self.roleEntry = Entry(self.ClientPage)
##        roleLabel = Label(self.ClientPage, text = "Role", font = ("Arial", 15), bg = "yellow")
##        roleLabel.grid(row = 7, column = 1)
##        self.roleEntry.grid(row = 7, column = 5)

        InsertButton = Button(self.ClientPage, text = "Insert",bg="red",fg="white",command = lambda: self.Insert_Client())
        InsertButton.grid(row = 8, column = 5)

        DisplayButton = Button(self.ClientPage, text = "Display",bg="red",fg="white",command = lambda: self.Display())
        DisplayButton.grid(row = 9, column = 5)

        TitleLabel.grid(row = 0, column = 0, padx = 50, pady = 50)
        MenuButton.grid(row = 1, column = 0)

##        root = Tk()
##        root.title("recruitment")
##        root.config(bg = "lightgreen",height = 800, width = 800)
##        TitleLabel = Label(root,text = "Cient Data screen",font=("Ariel",24,"bold"), bg="lightgreen")

        sqlview = tkinter.ttk.Treeview(self.ClientPage)

        sqlview["columns"] = ("c1","c2","c3","c4","c5","c6","c7","c8","c9","c10")
        sqlview.heading("c1",text = "clientId")
        sqlview.heading("c2",text = "forename")
        sqlview.heading("c3",text = "surname")
        sqlview.heading("c4",text = "Email Address")
        sqlview.heading("c5",text = "Company Name")
        sqlview.heading("c6",text = "phone number")

        sqlview.column("c1",width = "100")
        sqlview.column("c2",width = "100")
        sqlview.column("c3",width = "100")
        sqlview.column("c4",width = "100")
        sqlview.column("c5",width = "100")
        sqlview.column("c6",width = "100")
        sqlview.column("c7",width = "100")

        sqlview.column("#0",width = 0, stretch = "no")
        sqlview.column("#8",width = 0, stretch = "no")
        sqlview.column("#9",width = 0, stretch = "no")
        sqlview.column("#10",width = 0, stretch = "no")

        sqlview.grid(row=50,column=0,pady=10,padx=10)

##        conn = sqlite3.connect('database project lol.db')
##        print("database opened")
##
##        DDL = '''CREATE TABLE if not exists Client (
##                 Clientid    TEXT PRIMARY KEY,
##                 forename       TEXT,
##                 surname        TEXT,
##                 Age            TEXT,
##                 Email          TEXT,
##                 PhoneNo        TEXT,
##                 Role         TEXT REFERENCES [Roles ] ([Role of job])'''
##        try:
##                conn.execute(DDL)
##                print("Student table created/exists")
##        except sqlite3.Error as err:
##            print("An error occured",err)
        

    def Insert_Client(self):
        try:
            conn = sqlite3.connect('database project1.db')
            cursor = conn.cursor()

            ClientIdEntry = self.ClientIdEntry.get()
            forenameEntry = self.forenameEntry.get()                                                                
            surnameEntry = self.surnameEntry.get()
            emailEntry = self.emailEntry.get()
            CompanyNameEntry = self.CompanyNameEntry.get()
            PhoneNumberEntry = self.PhoneNumberEntry.get()
##        roleEntry = self.roleEntry.get()


            ClientData = (ClientIdEntry, forenameEntry, surnameEntry, emailEntry, CompanyNameEntry, PhoneNumberEntry)
            DML = "INSERT INTO Client(Clientid, forename, surname,Email, CompanyName, PhoneNo)"
            cursor.execute(DML, ClientData)

            conn.commit()
            print("Data added")
        except sqlite3.Error as err:
            print("An error occured",err)
        conn.close  
      
##        DML += "VALUES" + str(ClientData)
##        try:
##            print(DML)
##            conn.execute(DML)
##            conn.commit()
##            print("Data added")
##        except sqlite3.Error as err:
##            print("An error occured",err)
##        conn.close()
    def Display(self, sqlview):
        conn = sqlite3.connect('database project1.db')
        sqlstr = "SELECT * FROM CLIENT"
        print(sqlstr)
        result = conn.execute(sqlstr).fetchall()
     
        #result = conn.fetchall()
        print(result)
        count = 0
        for row in result:
            sqlview.insert("",count,text="",values=(row[0],row[1],row[2],row[3],row[4],row[5]))
            count+=1

    def CreateRolePage(self):
        TitleLabel = Label(self.RolePage,  text = "Role Page", font = ("Arial", 40), bg = "white")
        MenuButton = Button(self.RolePage, text = "Back",bg="red",fg="white",command = lambda: self.SwitchPage(self.MenuPage,self.RolePage))

        TitleLabel.grid(row = 1, column = 50, padx = 50, pady = 50)
        MenuButton.grid(row = 1, column = 0)

        self.RoleOfJobEntry = Entry(self.RolePage)
        RoleOfJobLabel = Label(self.RolePage, text = "Role of Job", font = ("Arial", 15), bg = "white")
        RoleOfJobLabel.grid(row = 5, column = 1)
        self.RoleOfJobEntry.grid(row = 5, column = 5)
        
        self.SalaryEntry = Entry(self.RolePage)
        SalaryLabel = Label(self.RolePage, text = "Salary", font = ("Arial", 15), bg = "white")
        SalaryLabel.grid(row = 6, column = 1)
        self.SalaryEntry.grid(row = 6, column = 5)

        entries = self.RoleOfJobEntry, self.SalaryEntry

##        self.ClientidEntry = Entry(self.RolePage)
        ClientidLabel = Label(self.RolePage, text = "Client Id", font = ("Arial", 15), bg = "white")
        ClientidLabel.grid(row = 7, column = 1)
##        self.ClientidComboBox.grid(row = 7, column = 5)

        InsertIntoButton = Button(self.RolePage, text = "Insert",bg="red",fg="white",command = lambda: self.Insert())
        InsertIntoButton.grid(row = 8, column = 5)

        displayButton = Button(self.RolePage, text = "Display",bg="red",fg="white",command = lambda: self.Insert())
        displayButton.grid(row = 9, column = 5)

        Role2Button = Button(self.RolePage, text = "Go to Rolepage2",bg="red",fg="white",command = lambda: self.SwitchPage(self.RolePage2,self.RolePage))
        Role2Button.grid(row = 10, column = 5)

        ClearEntriesButton = Button(self.RolePage, text = "Clear Entries",bg="red",fg="white",command = lambda: self.Clear_Entry(entries))
        ClearEntriesButton.grid(row = 11, column =5)

        CalculateButton = Button(self.RolePage, text = "Calculate button",bg="red",fg="white",command = lambda: self.Calculate()) 
        CalculateButton.grid(row = 12, column = 5)
##        Role2Button = Button(self.RolePage2, text = "Go to RolePage2",bg="red",fg="white",command = lambda: self.SwitchPage(self.RolePage2,self.RolePage)) 
##        Role2Button.grid(row = 2, column = 0)
##        root = Tk()
##        root.title("recruitment")
##        root.config(bg = "lightgreen",height = 800, width = 800)
##        TitleLabel = Label(root,text = "Role Data screen",font=("Ariel",24,"bold"), bg="lightgreen")

        sqlview = tkinter.ttk.Treeview(self.RolePage2)

        sqlview["columns"] = ("c1","c2","c3","c4","c5","c6","c7","c8","c9","c10")
        sqlview.heading("c1",text = "Role of Job")
        sqlview.heading("c2",text = "Salary")
##        sqlview.heading("c3",text = "client id")

        sqlview.column("c1",width = "100")
        sqlview.column("c2",width = "100")
        sqlview.column("c3",width = "100")

        sqlview.column("#0",width = 0, stretch = "no")
        sqlview.column("#4",width = 0, stretch = "no")
        sqlview.column("#5",width = 0, stretch = "no")
        sqlview.column("#6",width = 0, stretch = "no")
        sqlview.column("#7",width = 0, stretch = "no")
        sqlview.column("#8",width = 0, stretch = "no")
        sqlview.column("#9",width = 0, stretch = "no")
        sqlview.column("#10",width = 0, stretch = "no")
        
        sqlview.grid(row=50,column=0,pady=5,padx=5)

##        conn = sqlite3.connect('database project lol.db')
##        print("database opened")
##
##
##        DDL = '''CREATE TABLE if not exists Roles(
##              RoleOfJob TEXT PRIMARY KEY,
##              salary        TEXT,
##              clientId      TEXT)'''
##        try:
##            conn.execute(DDL)
##            print("Student table created/exists")
##        except sqlite3.Error as err:
##           print("An error occured",err)
        self.RoleOfJobEntry.bind("<FocusOut>",lambda e:self.validateName(self.RoleOfJobEntry))
        
    def Insert(self):
        RoleOfJobEntry = self.RoleOfJobEntry.get()
        SalaryEntry = self.SalaryEntry.get()
##        ClientidEntry= self.ClientidEntry.get()

##        conn = sqlite3.connect('database project2.db')
##        DDL = '''CREATE TABLE if not exists Roles(
##                 RoleOfJob TEXT PRIMARY KEY,
##                 salary        TEXT,
##                 clientId      TEXT)'''
##        try:
##            conn.execute(DDL)
##            print("Student table created/exists")
##        except sqlite3.Error as err:
##           print("An error occured",err)
           
        RoleData = (RoleOfJobEntry, SalaryEntry)
        DML = "INSERT INTO ROLES(RoleOfJob, salary)"
        DML += "VALUES" + str(RoleData)

        try:
            conn.execute(DML)
            conn.commit()
            print("Data added")
        except sqlite3.Error as err:
            print("An error occured",err)

    def Display_Data(self, sqlview):
           conn = sqlite3.connect('database project1.db')
           sqlstr = "SELECT * FROM ROLES"
           print(sqlstr)
           result = conn.execute(sqlstr).fetchall()
         
           #result = conn.fetchall()
           print(result)
           count = 0
           for row in result:
               sqlview.insert("",count,text="",values=(row[0],row[1],row[2],row[3],row[4],row[5]))
               count+=1

    def Clear_Entry(self, entries):
        for entry in entries:
            entry.delete(0,END)

    def calculations(self):
        self.SalaryEntry = float(Self.SalaryEntry.get())
        if self.SalaryEntry > 12500:
            tax = 0.2
##            tax_cut = self.SalaryEntry * tax
##            actual_salary = self.SalaryEntry - tax_cut
##            return actual_salary
        elif self.SalaryEntry > 37700:
            tax = 0.4
##            tax_cut = self.SalaryEntry * tax
##            actual_salary = self.SalaryEntry - tax_cut
##            return actual_salary
        elif self.SalaryEntry > 125140:
            tax = 0.45
##            tax_cut = self.SalaryEntry * tax
##            actual_salary = self.SalaryEntry - tax_cut
##            return actual_salary
        else:
            tax = 0
        tax_cut = self.SalaryEntry * tax
        actual_salary = self.SalaryEntry - tax_cut
        return actual_salary

    def CreateRolePage2(self):
        TitleLabel2 = Label(self.RolePage2,  text = "Role Page 2", font = ("Arial", 40), bg = "yellow")
        BackButton = Button(self.RolePage2, text = "Back",bg="red",fg="white",command = lambda: self.SwitchPage(self.RolePage,self.RolePage2))

        TitleLabel2.grid(row = 1, column = 50, padx = 50, pady = 50)
        BackButton.grid(row = 1, column = 0)

    def CreateMatchPage(self):
        TitleLabel = Label(self.MatchPage, text = "Match Page", font = ("Arial", 40), bg = "grey")
        BackButton = Button(self.MatchPage, text = "Back",bg="red",fg="white",command = lambda: self.SwitchPage(self.MenuPage,self.MatchPage))

        TitleLabel.grid(row = 1, column = 50, padx = 50, pady = 50)
        BackButton.grid(row = 1, column = 0)
        
    def SwitchPage(self,ToPage,FromPage):
        FromPage.grid_remove()
        ToPage.grid()
        
root = Tk()
root.title("Recruitment")
menu = ProjectMenu(root)# Make a Project menu object by calling the constructor
root.mainloop()
