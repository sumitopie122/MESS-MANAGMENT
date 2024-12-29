import tkinter as tk
from tkinter import Frame, Label, Button
from tkinter import *
from tkinter import messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mess Management App")
        self.geometry("1920x1080")
        self.configure(bg="pink")
       
        self.pages = {}

        
        for Page in (HomePage, PageOne):
            page_name = Page.__name__
            page = Page(parent=self, controller=self)
            self.pages[page_name] = page

           
            page.grid(row=0, column=0, sticky="nsew")

       
        self.show_page("HomePage")
    def close_windows(self):
       
        self.destroy()

    def show_page(self, page_name):
      
        page = self.pages[page_name]
        page.tkraise()


class HomePage(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="pink")
        
        self.canvas = tk.Canvas(self, width=1980, height=1080)
        self.canvas.pack(fill="both", expand=True)

        
        try:
            self.image = tk.PhotoImage(file="project/HOMEPAGE1.png")
            self.canvas.create_image(0, 0, anchor="nw", image=self.image)
        except Exception as e:
            self.canvas.create_text(300, 200, text=f"Image not found: {e}", fill="red", font=("Times New Roman", 16))

       
        button = Button(self, text="NEXT PAGE",
               command=lambda: controller.show_page("PageOne"))
        self.canvas.create_window(1300, 600, anchor="center", window=button)


class PageOne(Frame):
    
    def delete_data(self):
        
        for widget in self.l1:
            widget.destroy()  
        self.l1.clear()  

    def save_data(self):
    
        n = self.e1.get()
        name = n.replace(" ","")
        roll_no = self.e2.get()
        with open("project/studentData.txt","r") as f:
            if(str(roll_no) in f.read().split()):
                messagebox.showerror("Error","Already a user with this roll no")
                return 
        cash = self.e3.get()
        if(roll_no.isdigit() and cash.isdigit()):
            print(name,roll_no,cash)
            if name and roll_no and cash:
                with open("project/studentData.txt", "a+") as f:
                    f.write(f"\n{name.lower()} {roll_no} {cash}")
                messagebox.showinfo("Success", "Your data has been saved successfully!")
            else:
                messagebox.showerror("Error", "Please fill all the fields properly")
        else:
            messagebox.showerror("Error", "Make sure that cash and roll number are a numeric value")
    def search(self):
        
    
        rollno = self.e1.get()
        
        
        if rollno:
            with open("project/studentData.txt", "r+") as f:
                l = f.read().split()
            print(l)
            if str(rollno) in l:
                a = l.index(str(rollno))
            else:
                messagebox.showerror("Error", "NOT FOUND")
            
            name = l[a-1]
            cash = l[a+1]
            messagebox.showinfo("Success", f"NAME - {name.upper()}    ROLL NO - {rollno}    CASH = {cash}")
        else:
            messagebox.showerror("Error", "Please fill the name")
    
    def viewid(self):
        for widget in self.l1:
            widget.destroy()
        with open("project/studentData.txt") as f:
            l = f.read().split()
            n = len(l)
        rollno_label = Label(self, text='Roll No :')
        rollno_label.grid(row=2, column=7, pady=5, sticky=W)
        self.e1 = Entry(self)
       
        self.e1.grid(row=2, column=8, pady=5)
        
        self.l1.extend([self.e1,rollno_label]) 
            
            
        save_button = Button(self, text="Search",command = self.search,width=10, bg="lightblue")
        save_button.grid(row=4, column=8, pady=10)
        self.l1.append(save_button)
        del_button = Button(self, text="Close",command = self.delete_data,width=10, bg="lightblue")
        del_button.grid(row=5, column=8, pady=10)
        self.l1.append(del_button)
        
        

    def newid(self):
        for widget in self.l1:
            widget.destroy()
        
    
        name_label = Label(self, text='Name')
        roll_label = Label(self, text='Roll No')
        cash_label = Label(self, text='Current Bal')
        name_label.grid(row=2, column=7, pady=5, sticky=W)
        roll_label.grid(row=3, column=7, pady=5, sticky=W)
        cash_label.grid(row=4, column=7, pady=5, sticky=W)
        self.l1.extend([name_label, roll_label,cash_label])  
        
        self.e1 = Entry(self)
        self.e2 = Entry(self)
        self.e3 = Entry(self)
        self.e1.grid(row=2, column=8, pady=5)
        self.e2.grid(row=3, column=8, pady=5)
        self.e3.grid(row=4, column=8, pady=5)
        self.l1.extend([self.e1, self.e2,self.e3]) 
            
            
        save_button = Button(self, text="Save",command = self.save_data,width=10, bg="lightblue")
        save_button.grid(row=5, column=8, pady=10)
        self.l1.append(save_button)  
            
            
        delete_button = Button(self, text="Close", command = self.delete_data,width=10, bg="lightblue")
        delete_button.grid(row=6, column=8, pady=10)
        self.l1.append(delete_button)
    def delid1(self):
        for widget in self.l1:
            widget.destroy()
        self.e1 = Entry(self)
        self.e1.grid(row=2, column=8, pady=5)
        rollno_label = Label(self, text='Roll no :')
        rollno_label.grid(row=2, column=7, pady=5, sticky=W)
        self.l1.append(rollno_label)
        self.l1.extend([self.e1])
        button = Button(self,text="ERASE DATA?",command=self.delid,width=10, bg="lightblue")
        button.grid(row=4, column=8, pady=10)
        self.l1.append(button)
        button1 = Button(self,text="CLOSE",command=self.delete_data,width=10, bg="lightblue")
        button1.grid(row=5, column=8, pady=10)
        self.l1.append(button1)
    
    def delid(self):
        rollno = self.e1.get()
    

        with open("project/studentData.txt") as f:
            a = f.read().split()
        if str(rollno) in a:
                b = a.index((rollno))
        else:
                messagebox.showerror("Error", "NOT FOUND!")
            
        name= a[b-1]
        cash = a[b+1]
        with open("project/studentData.txt") as f:
            a = f.read()
        new_a = a.replace(name.lower(),"")
        new_c = new_a.replace(cash,"")
        new_b = new_c.replace(rollno,"")
        messagebox.showinfo("Success","Deleted the given Data")
        with open("project/studentData.txt","w") as f:
            f.write(new_b)
    def viewallid(self):
        for widget in self.l1:
            widget.destroy()
        with open("project/studentData.txt") as f:
            a = f.read().split()
        finalstr = "NAMES : "
        for i in range(0,len(a),3):
            finalstr = finalstr + " " + a[i].upper()
            
        if(len(finalstr)!=0):
            messagebox.showinfo("ALL STUDENTS",f"{finalstr}")
        else:
            messagebox.showinfo("Error","Create some data first")
    def addingdish(self):
        for widget in self.l1:
            widget.destroy()
        name_label = Label(self, text='Roll NO')
       
        cash_label = Label(self, text='Amount')
        name_label.grid(row=2, column=7, pady=5, sticky=W)
        
        cash_label.grid(row=3, column=7, pady=5, sticky=W)
        self.l1.extend([name_label,cash_label])  
        
        self.e1 = Entry(self)
      
        self.e2 = Entry(self)
        self.e1.grid(row=2, column=8, pady=5)
        self.e2.grid(row=3, column=8, pady=5)
       
        self.l1.extend([self.e1, self.e2]) 
            
            
        save_button = Button(self, text="Confirm",command = self.addingdishworking,width=10, bg="lightblue")
        save_button.grid(row=5, column=8, pady=10)
        self.l1.append(save_button)
        button1 = Button(self,text="CLOSE",command=self.delete_data,width=10, bg="lightblue")
        button1.grid(row=6, column=8, pady=10)
        self.l1.append(button1)
    def addingdishworking(self):
        try:
            rollno = self.e1.get()
            cash = self.e2.get()
            if cash.isdigit():
                with open("project/studentData.txt") as f:
                    a = f.read().split()
                    f.seek(0)
                    d = f.read()
                if str(rollno) in a:
                
                    b = a.index(str(rollno))
                c = a[b+1]
                new_text = d.replace(c,str(int(c)-int(cash)))
                
                with open("project/studentData.txt","w") as f:
                    f.write(new_text)
                messagebox.showinfo("Success","Successfully added the dish the he user")
            else:
                messagebox.showerror("Success","Make sure the cash input is numeric")

        except:
            messagebox.showinfo("ERROR","SOMETHING WENT WRONG")
    
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="pink")
        self.l1 = []
        
        try:
            self.image1 = tk.PhotoImage(file="project/mess menu.png")
            label = tk.Label(self, image=self.image1)
            label.grid(row=1, column=4, padx=20, pady=10)
        except Exception as e:
            label = tk.Label(self, text=f"Image not found: {e}", bg="pink", fg="red")
            label.grid(row=1, column=4, padx=20, pady=10)
        try:
            self.image = tk.PhotoImage(file="project/messextra.png")
            label = tk.Label(self, image=self.image)
            label.grid(row=1, column=14, padx=20, pady=10)
        except Exception as e:
            label = tk.Label(self, text=f"Image not found: {e}", bg="pink", fg="red")
            label.grid(row=1, column=4, padx=20,pady=10)

        button_frame = Frame(self, bg="pink")
        button_frame.grid(row=1, column=8, rowspan=5, sticky=N, padx=20)  

        button_new = tk.Button(button_frame, text='New ID',command=self.newid, width=21, height=2, font=("Times New Roman", 16))
        button_new.pack(pady=5)  

        button_view = tk.Button(button_frame, text='View ID',command =self.viewid, width=21, height=2, font=("Times New Roman", 16))
        button_view.pack(pady=5)

        button_delete = tk.Button(button_frame, text='Delete ID',command = self.delid1, width=21, height=2, font=("Times New Roman", 16))
        button_delete.pack(pady=5)
        button_fine = tk.Button(button_frame, text='View ALL IDS',command = self.viewallid, width=21, height=2, font=("Times New Roman", 16))
        button_fine.pack(pady=5)

        button_dish = tk.Button(button_frame, text='Adding DISH',command = self.addingdish, width=21, height=2, font=("Times New Roman", 16))
        button_dish.pack(pady=5)
        Button(self, text="HOME PAGE",
               command=lambda: controller.show_page("HomePage")).grid(row=4, column=11)
        Button(self, text="EXIT", command=controller.close_windows).grid(row=5, column=11)
        
        



if __name__ == "__main__":
    app = App()
    app.mainloop()
