from tkinter import*
from tkinter import messagebox
from time import strftime
#from datetime import datetime
#from tkinter import ttk
from PIL import Image, ImageTk  # Requires Pillow library
from customer2 import Cust_Win
from room  import Roombooking
from details import DetailsRoom
#from login_window import login


#from login_window import admin_login,customer_login


class HotelManagementSystem:
    def __init__(self, root):
        self.root =root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
    

        # =================== 1st Image (Header) =====================
        img1 = Image.open(r"C:\Users\ishit\OneDrive\Desktop\hotelmanagement\image\pexels-pixabay-258154.jpg")
        img1 = img1.resize((1550,140), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        # =================== Logo (Sidebar) =====================
        img2 = Image.open(r"C:\Users\ishit\OneDrive\Desktop\hotelmanagement\image\35181-NZV3DS.jpg")
        img2 = img2.resize((230, 140), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)

        # =================== Title Bar =====================
        lbl_title = Label(
            self.root,text="Hotel Management System",font=("times new roman",30, "bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

#===========================main frame=========================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

#=================menu===========================================
        lbl_menu = Label(main_frame,text="MENU",font=("times new roman", 20, "bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)
#================button frame==================================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)
        cust_btn=Button(btn_frame,text="Customer",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)
        room_btn=Button(btn_frame,text="Rooms",command=self.roombooking,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)
        details_btn=Button(btn_frame,text="Details",width=22,command=self.details_room,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)
        report_btn=Button(btn_frame,text="Report",command=self.submit_report,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)
        logout_btn=Button(btn_frame,text="Logout",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)

#===================customer file===========================        
    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window) 

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)  

    def  details_room(self):

        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)  

    # =================== Logout Function =====================
    def logout(self):
        # Confirm logout
        response = messagebox.askyesno("Logout", "Are you sure you want to log out?")
        if response:
            # Close the current window
            self.root.destroy()
            # Reopen the login window
            #login.main()  # Call the main function from your login script to open the login window
            messagebox.showinfo("Logged Out", "Successfully logged out!")

    # =================== Submit Report =====================
    def submit_report(self):
        content = self.report_text.get("1.0", END).strip()
        if content:
            # You can store this in a text file or DB
            with open("customer_reports.txt", "a") as file:
                file.write(content + "\n\n")
            messagebox.showinfo("Submitted", "Your report has been submitted. Thank you!")
            self.root.destroy()
        else:
            messagebox.showwarning("Empty", "Please write something before submitting.")

    def clear_report(self):
        self.report_text.delete("1.0", END)



#====================right side image=======================

    def submit_report(self):
        content = self.report_text.get("1.0", END).strip()
        if content:
            # You can store this in a text file or DB
            with open("customer_reports.txt", "a") as file:
                file.write(content + "\n\n")
            messagebox.showinfo("Submitted", "Your report has been submitted. Thank you!")
            self.root.destroy()
        else:
            messagebox.showwarning("Empty", "Please write something before submitting.")

    def clear_report(self):
        self.report_text.delete("1.0", END)

    
      

if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
    

