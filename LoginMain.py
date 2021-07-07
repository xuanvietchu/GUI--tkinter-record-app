from tkinter import*
from tkinter import ttk
import sqlite3
from matplotlib import pyplot as plt
import os 

def main():
    global root
    root = Tk()
    root.geometry("500x500")
    root.config(bg="cadet blue")
    root.title("Workout management system")
    Label(text ="Workout management system",bg="Cadet blue", font =("Impact",30)).pack()
    Label(text ="",bg="Cadet blue").pack()

    photo = PhotoImage(file='image/Memelord.png')
    photo = photo.subsample(2,2)
    Label(root, image=photo).pack()

    Label(text ="",bg="Cadet blue").pack()
    Button(root, text ="Login",padx=10,pady=5,fg="white",bg="green",command = login).pack()
    Button(root,text="Register",padx=10,pady=5,fg="white",bg="green",command = register).pack()
    root.mainloop()

def backregister():
    root1.destroy()
    root.deiconify()

def register_user():
    username_info = username.get()
    password_info = password.get()
    name1_ = name_.get()
    age1_ = age_.get()
    gender1_ = gender_.get()
    height1_ = height_.get()
    weight1_ = weight_.get()
    list_user = os.listdir(r'C:\Users\T440\Desktop\work')
    if username_info +".db" not in list_user:
        db = sqlite3.connect(username_info +".db")
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS user(
        row integer NOT NULL,
        name text NOT NULL,
        age integer NOT NULL,
        gender text NOT NULL,
        height integer NOT NULL,
        weight integer NOT NULL
        )
        """)
        c.execute("""CREATE TABLE IF NOT EXISTS history(
        daynumber integer NOT NULL,
        khoidong integer NOT NULL,
        cotayrep integer NOT NULL,
        cotayset integer NOT NULL,
        cobungrep integer NOT NULL,
        cobungset integer NOT NULL,
        cochanrep integer NOT NULL,
        cochanset integer NOT NULL
        )
        """)
        c.execute("""CREATE TABLE IF NOT EXISTS userlogin(
        username VARCHAR NOT NULL,
        password VARCHAR NOT NULL 
        )
        """)
        c.execute("INSERT INTO userlogin VALUES (:username,:password)",
        	[username_info,password_info]
	    )
        c.execute("INSERT INTO user VALUES (:row,:name,:age,:gender,:height,:weight)",
        [1,name1_,age1_,gender1_,height1_,weight1_]
        )
        Label(root1, text="Registration is successful",fg= "green",bg="cadet blue",
                                                             font = ("calibri", 11)).pack()
        db.commit()
        db.close()
    else:
        Label(root1, text= username_info + " was taken, please try another name",
                                bg= "cadet blue",fg = "red",font = ("calibri", 11)).pack()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    gender_entry.delete(0, END)
    height_entry.delete(0, END)
    weight_entry.delete(0, END)

def register():
    global root1
    root.withdraw()
    root1= Toplevel(root)
    root1.title("Register")
    root1.geometry("600x600")
    root1.config(bg="cadet blue")
    global username
    global password
    global username_entry
    global password_entry
    global name_
    global age_
    global gender_
    global height_
    global weight_
    global name_entry
    global gender_entry
    global height_entry
    global weight_entry
    global age_entry
    username= StringVar()
    password= StringVar()
    name_= StringVar()
    age_= StringVar()
    gender_= StringVar()
    height_= StringVar()
    weight_= StringVar()
    Label(root1,text ="Enter the details below", bg="cadet blue",font =("Impact",30)).pack()
    Label(root1, bg="cadet blue",text = "Username*").pack()
    username_entry = Entry(root1, textvariable = username)
    username_entry.pack()
    Label(root1, bg="cadet blue",text = "Password*").pack()
    password_entry = Entry(root1, textvariable = password)
    password_entry.pack()
    Label(root1, text ="Real name", bg = "cadet blue").pack()
    name_entry = Entry(root1, textvariable = name_)
    name_entry.pack()
    Label(root1, text ="Age", bg = "cadet blue").pack()
    age_entry = Entry(root1, textvariable = age_)
    age_entry.pack()
    Label(root1, text ="Gender", bg = "cadet blue").pack()
    gender_entry = Entry(root1, textvariable = gender_)
    gender_entry.pack()
    Label(root1, text ="Height", bg = "cadet blue").pack()
    height_entry = Entry(root1, textvariable = height_)
    height_entry.pack()
    Label(root1, text ="Weight", bg = "cadet blue").pack()
    weight_entry = Entry(root1, textvariable = weight_)
    weight_entry.pack()
    Label(root1, text = "", bg ="cadet blue").pack()
    Button(root1, text = "Register", width = 7, height = 3, command = register_user).pack()
    Button(root1, text = "Back", width = 7, height = 3, command = backregister).pack()

def check_login():
    username1 = username_verify.get()
    password1 = password_verify.get()
    list_user = os.listdir(r"C:\Users\T440\Desktop\work")
    if username1 +".db" in list_user:
        db = sqlite3.connect(username1 +".db")
        c = db.cursor()
        c.execute("SELECT password FROM userlogin")
        checker = c.fetchall()
        if password1 in checker[0]:
            access_granted()
        else:
            wrong_password()
        db.commit()
        db.close()
    else:
        user_not_found()

def backlogin():
    root2.destroy()
    root.deiconify()

def wrong_password():
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    Label(root2, text ="Wrong password, please try again",fg = "red",bg ="cadet blue").pack()

def user_not_found():
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    Label(root2, text ="User not found",fg = "yellow", bg ="cadet blue").pack()
    
def access_granted():
    global root3
    root2.withdraw()
    root3 = Toplevel(root2)
    root3.title=("Workout system")
    root3.config(bg="cadet blue")
    root3.geometry("600x600")
    Label(root3, text="Login success", fg = "green", bg = "cadet blue").pack()
    Button(root3, text="Biography", width = 7, height =3, command = profile).pack()
    Button(root3, text="Start", width = 7, height =3, command = start).pack()
    Button(root3, text="History", width = 7, height =3, command = historyhub).pack()
    Button(root3, text="Back", width = 7, height =3, command = backaccess).pack()

def backaccess():
    root3.destroy()
    root2.deiconify()

def login():
    global root2
    root.withdraw()
    root2 = Toplevel(root)
    root2.title("Login")
    root2.geometry("500x500")
    root2.config(bg="cadet blue")
    Label(root2, text = "Type in the following information",bg="cadet blue",
                                                    font =("Impact",26)).pack()
    global username_verify
    global password_verify
    global username_entry1
    global password_entry1
    username_verify = StringVar()
    password_verify = StringVar()
    Label(root2,text = "Username",bg="cadet blue",font =("Calibri",20)).pack()
    username_entry1=Entry(root2, textvariable = username_verify)
    username_entry1.pack()
    Label(root2,text = "Password",bg="cadet blue",font =("Calibri",20)).pack()
    password_entry1=Entry(root2,show = "*", textvariable = password_verify)
    password_entry1.pack()
    Label(root2, text="",bg = "cadet blue").pack()
    Button(root2,text="Login", width = 7, height = 3, command = check_login).pack()
    Button(root2,text="Back", width = 7, height = 3, command = backlogin).pack()

def updateprofile():
    global personal_info
    name2 = name1.get()
    age2 = age1.get()
    gender2 = gender1.get()
    weight2 = weight1.get()
    height2 = height1.get()
    user_info = username_verify.get()
    db = sqlite3.connect(user_info +".db")
    c = db.cursor()
    c.execute("""UPDATE user SET name=? WHERE row = ?""",(name2,1))
    c.execute("""UPDATE user SET age=? WHERE row = ?""",(age2,1))
    c.execute("""UPDATE user SET gender=? WHERE row =?""",(gender2,1))
    c.execute("""UPDATE user SET weight=? WHERE row = ?""",(weight2,1))
    c.execute("""UPDATE user SET height=? WHERE row = ?""",(height2,1))
    db.commit()
    name_entry1.delete(0, END)
    age_entry1.delete(0, END)
    gender_entry1.delete(0, END)
    height_entry1.delete(0, END)
    weight_entry1.delete(0, END)
    label = Label(rootprofile, text ="Update success", bg = "cadet blue",fg = "green").grid(row=5,column = 0)
    db.close()

def backprofile():
    rootprofile.destroy()
    root3.deiconify()

def showinfo():
    global tree
    rootinfo = Toplevel(rootprofile)
    rootinfo.title=("Personal info")
    tree = ttk.Treeview(rootinfo, column=("c1", "c2", "c3","c4","c5"), show='headings')
    tree.column("#1", anchor=CENTER)
    tree.heading("#1", text="Name")
    tree.column("#2", anchor=CENTER)
    tree.heading("#2", text="Age")
    tree.column("#3", anchor=CENTER)
    tree.heading("#3", text="Gender")
    tree.column("#4", anchor=CENTER)
    tree.heading("#4", text="Height")
    tree.column("#5", anchor=CENTER)
    tree.heading("#5", text="Weight")
    tree.pack()

    user_info = username_verify.get()
    db = sqlite3.connect(user_info +".db")
    c = db.cursor()
    c.execute("SELECT name,age,gender,height,weight FROM user")
    rows = c.fetchall()    
    for row in rows:
        tree.insert("", END, values=row)        
    db.close()

def backprofile():
    rootprofile.destroy()
    root3.deiconify()

def profile():
    global rootprofile
    root3.withdraw()
    rootprofile = Toplevel(root3)
    rootprofile.title = ("Your profile")
    rootprofile.config(bg="cadet blue")
    rootprofile.geometry("600x600")
    global name1
    global age1
    global gender1
    global height1
    global weight1
    global name_entry1
    global age_entry1
    global gender_entry1
    global height_entry1
    global weight_entry1
    name1 = StringVar()
    age1 = StringVar()
    gender1 = StringVar()
    height1 = StringVar()
    weight1 = StringVar()
    Label(rootprofile, text ="Real name", bg = "cadet blue").grid(row=6,column = 0)
    name_entry1 = Entry(rootprofile, textvariable = name1)
    name_entry1.grid(row=6,column = 1)
    Label(rootprofile, text ="Age", bg = "cadet blue").grid(row=7,column = 0)
    age_entry1 = Entry(rootprofile, textvariable = age1)
    age_entry1.grid(row=7,column = 1)
    Label(rootprofile, text ="Gender", bg = "cadet blue").grid(row=8,column = 0)
    gender_entry1 = Entry(rootprofile, textvariable = gender1)
    gender_entry1.grid(row=8,column = 1)
    Label(rootprofile, text ="Height", bg = "cadet blue").grid(row=9,column = 0)
    height_entry1 = Entry(rootprofile, textvariable = height1)
    height_entry1.grid(row=9,column = 1)
    Label(rootprofile, text ="Weight", bg = "cadet blue").grid(row=10,column = 0)
    weight_entry1 = Entry(rootprofile, textvariable = weight1)
    weight_entry1.grid(row=10,column = 1)
    Button(rootprofile, text ="Show info", command = showinfo).grid(row=12,column = 1)
    Button(rootprofile, text ="Update", command = updateprofile).grid(row=11,column = 1)
    Button(rootprofile, text ="Back", command = backprofile).grid(row=13,column = 1)
def backstart():
    rootstart.destroy()
    root3.deiconify()

def submitstart():
    daynumber1 = daynumber.get()
    khoidong1 = khoidong.get()
    cotayrep1 = cotayrep.get()
    cotayset1 = cotayset.get()
    cobungrep1 = cobungrep.get()
    cobungset1 = cobungset.get()
    cochanrep1 = cochanrep.get()
    cochanset1 = cochanset.get()
    user_info = username_verify.get()
    db = sqlite3.connect(user_info +".db")
    c = db.cursor()
    c.execute("""INSERT INTO history VALUES 
    (:daynumber,:khoidong,:cotayrep,:cotayset,:cobungrep,:cobungset,:cochanrep,:cochanset)""",
    [daynumber1,khoidong1,cotayrep1,cotayset1,cobungrep1,cobungset1,cochanrep1,cochanset1]
    )        
    db.commit()
    db.close()
    Label(rootstart, text="Data is submitted",fg= "green",bg="cadet blue",font = ("calibri", 11)).grid(row=8,column = 2)

def start():
    global rootstart
    global khoidong
    global cotayrep
    global cotayset
    global cobungrep
    global cobungset
    global cochanrep
    global cochanset
    global daynumber
    khoidong = IntVar()
    cotayrep = IntVar()
    cotayset = IntVar()
    cobungrep = IntVar()
    cobungset = IntVar()
    cochanrep = IntVar()
    cochanset = IntVar()
    daynumber = IntVar()
    root3.withdraw()
    rootstart = Toplevel(root3)
    rootstart.title = ("Your profile")
    rootstart.config(bg="cadet blue")
    rootstart.geometry("600x600")
    Label(rootstart, text = "Repetition", bg = "cadet blue").grid(row=0,column = 1)
    Label(rootstart, text = "Set", bg = "cadet blue").grid(row=0,column = 2)
    Label(rootstart, text = "Time", bg = "cadet blue").grid(row=0,column = 3)
    Label(rootstart, text ="Khởi Động", bg = "cadet blue").grid(row=1,column = 0)
    khoidong_tg = Entry(rootstart, textvariable = khoidong)
    khoidong_tg.grid(row=1,column = 3)
    Label(rootstart, text ="Cơ tay", bg = "cadet blue").grid(row=2,column = 0)
    cotay_rep = Entry(rootstart, textvariable = cotayrep)
    cotay_rep.grid(row=2,column = 1)
    cotay_set = Entry(rootstart, textvariable = cotayset)
    cotay_set.grid(row=2,column = 2)
    Label(rootstart, text ="Cơ bụng", bg = "cadet blue").grid(row=3,column = 0)
    cobung_rep = Entry(rootstart, textvariable = cobungrep)
    cobung_rep.grid(row=3,column = 1)
    cobung_set = Entry(rootstart, textvariable = cobungset)
    cobung_set.grid(row=3,column = 2)
    Label(rootstart, text ="Chân", bg = "cadet blue").grid(row=4,column = 0)
    cochan_rep = Entry(rootstart, textvariable = cochanrep)
    cochan_rep.grid(row=4,column = 1)
    cochan_set = Entry(rootstart, textvariable = cochanset)
    cochan_set.grid(row=4,column = 2)
    Label(rootstart, text ="Day number", bg = "cadet blue").grid(row=5,column = 0)
    day_number = Entry(rootstart, textvariable = daynumber)
    day_number.grid(row=5,column = 1)
    Button(rootstart, text ="Submit", bg= "green", width = 6, height =3, command = submitstart).grid(row=6,column = 2)
    Button(rootstart, text ="End", bg= "green", width = 6, height =3, command = backstart).grid(row=7,column = 2)

def backhistory():
    roothistoryhub.destroy()
    root3.deiconify()

def viewhistory():
    user_info = username_verify.get()
    db = sqlite3.connect(user_info +".db")
    c = db.cursor()
    c.execute("SELECT * FROM history")
    rows = c.fetchall()    
    for row in rows:
        tree1.insert("", END, values=row)        
    db.close()
    
def history():
    global tree1
    roothistory = Toplevel(roothistoryhub)
    roothistory.title=("History")
    tree1 = ttk.Treeview(roothistory, column=("c1","c2","c3","c4","c5","c6","c7","c8"), show='headings')
    tree1.column("#1", anchor=CENTER,width = 90)
    tree1.heading("#1", text="Day number")
    tree1.column("#2", anchor=CENTER,width = 110)
    tree1.heading("#2", text="Khởi động")
    tree1.column("#3", anchor=CENTER,width = 110)
    tree1.heading("#3", text="Cơ tay rep")
    tree1.column("#4", anchor=CENTER,width = 110)
    tree1.heading("#4", text="Cơ tay set")
    tree1.column("#5", anchor=CENTER,width = 110)
    tree1.heading("#5", text="Cơ bụng rep")
    tree1.column("#6", anchor=CENTER,width = 110)
    tree1.heading("#6", text="Cơ bụng set")
    tree1.column("#7", anchor=CENTER,width = 110)
    tree1.heading("#7", text="Cơ chân rep")
    tree1.column("#8", anchor=CENTER,width = 110)
    tree1.heading("#8", text="Cơ chân set")
    tree1.pack()
    button = Button(roothistory,text="Display data", command=viewhistory)
    button.pack()

def edithistory():
    daynumber3 = daynumber2.get()
    khoidong3 = khoidong2.get()
    cotayrep3 = cotayrep2.get()
    cotayset3 = cotayset2.get()
    cobungrep3 = cobungrep2.get()
    cobungset3 = cobungset2.get()
    cochanrep3 = cochanrep2.get()
    cochanset3 = cochanset2.get()
    user_info = username_verify.get()
    db = sqlite3.connect(user_info +".db")
    c = db.cursor()
    c.execute("""UPDATE history SET khoidong=? WHERE daynumber = ?""",(khoidong3,daynumber3))
    c.execute("""UPDATE history SET cotayrep=? WHERE daynumber =?""",(cotayrep3,daynumber3))
    c.execute("""UPDATE history SET cotayset=? WHERE daynumber = ?""",(cotayset3,daynumber3))
    c.execute("""UPDATE history SET cobungrep=? WHERE daynumber = ?""",(cobungrep3,daynumber3))
    c.execute("""UPDATE history SET cobungset=? WHERE daynumber = ?""",(cobungset3,daynumber3))
    c.execute("""UPDATE history SET cochanrep=? WHERE daynumber = ?""",(cochanrep3,daynumber3))
    c.execute("""UPDATE history SET cochanset=? WHERE daynumber = ?""",(cochanset3,daynumber3))
    db.commit()
    label = Label(roothistoryhub, text ="Update success", bg = "cadet blue",fg = "green").grid(row=6,column = 0)
    db.close()

def historyselect():
    global tree2
    roothistoryselect = Toplevel(roothistoryhub)
    roothistoryselect.title=("History select")
    tree2 = ttk.Treeview(roothistoryselect, column=("c1","c2","c3","c4","c5","c6","c7","c8"), show='headings')
    tree2.column("#1", anchor=CENTER,width = 90)
    tree2.heading("#1", text="Day number")
    tree2.column("#2", anchor=CENTER,width = 110)
    tree2.heading("#2", text="Khởi động")
    tree2.column("#3", anchor=CENTER,width = 110)
    tree2.heading("#3", text="Cơ tay rep")
    tree2.column("#4", anchor=CENTER,width = 110)
    tree2.heading("#4", text="Cơ tay set")
    tree2.column("#5", anchor=CENTER,width = 110)
    tree2.heading("#5", text="Cơ bụng rep")
    tree2.column("#6", anchor=CENTER,width = 110)
    tree2.heading("#6", text="Cơ bụng set")
    tree2.column("#7", anchor=CENTER,width = 110)
    tree2.heading("#7", text="Cơ chân rep")
    tree2.column("#8", anchor=CENTER,width = 110)
    tree2.heading("#8", text="Cơ chân set")
    tree2.pack()
    selectday1 = selectday.get()
    user_info = username_verify.get()
    db = sqlite3.connect(user_info +".db")
    c = db.cursor()
    c.execute("SELECT * FROM history WHERE daynumber = ?",[selectday1])
    rows = c.fetchall()    
    for row in rows:
        tree2.insert("", END, values=row)        
    db.close()

def delete():
    selectday1 = selectday.get()
    user_info = username_verify.get()
    db = sqlite3.connect(user_info +".db")
    c = db.cursor()
    c.execute("DELETE FROM history WHERE daynumber = ?",[selectday1])
    db.commit()
    label = Label(roothistoryhub, text ="Update success", bg = "cadet blue",fg = "green").grid(row=7,column = 0)
    db.close()

def overall():
    user_info = username_verify.get()
    db = sqlite3.connect(user_info +".db")
    c = db.cursor()
    c.execute("SELECT SUM(cotayrep*cotayset) AS tay FROM history")
    tay= c.fetchone()
    c.execute("SELECT SUM(cobungrep*cobungset) AS bung FROM history")
    bung= c.fetchone()
    c.execute("SELECT SUM(cochanrep*cochanset) AS chan FROM history")
    chan= c.fetchone()
    label=["tay","bụng","chân"]
    data=[tay[0],bung[0],chan[0]]
    fig = plt.figure(figsize =(6, 6)) 
    plt.pie(data, labels = label,autopct='%.2f%%')
    plt.show()

def progress():
    user_info = username_verify.get()
    db = sqlite3.connect(user_info +".db")
    c = db.cursor()
    c.execute("""SELECT cotayrep*cotayset + cobungrep*cobungset + cochanrep*cochanset
                                AS progress, daynumber FROM history""")
    data = c.fetchall()
    day = []
    progress = []
    for row in data:
        day.append(row[1])
        progress.append(row[0])

    plt.plot(day,progress)
    plt.xlabel("Day Number")
    plt.ylabel("Repetition")
    plt.show()

def historyhub():
    global roothistoryhub
    root3.withdraw()
    roothistoryhub = Toplevel(root3)
    roothistoryhub.title = ("Workout History Hub")
    roothistoryhub.config(bg="cadet blue")
    roothistoryhub.geometry("600x600")
    global khoidong2
    global cotayrep2
    global cotayset2
    global cobungrep2
    global cobungset2
    global cochanrep2
    global cochanset2
    global daynumber2
    global selectday
    daynumber2 = IntVar()
    khoidong2 = IntVar()
    cotayrep2 = IntVar()
    cotayset2 = IntVar()
    cobungrep2 = IntVar()
    cobungset2 = IntVar()
    cochanrep2 = IntVar()
    cochanset2 = IntVar()
    selectday = IntVar()
    Label(roothistoryhub, text = "Repetition", bg = "cadet blue").grid(row=0,column = 1)
    Label(roothistoryhub, text = "Set", bg = "cadet blue").grid(row=0,column = 2)
    Label(roothistoryhub, text = "Time", bg = "cadet blue").grid(row=0,column = 3)
    Label(roothistoryhub, text ="Khởi Động", bg = "cadet blue").grid(row=1,column = 0)
    khoidong_tg = Entry(roothistoryhub, textvariable = khoidong2)
    khoidong_tg.grid(row=1,column = 3)
    Label(roothistoryhub, text ="Cơ tay", bg = "cadet blue").grid(row=2,column = 0)
    cotay_rep = Entry(roothistoryhub, textvariable = cotayrep2)
    cotay_rep.grid(row=2,column = 1)
    cotay_set = Entry(roothistoryhub, textvariable = cotayset2)
    cotay_set.grid(row=2,column = 2)
    Label(roothistoryhub, text ="Cơ bụng", bg = "cadet blue").grid(row=3,column = 0)
    cobung_rep = Entry(roothistoryhub, textvariable = cobungrep2)
    cobung_rep.grid(row=3,column = 1)
    cobung_set = Entry(roothistoryhub, textvariable = cobungset2)
    cobung_set.grid(row=3,column = 2)
    Label(roothistoryhub, text ="Chân", bg = "cadet blue").grid(row=4,column = 0)
    cochan_rep = Entry(roothistoryhub, textvariable = cochanrep2)
    cochan_rep.grid(row=4,column = 1)
    cochan_set = Entry(roothistoryhub, textvariable = cochanset2)
    cochan_set.grid(row=4,column = 2)
    Label(roothistoryhub, text ="Day number", bg = "cadet blue").grid(row=5,column = 0)
    day_number = Entry(roothistoryhub, textvariable = daynumber2)
    day_number.grid(row=5,column = 1)
    Button(roothistoryhub, text ="Change", width = 12, height =3, command = edithistory).grid(row=6,column = 2)
    Button(roothistoryhub, text ="View history", width = 12, height =3, command = history).grid(row=7,column = 2)
    Label(roothistoryhub, text ="Select day to view/delete", bg = "cadet blue").grid(row=9,column = 0)
    day = Entry(roothistoryhub, textvariable = selectday)
    day.grid(row=9,column = 1)
    Button(roothistoryhub, text ="Selective History", width = 12, height =3, command = historyselect).grid(row=9,column = 2)
    Button(roothistoryhub, text ="Selective Delete", width = 12, height =3, command = delete).grid(row=10,column = 2)
    Button(roothistoryhub, text ="Overall Graph", width = 12, height =3, command = overall).grid(row=11,column = 2)
    Button(roothistoryhub, text ="Progress Graph", width = 12, height =3, command = progress).grid(row=12,column = 2)   
    Button(roothistoryhub, text ="Back", width = 12, height =3, command = backhistory).grid(row=13,column = 2)

main()