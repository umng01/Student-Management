
import mysql.connector
# python3 -m pip install mysql-connector-python
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk 
from tkinter import messagebox

class Student:
    def __init__(self, root):
        self.root = root 
        self.root.geometry("1530x630+0+0")
        self.root.title("Managing")
        self.root.resizable(False,False)


        # Variables

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar() 
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_faculty = StringVar()





        #1st
        # img = Image.open(r"college_images/7th.jpg")
        # img = img.resize((540, 160), Image.ANTIALIAS)
        # self.photoimg = ImageTk.PhotoImage(img)

        # self.btn_1 = Button(self.root, image=self.photoimg, cursor="hand2")
        # self.btn_1.place(x=0,y=0,width=540,height=160)


        #2nd
        # img_2 = Image.open(r"college_images/5th.jpg")
        # img_2 = img_2.resize((540, 160), Image.ANTIALIAS)
        # self.photoimg_2 = ImageTk.PhotoImage(img_2)

        # self.btn_2 = Button(self.root, image=self.photoimg_2, cursor="hand2")
        # self.btn_2.place(x=540,y=0,width=540,height=160)


        # #3rd
        # img_3 = Image.open(r"college_images/6th.jpg")
        # img_3 = img_3.resize((540, 160), Image.ANTIALIAS)
        # self.photoimg_3 = ImageTk.PhotoImage(img_3)

        # self.btn_3 = Button(self.root, image=self.photoimg_3, cursor="hand2")
        # self.btn_3.place(x=1000,y=0,width=540,height=160)


        # bg image

        img_4 = Image.open(r"college_images/black.jpg")
        img_4 = img_4.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg_4 = ImageTk.PhotoImage(img_4)

        bg_lbl = Label(self.root, image = self.photoimg_4, bd = 2, relief=RIDGE)
        bg_lbl.place(x=0, y = 0, width=1530, height=710)


        lbl_title = Label(bg_lbl, text = "Perform CRUD", font = ("times new roman",37,"bold"),fg="black", bg="white")
        lbl_title.place(x=0,y=0,width=1530, height=50)



        # frame is like a container 
        Manage_frame = Frame(bg_lbl, bd=2, relief=RIDGE, bg="white")
        Manage_frame.place(x=15,y=55,width=1500,height=560)


        #left frame
        DataLeftFrame = LabelFrame(Manage_frame, bd=4,relief=RIDGE,
        padx=2, text="Student Information", font = ("times new roman",12,"bold"),fg="red" , bg="white" 
        )
        DataLeftFrame.place(x=10, y = 10, width=660, height=540)


        #img
        img_5 = Image.open(r"college_images/1.jpg")
        img_5 = img_5.resize((650, 110), Image.ANTIALIAS)
        self.photoimg_5 = ImageTk.PhotoImage(img_5)

        my_img = Label(DataLeftFrame, image = self.photoimg_5, bd = 2, relief=RIDGE)
        my_img.place(x=0, y =0, width=650, height=110)


        # Current Course Label Frame Information

        std_lbl_info_frame = LabelFrame(DataLeftFrame, bd=4,relief=RIDGE,
        padx=2, text="Course Information", font = ("times new roman",12,"bold"),fg="red" , bg="white"
        )
        std_lbl_info_frame.place(x=00, y = 120, width=650, height=115)

        # Labels and Combobox
        # department
        lbl_dep = Label(std_lbl_info_frame, text="Department", font = ("arial",12,"bold"),fg="black" , bg="white")
        lbl_dep.grid(row = 0, column=0, padx=2, sticky=W)

        combo_dep = ttk.Combobox(std_lbl_info_frame,textvariable=self.var_dep, font = ("arial",12,"bold"), width=17, state="readonly")
        combo_dep["value"] = ("Select Department", "CSE", "IT", "CSI", "CO", "ME")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,  sticky=W)

        # course
        course_std = Label(std_lbl_info_frame,  font = ("arial",12,"bold"),text="Courses:", bg="white")
        course_std.grid(row=0, column=2, sticky=W, padx=2, pady=10)

        com_txtcourse_std = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_course,state="readonly",
        font=("arial", 12, "bold"), width=17)
        com_txtcourse_std["value"] = ("Select Course", "BTech", "MTech","BCA", "MCA", "MBA")
        com_txtcourse_std.current(0)
        com_txtcourse_std.grid(row=0, column=3, sticky=W, padx=2, pady=10)

        #year 
        current_year = Label(std_lbl_info_frame, font=("arial", 12, "bold"), 
        text = "Year: ", bg="white")
        current_year.grid(row=1, column=0, sticky=W, padx=2, pady=10)

        com_txt_current_year = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_year, state="readonly", font=("arial",12, "bold"), width=17)
        com_txt_current_year["value"] = ("Select Year", "2023", "2022", "2021", "2020")
        com_txt_current_year.current(0)
        com_txt_current_year.grid(row=1, column=1, sticky=W, pady=2)

        # semester 
        label_semester = Label(std_lbl_info_frame,font=("arial", 12, "bold"), text="Semester:", bg="white")
        label_semester.grid(row=1, column=2, sticky=W, padx=2, pady=10)
        comSemester = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_semester, state="readonly", font=("arial",12, "bold"), width=17
        )
        comSemester["value"] = ("Select Semester", "1", "2","3", "4", "5", "6", "7", "8")
        comSemester.current(0)
        comSemester.grid(row=1, column=3, sticky=W, padx=2, pady=10)

        # Student Class Label Frame Information
        std_lbl_class_frame = LabelFrame(DataLeftFrame, bd=4,relief=RIDGE,
        padx=2, text="Class Course Information", font = ("times new roman",12,"bold"),fg="red" , bg="white"
        )
        std_lbl_class_frame.place(x=0, y = 235, width=650, height=250)

        # Labels Entry
        # ID
        lbl_id = Label(std_lbl_class_frame, font=("arial", 12, "bold"), text="Student ID", bg="white")
        lbl_id.grid(row=0, column=0, sticky=W, padx=2, pady=7)
        
        id_entry = ttk.Entry(std_lbl_class_frame, textvariable=self.var_std_id, font = ("arial", 12, "bold"), width = 20)
        id_entry.grid(row=0, column=1, sticky=W, padx=2, pady=7)

        # Name 
        lbl_name = Label(std_lbl_class_frame, font=("arial", 11, "bold"), text="Student Name", bg="white")
        lbl_name.grid(row=0, column=2, sticky=W, padx=2, pady=7)
        
        txt_name = ttk.Entry(std_lbl_class_frame, textvariable=self.var_std_name,font = ("arial", 11, "bold"), width = 22)
        txt_name.grid(row=0, column=3, sticky=W, padx=2, pady=7)

        # Division 
        lbl_div = Label(std_lbl_class_frame, font=("arial", 11, "bold"), text="Class Division", bg="white")
        lbl_div.grid(row=1, column=0, sticky=W, padx=2, pady=7)
        
        com_txt_div = ttk.Combobox(std_lbl_class_frame, textvariable=self.var_div, font = ("arial", 12, "bold"), width = 18, state="readonly")
        com_txt_div["value"] = ("Select Division", "A", "B", "C")
        com_txt_div.current(0)
        com_txt_div.grid(row=1, column=1, sticky=W, padx=2, pady=7)

        # Roll 
        lbl_roll = Label(std_lbl_class_frame, font=("arial", 11, "bold"), text="Roll No:", bg="white")
        lbl_roll.grid(row=1, column=2, sticky=W, padx=2, pady=7)
        
        txt_roll = ttk.Entry(std_lbl_class_frame, textvariable=self.var_roll, font = ("arial", 11, "bold"), width = 22)
        txt_roll.grid(row=1, column=3, sticky=W, padx=2, pady=7)

        # Gender 
        lbl_gender = Label(std_lbl_class_frame, font=("arial", 11, "bold"), text="Gender", bg="white")
        lbl_gender.grid(row=2, column=0, sticky=W, padx=2, pady=7)
        
        com_txt_gender = ttk.Combobox(std_lbl_class_frame, textvariable=self.var_gender, font = ("arial", 12, "bold"), width = 18, state="readonly")

        com_txt_gender["value"] = ("Select Gender", "Female", "Male", "Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=2, column=1, sticky=W, padx=2, pady=7)

        # DOB
        lbl_dob = Label(std_lbl_class_frame, font=("arial", 11, "bold"), text="Date of Birth:", bg="white")
        lbl_dob.grid(row=2, column=2, sticky=W, padx=2, pady=7)
        
        txt_dob = ttk.Entry(std_lbl_class_frame,textvariable=self.var_dob, font = ("arial", 11, "bold"), width = 22)
        txt_dob.grid(row=2, column=3, sticky=W, padx=2, pady=7)

        # Email
        lbl_email = Label(std_lbl_class_frame,font=("arial", 11, "bold"), text="Email:", bg="white")
        lbl_email.grid(row=3, column=0, sticky=W, padx=2, pady=7)
        
        txt_email = ttk.Entry(std_lbl_class_frame, textvariable=self.var_email, font = ("arial", 11, "bold"), width = 22)
        txt_email.grid(row=3, column=1, sticky=W, padx=2, pady=7)

        # Phone 
        lbl_phone = Label(std_lbl_class_frame, font=("arial", 11, "bold"), text="Phone No:", bg="white")
        lbl_phone.grid(row=3, column=2, sticky=W, padx=2, pady=7)
        
        txt_phone = ttk.Entry(std_lbl_class_frame, textvariable=self.var_phone, font = ("arial", 11, "bold"), width = 22)
        txt_phone.grid(row=3, column=3, sticky=W, padx=2, pady=7)

        # Address 
        lbl_address = Label(std_lbl_class_frame, font=("arial", 11, "bold"), text="Address:", bg="white")
        lbl_address.grid(row=4, column=0, sticky=W, padx=2, pady=7)
        
        txt_address = ttk.Entry(std_lbl_class_frame, textvariable=self.var_address, font = ("arial", 11, "bold"), width = 22)
        txt_address.grid(row=4, column=1, sticky=W, padx=2, pady=7)

        # Faculty 
        lbl_faculty = Label(std_lbl_class_frame, font=("arial", 11, "bold"), text="Faculty:", bg="white")
        lbl_faculty.grid(row=4, column=2, sticky=W, padx=2, pady=7)
        
        txt_faculty = ttk.Entry(std_lbl_class_frame, textvariable=self.var_faculty, font = ("arial", 11, "bold"), width = 22)
        txt_faculty.grid(row=4, column=3, sticky=W, padx=2, pady=7)

        # Button Frame
        btn_frame = Frame(DataLeftFrame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0,y=470,width=650,height=38)

        btn_add = Button(btn_frame,command=self.add_data,text="Save", font=("arial", 11, "bold"), width=17, bg = "blue", fg = "white")
        btn_add.grid(row=0, column=0, padx=1)

        btn_update = Button(btn_frame,command=self.update_data, text="Update", font=("arial", 11, "bold"), width=17, bg = "blue", fg = "white")
        btn_update.grid(row=0, column=1, padx=1)

        btn_delete = Button(btn_frame,command=self.delete_data,text="Delete", font=("arial", 11, "bold"), width=17, bg = "blue", fg = "white")
        btn_delete.grid(row=0, column=2, padx=1)

        btn_reset = Button(btn_frame,command=self.reset_data, text="Reset", font=("arial", 11, "bold"), width=17, bg = "blue", fg = "white")
        btn_reset.grid(row=0, column=3, padx=1)






        #right frame
        DataRightFrame = LabelFrame(Manage_frame, bd=4,relief=RIDGE, padx=2, text="Student Information", font = ("times new roman",12,"bold"),fg="red" )
        DataRightFrame.place(x=680, y = 0, width=800, height=540)


        # img_6 = Image.open(r"college_images/6th.jpg")
        # img_6 = img_6.resize((780, 200), Image.ANTIALIAS)
        # self.photoimg_6 = ImageTk.PhotoImage(img_6)

        # my_img = Label(DataRightFrame, image = self.photoimg_6, bd = 2, relief=RIDGE)
        # my_img.place(x=0, y =0, width=790, height=200)

        # Right Frame 
        Search_Frame = LabelFrame(DataRightFrame, bd=4,relief=RIDGE, padx=2, text="", font = ("times new roman",12,"bold"),fg="red" )
        Search_Frame.place(x=0, y = 10, width=790, height=60)

        Search_by = Label(Search_Frame, font=("arial", 11, "bold"), text="Search By:", bg="black", fg="red")
        Search_by.grid(row=0, column=0, sticky=W, padx=5)
        
        # search
        self.var_combo_search = StringVar()
        com_txt_search = ttk.Combobox(Search_Frame,textvariable=self.var_combo_search, font = ("arial", 12, "bold"), width = 18, state="readonly")

        com_txt_search["value"] = ("Select Option", "Roll", "Phone", "Student_id")
        com_txt_search.current(0)
        com_txt_search.grid(row=0, column=1, sticky=W, padx=5)

        self.var_search = StringVar()
        txt_search = ttk.Entry(Search_Frame,textvariable=self.var_search, font = ("arial", 11, "bold"), width = 22)
        txt_search.grid(row=0, column=2, sticky=W, padx=5)

        btn_search = Button(Search_Frame,command=self.search_data, text="Search", font=("arial", 11, "bold"), width=12, bg = "blue", fg = "white")
        btn_search.grid(row=0, column=3, padx=2)

        btn_showAll = Button(Search_Frame,command=self.fetch_data,text="Show All", font=("arial", 11, "bold"), width=12, bg = "blue", fg = "white")
        btn_showAll.grid(row=0, column=4, padx=2)



        # ******************Student Table and Scroll Bar***************
        table_frame = Frame(DataRightFrame, bd=4, relief=RIDGE)
        table_frame.place(x=0,y=100,width=790,height=400)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "faculty"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("div", text="Class Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("faculty", text="Faculty")

        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("faculty", width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_dep.get() == "" or self.var_email.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error!!"," All fields Required")

        else: 
            try: 
                conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="mydb")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_faculty.get()
                )
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Successful!", "Successful!", parent=self.root)
            except Exception as es: 
                messagebox.showerror("Error", f"Due to{str(es)}", parent = self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="mydb")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0: 
            self.student_table.delete(*self.student_table.get_children())

            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data = content["values"]


        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_faculty.set(data[13])

    def update_data(self):
        if self.var_dep.get() == "" or self.var_email.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error!!"," All fields Required")
        
        else: 
            try: 
                update = messagebox.askyesno("Update", "Do you want to update?", parent=self.root)
                if update > 0: 
                    conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="mydb")
                    my_cursor = conn.cursor()
                    my_cursor.execute("Update Student set dep=%s, course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,faculty=%s where student_id=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_faculty.get(),
                        self.var_std_id.get()
                    )
                    )
                else: 
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success", "Student Successfully Updated!", parent=self.root)
            except Exception as es: 
                messagebox.showerror("Error", f"Due to;{str(es)}", parent = self.root)

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)

        else:
            try:
                Delete = messagebox.askyesno("Delete", "Do you want to delete?", parent=self.root)
                if Delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="mydb")
                    my_cursor = conn.cursor()
                    sql = "delete from student where student_id=%s"
                    value=(self.var_std_id.get(),)
                    my_cursor.execute(sql, value)
                else: 
                    if not Delete: return 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted!", parent=self.root)
            except Exception as es: 
                messagebox.showerror("Error", f"Due to{str(es)}", parent = self.root)

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_faculty.set("")


    #search data 
    def search_data(self):
        if self.var_combo_search.get() == "" or self.var_search.get() == "": 
            messagebox.showerror("Error", "Please select")
        else: 
            try: 
                conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="mydb")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student where " +str(self.var_combo_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                rows = my_cursor.fetchall()
                if len(rows) != 0: 
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("", END, values=i)
                    conn.commit()
                conn.close()
            except Exception as es: 
                messagebox.showerror("Error", f"Due to{str(es)}", parent = self.root)



                    


















if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
