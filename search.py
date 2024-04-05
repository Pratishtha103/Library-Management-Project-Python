from tkinter import *
from tkinter import ttk, messagebox
import pymysql
# Add your own database name and password here to reflect in the code
mypass = "mysql1234"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

def searchBook():
    global quitBtn
    sroot = Tk()
    sroot.title("Library")
    sroot.minsize(width=400,height=400)
    sroot.geometry("1500x1000")
    #background
    Canvas1 = Canvas(sroot) 
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH) 
    #heading frame
    headingFrame1 = Frame(sroot,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.01,relwidth=0.5,relheight=0.13)    
    headingLabel = Label(headingFrame1, text="Search Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    #table frame
    labelFrame = Frame(sroot, bg='black')
    labelFrame.place(relx=0.15,rely=0.3)
    
    #scrollbar

    table_scroll = Scrollbar(labelFrame)
    table_scroll.pack(side=RIGHT, fill=Y)

    table_scroll = Scrollbar(labelFrame,orient='horizontal')
    table_scroll.pack(side= BOTTOM,fill=X)

    table= ttk.Treeview(labelFrame,yscrollcommand=table_scroll.set, xscrollcommand =table_scroll.set)
    table.pack()

    table_scroll.config(command=table.yview)
    table_scroll.config(command=table.xview)
    table['columns'] = ('bid','title','author','status')
    # format our column
    table.column("#0", width=0,  stretch=NO)
    table.column("bid",width=100,anchor=CENTER)
    table.column("title",width=400,anchor=CENTER)
    table.column("author",width=300 ,anchor=CENTER)
    table.column("status",width=100,anchor=CENTER)
    table.heading("#0",text="",anchor=CENTER)
    table.heading("bid",text="BID")
    table.heading("title", text="Title")
    table.heading("author", text="Author")
    table.heading("status", text="Status")
    try:
        cur.execute('SELECT * FROM books')
        rows = cur.fetchall()
        con.commit()
        for row in rows:
            table.insert('',END, values=row)
    except:
        messagebox.showinfo("Error","Failed to fetch files from database")
    table.pack()
    quitBtn = Button(sroot,text="Quit",bg='#f7f1e3', fg='black', command=sroot.destroy)
    quitBtn.place(relx=0.43,rely=0.8, relwidth=0.18,relheight=0.08)

    sroot.mainloop()