from tkinter import *
from tkinter import ttk, messagebox
import pymysql


class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student management  system")
        self.root.geometry("1350x700")
        title=Label(self.root,text="Student Managment System",bd=5,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)
        # ===============All variables===============
        self.roll_no_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.search_by = StringVar()
        self.search = StringVar()







        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=570)

        m_title=Label(Manage_Frame,text="Manage Students",font=("times new roman",20,"bold"),bg="crimson",fg="white")
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll = Label(Manage_Frame, text="Roll No", font=("times new roman",20, "bold"), bg="crimson",
                        fg="white")
        lbl_roll.grid(row=1, column=0, pady=10,padx=29,sticky="w")

        txt_roll = Entry(Manage_Frame, textvariable=self.roll_no_var, font=("times new roman", 15, "bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", font=("times new roman", 20, "bold"), bg="crimson",
                         fg="white")
        lbl_name.grid(row=2, column=0, pady=10, padx=29, sticky="w")

        txt_name = Entry(Manage_Frame, textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")


        lbl_email = Label(Manage_Frame, text="Email", font=("times new roman", 20, "bold"), bg="crimson",
                        fg="white")
        lbl_email.grid(row=3, column=0, pady=10,padx=29,sticky="w")

        txt_email = Entry(Manage_Frame, textvariable=self.email_var, font=("times new roman", 15, "bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")


        lbl_gender = Label(Manage_Frame, text="Gender", font=("times new roman", 20, "bold"), bg="crimson",
                          fg="white")
        lbl_gender.grid(row=4, column=0, pady=10,padx=29,sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.gender_var,  font=("times new roman", 13, "bold"))
        combo_gender['values']=("male","female","other")
        combo_gender.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        lbl_contact = Label(Manage_Frame, text="Contact", font=("times new roman", 20, "bold"), bg="crimson",
                          fg="white")
        lbl_contact.grid(row=5, column=0, pady=10, padx=29, sticky="w")

        txt_contact = Entry(Manage_Frame,textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_dob = Label(Manage_Frame, text="D.O.B", font=("times new roman", 20, "bold"), bg="crimson",
                          fg="white")
        lbl_dob.grid(row=6, column=0, pady=10, padx=29, sticky="w")

        txt_dob = Entry(Manage_Frame, textvariable=self.dob_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_address = Label(Manage_Frame, text="Address", font=("times new roman", 20, "bold"), bg="crimson",
                        fg="white")
        lbl_address.grid(row=7, column=0, pady=10, padx=29, sticky="w")

        self.txt_address = Text(Manage_Frame, width=30,height=4, font=("", 10),)
        self.txt_address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        btn_frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        btn_frame.place(x=22,y=612,width=445)


        addbtn = Button(btn_frame, text="add", width=10,command=self.add_students).grid(row=0, column=0, padx=10, pady=10)
        updatebtn = Button(btn_frame, text="Update", width=10,command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_frame, text="Delete", width=10,command=self.delete_data).grid(row=0, column=2, padx=10, pady=10)
        clearbtn = Button(btn_frame, text="Clear", width=10,command=self.clear).grid(row=0, column=3, padx=10, pady=10)


        # # ---------------------Detailed Frame---------------------------
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=500, y=100, width=750, heigh=570)

        lbl_search = Label(Detail_Frame, text="Search By", font=("times new roman", 20, "bold"), bg="crimson",
                        fg="white")
        lbl_search.grid(row=0, column=0, pady=20)
        self.items = {'Roll NO': 'roll_no', 'Name': 'name', 'Contact': 'contact'}

        self.combo_serach = ttk.Combobox(Detail_Frame,width=10,state='readonly',values=list(self.items), font=("times new roman", 13, "bold"))
        # self.combo_serach['values'] = ("Roll ", "Name", "Contact")
        self.combo_serach.grid(row=0, column=1, pady=10, padx=20)

        self.txt_Search = Entry(Detail_Frame,  font=("times new roman", 13, "bold"), bd=5, relief=GROOVE)
        self.txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Detail_Frame, text="Seach", width=10,pady=5,command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(Detail_Frame, text="Show all", width=10,pady=5,command=self.feftch_data).grid(row=0, column=4, padx=10, pady=10)

        # #-------- table Frame-------------
        Table_frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_frame.place(x=20,y=70,width=700,height=480)

        scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(Table_frame,columns=("roll","name","email","gender","contact","dob","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("contact", text="Contact")
        self.student_table.heading("dob", text="D.O.B")
        self.student_table.heading("Address", text="Address")
        self.student_table["show"] = "headings"
        self.student_table.column("roll", width=50)
        self.student_table.column("name", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("contact", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("Address", width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.feftch_data()

    def add_students(self):
        if self.roll_no_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","all fileds should be required!")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            try:
                cur = con.cursor()
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)", (self.roll_no_var.get(),
                                                                              self.name_var.get(),
                                                                              self.email_var.get(),
                                                                              self.gender_var.get(),
                                                                              self.contact_var.get(),
                                                                              self.dob_var.get(),
                                                                              self.txt_address.get('1.0',END)
                                                                              ))
            except Exception as e:
                messagebox.showinfo("succ", e)
            con.commit()
            self.feftch_data()
            con.close()
    def feftch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        try:
            cur = con.cursor()
            cur.execute("select * from students")
            rows=cur.fetchall()
            if (len(rows)!=0 ):
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert('',END,values=row)
            elif (len(rows)==0 ):
                self.student_table.delete(*self.student_table.get_children())




        except Exception as e:
            messagebox.showinfo("succ", e)
        con.commit()
        con.close()
    def clear(self):
        self.roll_no_var.set("")
        self.name_var.set("")
        self.gender_var.set("")
        self.email_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete('1.0',END)

    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents['values']
        self.roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.gender_var.set(row[2])
        self.email_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert('1.0', row[6])


    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        try:
            cur = con.cursor()
            cur.execute("update students set name=%s, email=%s,gender=%s,contact=%s,dob=%s, address=%s where roll_no=%s", (
                                                                          self.name_var.get(),
                                                                          self.email_var.get(),
                                                                          self.gender_var.get(),
                                                                          self.contact_var.get(),
                                                                          self.dob_var.get(),
                                                                          self.txt_address.get('1.0',END),
                                                                          self.roll_no_var.get(),
                                                                          ))
        except Exception as e:
            messagebox.showinfo("succ", e)
        con.commit()
        self.feftch_data()
        self.clear()
        con.close()
    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        try:
            cur = con.cursor()
            cur.execute("delete  from students where roll_no=%s",self.roll_no_var.get())
            messagebox.showinfo("succ", "data deleted..")
        except Exception as e:
            messagebox.showerror("succ", e)
        con.commit()
        con.close()
        self.feftch_data()
        self.clear()


    def search_data(self):
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            try:
                cur = con.cursor()
                v=("select * from students where "+str(self.items[self.combo_serach.get()])+" LIKE '%"+str(self.txt_Search.get())+"%'")
                messagebox.showinfo("str",v);
                cur.execute(v)
                rows = cur.fetchall()
                if (len(rows) != 0):




                    self.student_table.delete(*self.student_table.get_children())
                    for row in rows:
                        self.student_table.insert('', END, values=row)
            except Exception as e:
                messagebox.showerror("error",e)
            con.commit()
            con.close()











root=Tk()
o=Student(root)
root.mainloop()