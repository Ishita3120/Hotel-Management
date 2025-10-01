from tkinter import*
from turtle import width
import random
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

from numpy import var


class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")


    
        #============================variables=================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_number=StringVar()



           # =================== Title Bar =====================
        
        
        lbl_title = Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18, "bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)
         #========================Label Frame===================
        
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="customer detail", padx=2,font=("times new roman",18, "bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)

#===============================labels and entries==================
        lbl_cust_ref=Label(labelframeleft,text="Customer ref",font=("arial",10,"bold"),padx=1,pady=3)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,font=("arial",10,"bold"),width=15)
        enty_ref.grid(row=0,column=1)

        #cust_name
        cname=Label(labelframeleft,text="Customer Name",font=("arial",10,"bold"),padx=1,pady=3)
        cname.grid(row=1,column=0,sticky=W)

        textcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,font=("arial",10,"bold"),width=15)
        textcname.grid(row=1,column=1)
        #mother name
        mother_name=Label(labelframeleft,text="Mother name",font=("arial",10,"bold"),padx=1,pady=3)
        mother_name.grid(row=2,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_mother,font=("arial",10,"bold"),width=15,)
        enty_ref.grid(row=2,column=1)
        #gender checkbox
        label_gender=Label(labelframeleft,font=("arial",10,"bold"),text="gender",padx=1,pady=3)
        label_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",10,"bold"),width=15,state="readonly")
        combo_gender["values"]=("Male","Female","Others")
        combo_gender.grid(row=3,column=1)

        #postcode
        postcode=Label(labelframeleft,text="postcode",font=("arial",10,"bold"),padx=1,pady=3)
        postcode.grid(row=4,column=0,sticky=W)

        post_entry=ttk.Entry(labelframeleft,textvariable=self.var_post,font=("arial",10,"bold"),width=15)
        post_entry.grid(row=4,column=1)
        #mobilenumber
        mobile_no=Label(labelframeleft,text="mobile number",font=("arial",10,"bold"),padx=1,pady=3)
        mobile_no.grid(row=5,column=0,sticky=W)

        mob_ref=ttk.Entry(labelframeleft,textvariable=self.var_mobile,font=("arial",10,"bold"),width=15)
        mob_ref.grid(row=5,column=1)
        #email
        lbl_email=Label(labelframeleft,text="Email",font=("arial",10,"bold"),padx=1,pady=3)
        lbl_email.grid(row=6,column=0,sticky=W)

        email_ref=ttk.Entry(labelframeleft,text=self.var_email,font=("arial",10,"bold"),width=15)
        email_ref.grid(row=6,column=1)

        #nationality
        nationality_ref=Label(labelframeleft,text="Nationality",font=("arial",10,"bold"),padx=1,pady=3)
        nationality_ref.grid(row=7,column=0,sticky=W)

        nation_ref=ttk.Entry(labelframeleft,textvariable=self.var_nationality,font=("arial",10,"bold"),width=15)
        nation_ref.grid(row=7,column=1)

        #id proof type
        id_type=Label(labelframeleft,font=("arial",10,"bold"),text="id proof type",padx=1,pady=3)
        id_type.grid(row=8,column=0,sticky=W)
        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("arial",10,"bold"),width=15)
        combo_id["values"]=("Aadhar Card","Voter-Id","Pan Card")
        combo_id.grid(row=8,column=1)
        #id number
        id_number=Label(labelframeleft,text="Id number",font=("arial",10,"bold"),padx=1,pady=3)
        id_number.grid(row=9,column=0,sticky=W)

        id_ref=ttk.Entry(labelframeleft,textvariable=self.var_number,font=("arial",10,"bold"),width=15)
        id_ref.grid(row=9,column=1)

        #address
        address=Label(labelframeleft,text="Address",font=("arial",10,"bold"),padx=1,pady=3)
        address.grid(row=10,column=0,sticky=W)

        add_ref=ttk.Entry(labelframeleft,textvariable=self.var_address,font=("arial",10,"bold"),width=15)
        add_ref.grid(row=10,column=1)

    #==================buttons==============================
        btn_frame=Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40,)
        

        btnAdd=Button(btn_frame, text="Add",command=self.add_data, font=("arial",11, "bold"),bg="Black",fg="gold", width=10)
        btnAdd.grid(row=0,column=0, padx=1)

        btnUpdate=Button(btn_frame, text="Update",command=self.update, font=("arial",11, "bold"),bg="Black",fg="gold", width=10)
        btnUpdate.grid(row=0,column=1, padx=1)

        btnDelete=Button(btn_frame, text="Delete",command=self.mDelete, font=("arial",11, "bold"),bg="Black",fg="gold", width=10)
        btnDelete.grid(row=0,column=2, padx=1)

        btnReset=Button(btn_frame, text="Reset",command=self.reset, font=("arial",11, "bold"),bg="Black",fg="gold", width=10)
        btnReset.grid(row=0,column=3, padx=1)

        # ======================== Table Frame ============================================

        TableFrame=LabelFrame(self.root,bd=2, relief=RIDGE,text="View Details And Search History System",font=("times new roman",20, "bold"),padx=1,)
        TableFrame.place(x=435, y=50, width=860, height=490)

        lblSearchBy=Label( TableFrame, text="Search By: ",font=("arial", 16, "bold"),fg="black")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)
        
        self.search_var=StringVar()
        combo_search=ttk.Combobox(TableFrame,textvariable=self.search_var, font=("arial",14, "bold"),width=10,state="readonly")
        combo_search["value"]=("Mobile","Ref")
        combo_search.current(0)
        combo_search.grid(row=0, column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(TableFrame,textvariable=self.txt_search, width=14,font=("arial",14, "bold"))
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch=Button(TableFrame, text="Search",command=self.search, font=("arial", 14, "bold"),bg="Black",fg="gold", width=10)
        btnSearch.grid(row=0,column=3, padx=2)

        btnShowAll=Button(TableFrame, text="Show All",command=self.fetch_data, font=("arial", 14, "bold"),bg="Black",fg="gold", width=10)
        btnShowAll.grid(row=0,column=4, padx=2)


        #=======================table frame search Analysis===================
        '''Table_frame = LabelFrame(root, bd=2, relief=RIDGE, text="View Details and Search Analysis System", font=("arial", 14, "bold"))
        Table_frame.place(x=435, y=50, width=860, height=490)

        LblSearchBy = Label(Table_frame, font=("arial", 12, "bold"), text="Search by", bg="red", fg="white")
        LblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        search_Var = StringVar()
        combo_search = ttk.Combobox(Table_frame, textvariable=search_Var, font=("arial", 12, "bold"), width=24, state="readonly")
        combo_search["value"] = ("Contact", "Room")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        text_search = StringVar()
        txtSearch = ttk.Entry(Table_frame, textvariable=text_search, font=("arial", 13, "bold"), width=24)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_frame, text="Search", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=2)

        btnShowAll = Button(Table_frame, text="Show All", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=2)

        root.mainloop()'''

        # ====================== Show Data Table =========================

        details_table=Frame(TableFrame, bd=2, relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table, orient= HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table, orient= VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile",
                                               "email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No.")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="Postcode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)

        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
             messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Ishitaipshita@31",database="management1")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_ref.get(),
                                                                                    self.var_cust_name.get(),
                                                                                    self.var_mother.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_post.get(),
                                                                                    self.var_mobile.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_nationality.get(),
                                                                                    self.var_id_proof.get(),
                                                                                    self.var_number.get(),
                                                                                    self.var_address.get()
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()                                                                    
                messagebox.showinfo("Success","customer has been added",parent=self.root)
            except Exception as es: 
                messagebox.showerror("Warning",f"Some thing went wrong:{str(es)}", parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Ishitaipshita@31",database="management1")
        my_cursor=conn.cursor()  
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END, values=i)
            conn.commit()
        conn.close()      

    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_number.set(row[9]),
        self.var_address.set(row[10])
    
    def update(self):
        if self.var_mobile.get=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:    
            conn=mysql.connector.connect(host="localhost",username="root",password="Ishitaipshita@31",database="management1")
            my_cursor=conn.cursor()  
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,Postcode=%s, Mobile=%s, Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s, Address=%s where Ref=%s ",(

                                                                                                                                                                            
              self.var_cust_name.get(),
              self.var_mother.get(),
              self.var_gender.get(),
              self.var_post.get(),
              self.var_mobile.get(),
              self.var_email.get(),
              self.var_nationality.get(),
              self.var_id_proof.get(),
              self.var_number.get(),
              self.var_address.get(),
              self.var_ref.get()     
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)

    def  mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer", parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Ishitaipshita@31",database="management1")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")
        
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Ishitaipshita@31",database="management1")
        my_cursor=conn.cursor()

        my_cursor.execute("select* from customer where "+str(self.search-var.get())+"LIKE'%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i) 
            conn.commit()
        conn.close()   


if __name__=="__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()




