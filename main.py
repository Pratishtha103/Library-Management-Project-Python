from tkinter import *
import pymysql
from tkinter.ttk import*
from PIL import Image as imim
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ReturnBook import *
from ViewBooks import *
from IssueBook import *
from search import *
import os 
 
mypass = "mysql1234"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

bookTable="books"
IssueTable="books_issued"
# Staff
# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue",fg="white").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue",fg='white', command = register_user).pack()
 

# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x300")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
    global masterpassword_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
    masterpassword_verify=StringVar()
 
    global username_login_entry
    global password_login_entry
    global masterpassword_login_entry
 
    Label(login_screen, text="Username ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Master Password * ").pack()
    masterpassword_login_entry = Entry(login_screen, textvariable=masterpassword_verify, show= '*')
    masterpassword_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()

# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 15)).pack()

# Implementing event on login button 
 
def login_verify():
    masterpassword="Libraryhost@1234"
    username1 = username_verify.get()
    password1 = password_verify.get()
    masterpassword1=masterpassword_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    masterpassword_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            if masterpassword1==masterpassword:
                Main()
            else:
                messagebox.showinfo('Access Denied','Authentication Failed')
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
#student
# register student window
def student_register():
    global student_register_screen
    student_register_screen = Toplevel(main_screen)
    student_register_screen.title("Register")
    student_register_screen.geometry("300x250")
   
    global student_username
    global student_password    
    global student_username_entry
    global student_password_entry
    student_username = StringVar()
    student_password = StringVar()
    
    Label(student_register_screen, text="Please enter details below",fg="black").pack()
    Label(student_register_screen, text="").pack()
    username_lable = Label(student_register_screen, text="Username ")
    username_lable.pack()
    student_username_entry = Entry(student_register_screen, textvariable=student_username)
    student_username_entry.pack()
    password_lable = Label(student_register_screen, text="Password * ")
    password_lable.pack()
    student_password_entry = Entry(student_register_screen,textvariable=student_password, show='*')
    student_password_entry.pack()
    Label(student_register_screen, text="").pack()
    Button(student_register_screen, text="Register", width=10, height=1, bg="blue",fg='white', command = register_student).pack()
#login student window
def student_login():
    global student_login_screen
    student_login_screen = Toplevel(main_screen)
    student_login_screen.title("Login")
    student_login_screen.geometry("300x300")
    Label(student_login_screen, text="Please enter details below to login").pack()
    Label(student_login_screen, text="").pack()
 
    global student_username_verify
    global student_password_verify
    student_username_verify = StringVar()
    student_password_verify = StringVar()
 
    global student_username_login_entry
    global student_password_login_entry
 
    Label(student_login_screen, text="Username ").pack()
    student_username_login_entry = Entry(student_login_screen, textvariable=student_username_verify)
    student_username_login_entry.pack()
    Label(student_login_screen, text="").pack()
    Label(student_login_screen, text="Password * ").pack()
    student_password_login_entry = Entry(student_login_screen, textvariable=student_password_verify, show= '*')
    student_password_login_entry.pack()
    Label(student_login_screen, text="").pack()
    Button(student_login_screen, text="Login", width=10, height=1, command = student_login_verify).pack()

# registeration of student
def register_student():
    student_username_info = student_username.get()
    student_password_info = student_password.get()
    file = open(student_username_info, "w")
    file.write(student_username_info + "\n")
    file.write(student_password_info)
    file.close()
 
    student_username_entry.delete(0, END)
    student_password_entry.delete(0, END)
 
    Label(student_register_screen, text="Registration Success",fg="green", font=("calibri", 15)).pack()

# student login verify
 
def student_login_verify():
    student_username1 = student_username_verify.get()
    student_password1 = student_password_verify.get()
    student_username_login_entry.delete(0, END)
    student_password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if student_username1 in list_of_files:
        file1 = open(student_username1, "r")
        student_verify = file1.read().splitlines()
        if student_password1 in student_verify:
            student_main()
        else:
            password_not_recognised()
    else:
        user_not_found()
 
#student password not recognised
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(student_login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(student_login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
def Quit():
    main_screen.destroy()
def sQuit():
    main_screen.destroy()
def openfile():
    os.system("demo.py")
#student Window
def student_main():
    global main_screen
    sroot=Toplevel(main_screen)
    sroot.title("Library")
    sroot.minsize(width=400,height=400)
    sroot.geometry("600x600")
    Canvas1 = Canvas(sroot) 
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(sroot,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="Welcome to Library", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(sroot,text="Search Book",bg='black', fg='white',command=searchBook)
    btn1.place(relx=0.28,rely=0.45, relwidth=0.45,relheight=0.1)
    
    btn6 = Button(sroot,text="Exit",bg='black', fg='white',command=sQuit)
    btn6.place(relx=0.28,rely=0.55, relwidth=0.45,relheight=0.1)
    sroot.mainloop()

#Library Window    
def Main():
    global main_screen
    global login_success_screen
    root=Toplevel(main_screen)
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x600")
    # photo =PhotoImage(file="lib.jpg")

    # # Resize the image
    # photo = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)

    # # Convert the image to a Tkinter-compatible format
    # img = ImageTk.PhotoImage(img)
    # background_image = ImageTk.PhotoImage(img)
    # background_label = Label(root, image=background_image)
    # background_label.place(x=0, y=0, relwidth=1, relheight=1)
    #background
    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH) 

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="Welcome to Library", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(root,text="Add Book Details",bg='black', fg='white',command=addBook)
    btn1.place(relx=0.28,rely=0.35, relwidth=0.45,relheight=0.1)

    btn2 = Button(root,text="Delete Book",bg='black', fg='white',command=delete)
    btn2.place(relx=0.28,rely=0.45, relwidth=0.45,relheight=0.1)
        
    btn3 = Button(root,text="View Book List",bg='black', fg='white',command=View)
    btn3.place(relx=0.28,rely=0.55, relwidth=0.45,relheight=0.1)
        
    btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white',command=issueBook)
    btn4.place(relx=0.28,rely=0.65, relwidth=0.45,relheight=0.1)

    btn5 = Button(root,text="Return Book",bg='black', fg='white',command=returnBook)
    btn5.place(relx=0.28,rely=0.75, relwidth=0.45,relheight=0.1)
        
    btn6 = Button(root,text="Exit",bg='black', fg='white',command=Quit)
    btn6.place(relx=0.28,rely=0.85, relwidth=0.45,relheight=0.1)
    root.mainloop()

#staff window
def staff():
    global staff_screen
    staff_screen = Toplevel(main_screen)
    staff_screen.geometry("300x250")
    staff_screen.title("Staff Account")
    Label(staff_screen,text="Select Your Choice", bg="blue",fg='white', width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(staff_screen,text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(staff_screen,text="Register", height="2", width="30", command=register).pack()
#student window
def student():
    global student_screen
    student_screen = Toplevel(main_screen)
    student_screen.geometry("300x250")
    student_screen.title("Student Account")
    Label(student_screen,text="Select Your Choice", bg="blue",fg='white', width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(student_screen,text="Login", height="2", width="30", command = student_login).pack()
    Label(text="").pack()
    Button(student_screen,text="Register", height="2", width="30", command=student_register).pack()
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Library Account")
    Label(text="Select Your Choice", bg="blue",fg='white', width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Staff", height="2", width="30", command = staff).pack()
    Label(text="").pack()
    Button(text="Student", height="2", width="30", command=student).pack()
    main_screen.mainloop()
main_account_screen()