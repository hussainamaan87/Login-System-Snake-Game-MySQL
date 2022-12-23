from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import random
import mysql.connector
mycon=mysql.connector.connect(host="localhost",user='root',passwd='1234',database='airlines')
cursor=mycon.cursor()
mycon.autocommit=True



def game_win():
    
    import random
      
    # Create Object
    root = Tk()
      
    # Set geometry
    root.geometry("300x300")
      
    # Set title
    root.title("Rock Paper Scissor Game")
      
    # Computer Value
    computer_value = {
        "0":"Rock",
        "1":"Paper",
        "2":"Scissor"
    }
      
    # Reset The Game
    def reset_game():
        b1["state"] = "active"
        b2["state"] = "active"
        b3["state"] = "active"
        l1.config(text = "Player              ")
        l3.config(text = "Computer")
        l4.config(text = "")
      
    # Disable the Button
    def button_disable():
        b1["state"] = "disable"
        b2["state"] = "disable"
        b3["state"] = "disable"
      
    # If player selected rock
    def isrock():
        c_v = computer_value[str(random.randint(0,2))]
        if c_v == "Rock":
            match_result = "Match Draw"
        elif c_v=="Scissor":
            match_result = "Player Win"
        else:
            match_result = "Computer Win"
        l4.config(text = match_result)
        l1.config(text = "Rock            ")
        l3.config(text = c_v)
        button_disable()
      
    # If player selected paper
    def ispaper():
        c_v = computer_value[str(random.randint(0, 2))]
        if c_v == "Paper":
            match_result = "Match Draw"
        elif c_v=="Scissor":
            match_result = "Computer Win"
        else:
            match_result = "Player Win"
        l4.config(text = match_result)
        l1.config(text = "Paper           ")
        l3.config(text = c_v)
        button_disable()
      
    # If player selected scissor
    def isscissor():
        c_v = computer_value[str(random.randint(0,2))]
        if c_v == "Rock":
            match_result = "Computer Win"
        elif c_v == "Scissor":
            match_result = "Match Draw"
        else:
            match_result = "Player Win"
        l4.config(text = match_result)
        l1.config(text = "Scissor         ")
        l3.config(text = c_v)
        button_disable()
      
    # Add Labels, Frames and Button
    Label(root,
          text = "Rock Paper Scissor",
          font = "normal 20 bold",
          fg = "blue").pack(pady = 20)
      
    frame = Frame(root)
    frame.pack()
      
    l1 = Label(frame,
               text = "Player              ",
               font = 10)
      
    l2 = Label(frame,
               text = "VS             ",
               font = "normal 10 bold")
      
    l3 = Label(frame, text = "Computer", font = 10)
      
    l1.pack(side = LEFT)
    l2.pack(side = LEFT)
    l3.pack()
      
    l4 = Label(root,
               text = "",
               font = "normal 20 bold",
               bg = "white",
               width = 15 ,
               borderwidth = 2,
               relief = "solid")
    l4.pack(pady = 20)
      
    frame1 = Frame(root)
    frame1.pack()
      
    b1 = Button(frame1, text = "Rock",
                font = 10, width = 7,
                command = isrock)
      
    b2 = Button(frame1, text = "Paper ",
                font = 10, width = 7,
                command = ispaper)
      
    b3 = Button(frame1, text = "Scissor",
                font = 10, width = 7,
                command = isscissor)
      
    b1.pack(side = LEFT, padx = 10)
    b2.pack(side = LEFT,padx = 10)
    b3.pack(padx = 10)
      
    Button(root, text = "Reset Game",
           font = 10, fg = "red",
           bg = "black", command = reset_game).pack(pady = 20)
      
    # Excecute Tkinter
    root.mainloop()























    





root_lm=Tk()
root_lm.geometry('400x500')
root_lm.title("LOGIN")
    
    
    #________bgimage__________
root_lm.bg=ImageTk.PhotoImage(file = "images/lmbg.png")
bg=Label(root_lm,image=root_lm.bg).place(x=0,y=0,width=400,height=500)

    #frame
frame_lm=Frame(root_lm,bg="#6A1B4D")
frame_lm.place(x=50,y=50, width=300, height=400)
    
wel_msg=Label(frame_lm,text="PLEASE LOGIN", font=("Calibri Light (Headings)",20,"bold"),bg="#6A1B4D",fg="white").place(x=50,y=10)
    
    #________l-image__________
lm_image=ImageTk.PhotoImage(Image.open("images/user_logo.png"))
lgn_image=Label(frame_lm,image=lm_image).place(x=100,y=45,width=100,height=100)

    #Insertion of user data
login_username=Label(frame_lm,text="ENTER USER NAME:", font=("Calibri Light (Headings)",15),bg="#6A1B4D",fg="White").place(x=50,y=150)
login_username_in=Entry(frame_lm,width=20,font=("Calibri Light (Headings)",15))
login_username_in.place(x=50,y=180)
login_pass=Label(frame_lm,text="ENTER PASSWORD:", font=("Calibri Light (Headings)",15),bg="#6A1B4D",fg="White").place(x=50,y=230)
login_pass_in=Entry(frame_lm,width=20,font=("Calibri Light (Headings)",15))
login_pass_in.place(x=50,y=260)

    


def login_btn():
    login_username_input=login_username_in.get()
    login_pass_input=login_pass_in.get()
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='airlines')
    cursor=mycon.cursor()
    mycon.autocommit=True
    if login_username_input=="" or login_pass_input=="":
        messagebox.showerror("ALL FIELDS ARE REQUIRED")
    else:
        try:
            c1="select fname, lname, email, user_name, pass1 from user_accounts where user_name='{}' and pass1='{}'".format(login_username_input,login_pass_input)
            cursor.execute(c1)
            data1=cursor.fetchall()[0]
            data1=list(data1)
            e_lg=data1[2]
            n_lg=data1[0]+''+data1[1]
            us_lg=data1[3]
            ps_lg=data1[4]
            print("login success")
            messagebox.showinfo("welcome: ",n_lg," email ",e_lg," user name ",us_lg)
                
        except:
            print("Login Failed")
    def root_btn_quit():
        root_btn.destroy()
            
    if login_username_input==us_lg:
        print("login good to go")
        root_btn=Tk()
        root_btn.geometry('200x100')
        
        start=Button(root_btn,text="START",width=8,bg="green",fg="white",font=("Calibri Light (Headings)",15,"bold"),command=game_win).place(x=100,y=0)
        quit_win=Button(root_btn,text="QUIT",width=8,bg="red",fg="white",font=("Calibri Light (Headings)",15,"bold"),command=root_btn_quit).place(x=100,y=50)
        root_lm.destroy()
        root_btn.mainloop()
    else:
        print("login not good to go")


    #LOGIN BUTTON_____
login=Button(frame_lm,text="LOGIN",width=10,bg="green",fg="white",font=("Calibri Light (Headings)",15,"bold"),command=login_btn).place(x=83,y=320)
    
root_lm.mainloop()
