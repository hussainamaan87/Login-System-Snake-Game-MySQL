from tkinter import *
from PIL import Image,ImageTk
import tkinter
from tkinter import messagebox
import mysql.connector
mycon=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='ARD_GAMES')
cursor=mycon.cursor()
mycon.autocommit=True

#WELCOME SCREEN



#LOGIN PANEL___________________________________________________________________________________________________________________

def login_menu():
    root_lm=Toplevel(root)
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
        mycon=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='ARD_GAMES')
        cursor=mycon.cursor()
        mycon.autocommit=True
        if login_username_input=="" or login_pass_input=="":
            print("All Fields are required")
        else:
            try:
                c1="select fname, lname, email from user_accounts where user_name='{}' and pass1='{}'".format(login_username_input,login_pass_input)
                cursor.execute(c1)
                print("login success;")
                data1=cursor.fetchall()[0]
                data1=list(data1)
                e_lg=data1[2]
                n_lg=data1[0]+' '+data1[1]
                
                messagebox.showinfo("Welcome","You are good to go:"+ " " + n_lg)
                return True
            except:
                print("Login Failed")
                return False

    #LOGIN BUTTON_____
    login=Button(frame_lm,text="LOGIN",width=10,bg="green",fg="white",font=("Calibri Light (Headings)",15,"bold"),command=login_btn).place(x=83,y=320)
    
    root_lm.mainloop()


#DELETE PANEL___________________________________________________________________________________________________________________

def delete_menu():
    root_dm=Toplevel(root)
    root_dm.geometry('700x400')
    root_dm.title("DELETE")
    
    #________bgimage__________
    root_dm.bg=ImageTk.PhotoImage(file = "images/del_bg.png")
    bg=Label(root_dm,image=root_dm.bg).place(x=0,y=0,width=700,height=400)

    #________l-image__________
    dm_image=ImageTk.PhotoImage(Image.open("images/del_l.png"))
    l_image=Label(root_dm,image=dm_image).place(x=50,y=50,width=300,height=300) 

    #frame
    frame_dm=Frame(root_dm,bg="brown")
    frame_dm.place(x=350,y=50, width=300, height=300)
    
    wel_msg=Label(frame_dm,text="ENTER YOUR INFO:", font=("Calibri Light (Headings)",20,"bold"),bg="brown",fg="white").place(x=20,y=10)

    #Insertion of user data
    delete_email=Label(frame_dm,text="EMAIL:", font=("Calibri Light (Headings)",15),bg="brown",fg="White").place(x=70,y=70)
    delete_email_in=Entry(frame_dm,width=15,font=("Calibri Light (Headings)",15))
    delete_email_in.place(x=70,y=100)
    delete_pass=Label(frame_dm,text="PASSWORD:", font=("Calibri Light (Headings)",15),bg="brown",fg="White").place(x=70,y=150)
    delete_pass_in=Entry(frame_dm,width=15,font=("Calibri Light (Headings)",15))
    delete_pass_in.place(x=70,y=180)


    def delete_btn():
        delete_email_input=delete_email_in.get()
        delete_pass_input=delete_pass_in.get()
        if delete_email_input=="" or delete_pass_input=="":
            print("All Fields are required")
        else:
            import mysql.connector
            mycon=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='ARD_GAMES')
            cursor=mycon.cursor()
            mycon.autocommit=True
            try:

            #acc confim yet to be made
                b1="delete from user_accounts where email='{}' and pass1='{}'".format(delete_email_input,delete_pass_input)
                cursor.execute(b1)
                print("account deleted")
                messagebox.showinfo("Delete Acc","Account:"+ delete_email_input+"-Deleted")
                return True
                
            except:
                messagebox.showerror("Error","Account does not exist")
        
        


    #DELETE BUTTON_____
    delete=Button(frame_dm,text="DELETE",width=10,bg="red",fg="white",font=("Calibri Light (Headings)",15,"bold"),command=delete_btn).place(x=90,y=230)
    
    root_dm.mainloop()


#REGISTRATION PANEL________________________________________________________________________________________________________________

def registration_menu():
    root_rm=Toplevel(root)
    root_rm.geometry('1200x700')
    root_rm.title("Regisration Panel")
    

    #________bgimage__________
    root_rm.bg=ImageTk.PhotoImage(file = "images/r_bg.png")
    bg=Label(root_rm,image=root_rm.bg).place(x=0,y=0,width=1200,height=700)

    
    #________l-image__________
    l_img=ImageTk.PhotoImage(Image.open("images/rm_l.png"))
    img_l=Label(root_rm,image=l_img).place(x=50,y=50,width=400,height=600)

    #Frame__________
    frame=Frame(root_rm,bg="BLACK")
    frame.place(x=450,y=50, width=700, height=600)
    msg=Label(frame,text="REGISTRATION FORM", font=("Calibri Light (Headings)",20,"bold"),fg="white",bg="BLACK").place(x=200,y=30)
    
        
    #input details_______________
    f_name=Label(frame,text="First Name:",font=("Calibri Light (Headings)",15,"bold"),bg="BLACK",fg="white").place(x=50,y=100)
    f_name_in=Entry(frame,font=("Calibri Light (Headings)",15,"bold"))
    f_name_in.place(x=50,y=130)

    l_name=Label(frame,text="Last Name:",font=("Calibri Light (Headings)",15,"bold"),bg="BLACK",fg="white").place(x=350,y=100)
    l_name_in=Entry(frame,font=("Calibri Light (Headings)",15,"bold"))
    l_name_in.place(x=350,y=130)

    email=Label(frame,text="Enter Email ID:",font=("Calibri Light (Headings)",15,"bold"),bg="BLACK",fg="white").place(x=50,y=180)
    email_in=Entry(frame,font=("Calibri Light (Headings)",15,"bold"))
    email_in.place(x=50,y=210)

    username=Label(frame,text="Enter User ID:",font=("Calibri Light (Headings)",15,"bold"),bg="BLACK",fg="white").place(x=350,y=180)
    username_in=Entry(frame,font=("Calibri Light (Headings)",15,"bold"))
    username_in.place(x=350,y=210)

    pass1=Label(frame,text="Enter Password:",font=("Calibri Light (Headings)",15,"bold"),bg="BLACK",fg="white").place(x=50,y=260)
    pass1_in=Entry(frame,font=("Calibri Light (Headings)",15,"bold"))
    pass1_in.place(x=50,y=290)

    pass2=Label(frame,text="Confirm Password:",font=("Calibri Light (Headings)",15,"bold"),bg="BLACK",fg="white").place(x=350,y=260)
    pass2_in=Entry(frame,font=("Calibri Light (Headings)n",15,"bold"))
    pass2_in.place(x=350,y=290)

    phno=Label(frame,text="Enter Phone No:",font=("Calibri Light (Headings)",15,"bold"),bg="BLACK",fg="white").place(x=50,y=340)
    phno_in=Entry(frame,font=("Calibri Light (Headings)",15,"bold"))
    phno_in.place(x=50,y=370)

    dob=Label(frame,text="DOB (DD|MM|YYYY):",font=("Calibri Light (Headings)",15,"bold"),bg="BLACK",fg="white").place(x=350,y=340)
    dob_in=Entry(frame,font=("Calibri Light (Headings)",15,"bold"))
    dob_in.place(x=350,y=370)

    gender=Label(frame,text="Gender (M,F or N):",font=("Calibri Light (Headings)",15,"bold"),bg="BLACK",fg="white").place(x=50,y=420)
    gender_in=Entry(frame,font=("Calibri Light (Headings)",15,"bold"))
    gender_in.place(x=50,y=450)

    age=Label(frame,text="Enter Age:",font=("Calibri Light (Headings)",15,"bold"),bg="BLACK",fg="white").place(x=350,y=420)
    age_in=Entry(frame,font=("Calibri Light (Headings)",15,"bold"))
    age_in.place(x=350,y=450)

    

    def register_btn():
        global f_name_input
        global l_name_input
        global email_input
        global username_input
        global pass1_input
        global pass2_input
        global phno_input
        global dob_input
        global gender_input
        global age_input
        f_name_input=f_name_in.get()
        l_name_input=l_name_in.get()
        email_input=email_in.get()
        username_input=username_in.get()
        pass1_input=pass1_in.get()
        pass2_input=pass2_in.get()
        phno_input=phno_in.get()
        dob_input=dob_in.get()
        gender_input=gender_in.get()
        age_input=age_in.get()


       
        
        if f_name_input=="" or l_name_input=="" or email_input=="" or username_input=="" or pass1_input=="" or pass2_input=="" or phno_input=="" or dob_input=="" or gender_input=="" or age_input=="":
            messagebox.showerror("Error","All Fields are Required")
        elif pass1_input!=pass2_input:
            messagebox.showerror("Error","Password and confirm password doesn't match")
        else:
            print("good to connect with sql")
            import mysql.connector
            mycon=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='ARD_GAMES')
            cursor=mycon.cursor()
            mycon.autocommit=True
            try:
                c1="insert into user_accounts values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(f_name_input,l_name_input,email_input,username_input,pass1_input,pass2_input,phno_input,dob_input,gender_input,age_input)
                cursor.execute(c1)
                messagebox.showinfo("Welcome","Welcome:"+ "" + f_name_input)
                return True
            except:
                messagebox.showinfo("ERROR","ACCOUNT ALREADY EXIST WITH THIS EMAIL" )
                return False
        f_name_in.delete(0,END)
        l_name_in.delete(0,END)
        email_in.delete(0,END)
        username_in.delete(0,END)
        pass1_in.delete(0,END)
        pass2_in.delete(0,END)
        phno_in.delete(0,END)
        dob_in.delete(0,END)
        gender_in.delete(0,END)
        age_in.delete(0,END)
                   
    Register=Button(frame,text="REGISTER",width=15,fg="white",bg="Green",font=("Calibri Light (Headings)",15,"bold"),command=register_btn).place(x=250,y=520)

    root_rm.mainloop()

    
    

#BUTTON MENU_______________________________________________________________________________________________________________________

#____def_function____

def welcome():
    global root

    def login_btn():
        
        login_menu()
        
        
    def sign_up_btn():
        
        registration_menu()
        
    def delete_btn():
        
        delete_menu()
        
    def close_btn():
        
        root.destroy()


    root=Tk()
    root.geometry('700x400')
    root.title("XYZ AIRLINES")

    #________bgimage__________
    root.bg=ImageTk.PhotoImage(file = "images/welcome_bg.png")
    bg=Label(root,image=root.bg).place(x=0,y=0,width=700,height=400)


    #________l-image__________
    root.wel=ImageTk.PhotoImage(Image.open("images/welcome_img.png"))
    wel_image=Label(image=root.wel).place(x=50,y=50,width=300,height=300)

    #___Registration Frame_____
    frame=Frame(root,bg="black")
    frame.place(x=350,y=50, width=300, height=300)
    

        
    #____command_buttons_______
    login=Button(frame,text="CHECK ACCOUNT", width=15,fg="black",bg="white",font=("Calibri Light (Headings)",15,"bold"),command=login_btn).place(x=50,y=50)
    sign_up=Button(frame,text="SIGN UP", width=15,fg="black",bg="white",font=("Calibri Light (Headings)",15,"bold"),command=sign_up_btn).place(x=50,y=100)
    delete=Button(frame,text="DELETE",width=15,fg="black",bg="white",font=("Calibri Light (Headings)",15,"bold"),command=delete_btn).place(x=50,y=150)
    close=Button(frame,text="CLOSE",width=15,fg="black",bg="white",font=("Calibri Light (Headings)",15,"bold"),command=close_btn).place(x=50,y=200)

    root.mainloop()
    #__________________________________________________________________________________________________________________________________________



#root=Tk()
#root.destroy()
#root.mainloop()
welcome()

