from tkinter import*
from turtle import width
import random
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

from numpy import var


class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

     # =================== Title Bar ====================
        
        lbl_title = Label(self.root,text="ROOM BOOKING  DETAILS",font=("times new roman",18, "bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50) 
        
    #========================Label Frame===================
        
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add", padx=2,font=("times new roman",18, "bold"))
        labelframeleft.place(x=5,y=50,width=540,height=350)

    # ==============================labels and entries==================
        #floor

        lbl_floor=Label(labelframeleft,text="Floor",font=("arial",10,"bold"),padx=1,pady=3)
        lbl_floor.grid(row=0,column=0,sticky=W)
        self.var_floor=StringVar()
        enty_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,font=("arial",10,"bold"),width=15)
        enty_floor.grid(row=0,column=1)
#==================room no==============
        lbl_room_no=Label(labelframeleft,text="Room No",font=("arial",10,"bold"),padx=1,pady=3)
        lbl_room_no.grid(row=1,column=0,sticky=W)
        
        self.var_roomno=StringVar()
        enty_room_no=ttk.Entry(labelframeleft,textvariable=self.var_roomno,font=("arial",10,"bold"),width=15)
        enty_room_no.grid(row=1,column=1)
#==========================Room type===============
        lbl_room_type=Label(labelframeleft,text="Room Type",font=("arial",10,"bold"),padx=1,pady=3)
        lbl_room_type.grid(row=2,column=0,sticky=W)

        self.var_roomtype=StringVar()
        enty_room_type=ttk.Entry(labelframeleft,textvariable=self.var_roomtype,font=("arial",10,"bold"),width=15)
        enty_room_type.grid(row=2,column=1)
#===========================Buttons=========================
        btn_frame=Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40,)
        

        btnAdd=Button(btn_frame, text="Add",command=self.add_data, font=("arial",11, "bold"),bg="Black",fg="gold", width=10)
        btnAdd.grid(row=0,column=0, padx=1)

        btnUpdate=Button(btn_frame, text="Update",command=self.update,font=("arial",11, "bold"),bg="Black",fg="gold", width=10)
        btnUpdate.grid(row=0,column=1, padx=1)

        btnDelete=Button(btn_frame, text="Delete",command=self.mDelete, font=("arial",11, "bold"),bg="Black",fg="gold", width=10)
        btnDelete.grid(row=0,column=2, padx=1)

        btnReset=Button(btn_frame, text="Reset",command=self.reset, font=("arial",11, "bold"),bg="Black",fg="gold", width=10)
        btnReset.grid(row=0,column=3, padx=1) 

#===============================Table frame search analysis
        Table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search Analysis System", font=("arial", 14, "bold"))
        Table_frame.place(x=600, y=55, width=600, height=350)

        scroll_x=ttk.Scrollbar(Table_frame, orient= HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame, orient= VERTICAL)     

        self.room_table = ttk.Treeview(Table_frame,column=("Floor","Roomno","roomtype"),
                                               xscrollcommand=scroll_x.set,
                                               yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
   
        self.room_table.heading("Floor",text="Floor")
        self.room_table.heading("Roomno",text="Room No")
        self.room_table.heading("roomtype",text="Room Type")
        
        

        self.room_table["show"]="headings"

        self.room_table.column("Floor",width=100)
        self.room_table.column("Roomno",width=100)
        self.room_table.column("roomtype",width=100)
       

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
#==========================Add data==========================
    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomtype.get()=="":
             messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Ishitaipshita@31",database="management1")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                                    self.var_floor.get(),
                                                                                    self.var_roomno.get(),
                                                                                    self.var_roomtype.get(),
                                                                                
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()                                                                    
                messagebox.showinfo("Success","New room  added successfully!",parent=self.root)
            except Exception as es: 
                messagebox.showerror("Warning",f"Some thing went wrong:{str(es)}", parent=self.root)  

#============================Fetch data================================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Ishitaipshita@31",database="management1")
        my_cursor=conn.cursor()  
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END, values=i)
            conn.commit()
        conn.close()  
#=================================get cursor============================
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        if not cursor_row:
         return
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_floor.set(row[0]),                                                                                
        self.var_roomno.set(row[1]),
        self.var_roomtype.set(row[2])
#================================update====================================
    def update(self):
        if self.var_floor.get== "":
            messagebox.showerror("Error","Please enter floor number",parent=self.root)
        else:    
            conn=mysql.connector.connect(host="localhost",username="root",password="Ishitaipshita@31",database="management1")
            my_cursor=conn.cursor()  
            my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(

                                                                                                                                                                            
                self.var_floor.get(),
                self.var_roomtype.get(),
                self.var_roomno.get(),
                
            ))
                                                                                                                                                                            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","New room details has been added successfully",parent=self.root)
   #deletion of data:

    def  mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this room details", parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Ishitaipshita@31",database="management1")
            my_cursor=conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_roomno.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()      
#================reset data===========
    def reset(self):
        self.var_floor.set(""),
        self.var_roomno.set(""),
        self.var_roomtype.set(""),
       

if __name__=="__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()